import newspaper
from newspaper import Article, fulltext
import json
from google.cloud import translate
from wordpress import publish


def translate_from_google(text, target_language):
    if (len(text) == 0 or len(target_language) == 0):
        return text
    try:
        client = translate.Client.from_service_account_json(
            './api_translate.json')
        result = client.translate(
            text, target_language=target_language)
        return result['translatedText']
    except Exception as e:
        print('Failed to translate text: ' + str(e))
        print("Google translate exception")
        return text


def save_article(url, lang):
    try:
        a = Article(url)
        a.download()
        a.parse()
        data = {}
        data['article'] = []
        title = translate_from_google(a.title, lang)
        text = translate_from_google(a.text, lang)
        a.nlp()
        keywords =  translate_from_google(a.keywords,lang)
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
        'keywords': keywords,
        'summary': summary,
        'url': url
    })
    with open("articles.json", "a", encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False)

    if (publish(title, text, a.top_img, keywords)):
        print("Publish OK")
        return True
    else:
        print("Error in publishing")
        return False
    return "Parse OK"
