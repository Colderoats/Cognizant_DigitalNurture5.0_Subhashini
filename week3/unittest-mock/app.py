from database import get_user
import requests

def fetch_user(user_id):
    return get_user(user_id)

def fetch_post(post_id):
    response = requests.get(
        f"https://jsonplaceholder.typicode.com/posts/{post_id}"
    )
    return response.json()