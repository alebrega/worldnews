import newspaper
from newspaper import Article, fulltext
import json
from google.cloud import translate
from wordpress import Wordpress
from datetime import datetime, timezone
import pytz
from keywords import is_similar_context, get_keywords_from_text, get_keywords_nltk
import spacy
from urllib.request import urlopen
from unplash import get_pics

def translate_from_google(text, target_language, format='text'):

    if (len(text) == 0 or len(target_language) == 0):
        return text
    try:
        client = translate.Client.from_service_account_json(
            './api_translate.json')
        result = client.translate(
            text, target_language=target_language, format_=format)
        return result['translatedText']
    except Exception as e:
        print('Failed to translate text: ' + str(e))
        print("Google translate exception")
        return text


def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)


def save_article(url, lang, keywords_matching, old_days):
    try:
        a = Article(url)
        a.download()
        a.parse()
        if a.publish_date is None:
            print("No publish date")
            try:
                with urlopen(url) as f:
                    conn = urlopen(url, timeout=30)
                    publish_date = conn.headers['last-modified']
                    if publish_date is None:
                        return False
                    print("Publish date from headers "+str(publish_date))
            except Exception as e:
                print('Cant get last modified date from headers' + str(e))
                return False
        else:
            publish_date = utc_to_local(a.publish_date)
        now = datetime.now(timezone.utc)
        time_between_insertion = now - publish_date
        if time_between_insertion.days > int(old_days):
            print("The insertion date is older than "+str(old_days)+" days")
            return False
        text = translate_from_google(a.text, lang, 'text')
        if (len(text) < 500):
            print("Text is less than 400 chars")
            return False
        try:
            matches = is_similar_context(text)
            print(matches)
        except Exception as e:
            print('Problems with similar context' + str(e))

        if (len(matches) < int(keywords_matching)):
            print("The keywords matching are less "+str(keywords_matching))
            return False
        data = {}
        data['article'] = []
        title = translate_from_google(a.title, lang)
        a.nlp()
        keywords = [keyword for keyword in a.keywords if len(keyword) > 3]
        keywords = [translate_from_google(keyword, lang)
                    for keyword in keywords]
        keywords.extend(get_keywords_from_text(text))
        k = set(keywords)
        unique_keywords = list(k)

        summary = translate_from_google(a.summary, lang)
    except Exception as e:
        print('Some errors trying to parse Article: ' + str(e))
        return False
    data['article'].append({
        'original_title': a.title,
        'title': title,
        'author':  a.authors,
        'original_text': a.text,
        'text':  text,
        'top_image': a.top_img,
        'keywords': unique_keywords,
        'summary': summary,
        'url': url,
        'date': publish_date.strftime("%B %d, %Y")
    })
    with open("articles.json", "a", encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)
    wp = Wordpress()
    query_for_images=(" ".join(get_keywords_nltk(text, 2)))
    images_src=get_pics(query_for_images,1)
    print (images_src)
    if (wp.publish(title, text,images_src[0], unique_keywords)):
        print("Publish OK")
        return True
    else:
        print("Error in publishing")
        return False
    return "Parse OK"
