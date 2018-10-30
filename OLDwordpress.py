import requests
import json
import base64
from slugify import slugify

user = 'alebrega'
pythonapp = 'JSoWLaPm*b*MZm9qG$'
url = 'https://www.thestartupfounder.com/api/posts/create_post/'

token = base64.standard_b64encode(b'user + ":" + pythonapp')
headers = {'Authorization: Basic ' + str(token)}


def publish(title, content, image_url, keywords):
    try:
        post = {
            'title': title,
            'slug': slugify(title),
            'status': 'draft',
            'content': content,
            'author': '1',
            'excerpt': content[:15]+"...",
            'format': 'standard'
        }

        r = requests.post(url, headers=headers, json=post)
        print(r)
        #print('Your post is published on ' + json.loads(r.content)['link'])
        return True
    except Exception as e:
        print('Failed to create a post in Wordpress: ' + str(e))
        return False
