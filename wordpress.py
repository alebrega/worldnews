from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import GetPosts, NewPost
from wordpress_xmlrpc.methods.users import GetUserInfo
from wordpress_uploadpic import upload_pic

wp = Client('https://www.thestartupfounder.com/xmlrpc.php',
            'alebrega', 'JSoWLaPm*b*MZm9qG$')


def publish(title, content, image_url, keywords):
    post = WordPressPost()
    post.title = title
    post.content = content
    post.status = 'draft'
    attachment_id = upload_pic(image_url)
    post.thumbnail = attachment_id
    post.terms_names = {
        'post_tag': keywords,
        'category': ['To review']
    }
    wp.call(NewPost(post))
    return True
