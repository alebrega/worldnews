from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.compat import xmlrpc_client
from wordpress_xmlrpc.methods import media, posts
import uuid
import requests


client = Client('https://www.thestartupfounder.com/xmlrpc.php',
                'alebrega', 'JSoWLaPm*b*MZm9qG$')


def upload_pic(img_url):
    try:
        img_data = requests.get(img_url).content
        img_name = './uploads/'+str(uuid.uuid4())+'.jpg'
        with open(img_name, 'wb') as handler:
            handler.write(img_data)

        filename = img_name

        # prepare metadata
        data = {
            'name': img_name,
            'type': 'image/jpeg',  # mimetype
        }

        # read the binary file and let the XMLRPC library encode it into base64
        with open(filename, 'rb') as img:
            data['bits'] = xmlrpc_client.Binary(img.read())

        response = client.call(media.UploadFile(data))
        attachment_id = response['id']
    except Exception as e:
        print('Some errors trying to save the image from remote host: ' + str(img_url))
        attachment_id = ""

    return attachment_id
