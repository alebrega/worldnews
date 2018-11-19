from flask import Flask
from flask import request, jsonify, abort
from urllib.request import urlopen, URLError, urlparse
from article import save_article
from models import get_engine, articles
from sqlalchemy.sql import table, column, select

app = Flask(__name__)

engine = get_engine()
conn = engine.connect()


def valid_url(url):
    parsed_url = urlparse(url)
    return bool(parsed_url.scheme)


@app.route('/')
def index():
    return "Read API instructions"


@app.route('/api/article', methods=['POST'])
def get_task():
    content = request.json
    url = content['url']
    languange_to_translate = content['lang']
    keywords_matching = content['keywords_matching']
    old_days = content['old_days']
    t = table('articles', column('url'))
    s = select([t]).where(t.c.url == url)
    r = conn.execute(s)
    results = r.fetchall()
    if (len(results) > 0):
        return jsonify({'url': url, 'success': False, 'error': 'URL was used before'})

    if valid_url(url):
        response = save_article(
            url, languange_to_translate, keywords_matching, old_days)
        if response['success']:
            return jsonify({'url': url, 'success': response['success'], 'message': response['message']})
        else:
            return jsonify({'url': url, 'success': response['success'], 'message': response['error']})
    else:
        return jsonify({'url': url, 'success': False, 'error': 'URL is no valid'})

    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
