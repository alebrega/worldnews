from flask import Flask
from flask import request, jsonify, abort
from urllib.request import urlopen, URLError, urlparse
from get_links import save_article

app = Flask(__name__)


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
    if valid_url(url):
        response = save_article(url, languange_to_translate)
        return jsonify({'url': url, 'success': response})
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
