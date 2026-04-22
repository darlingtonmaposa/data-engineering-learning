from services.users import get_all_users, get_user_by_id
from services.posts import get_all_posts, get_post_by_id
from services.timeline import get_timeline



def test_get_all_users():
    # Retrieve all users
    users = get_all_users()
    
    for user in users:  
        print(f"User ID: {user[0]}, Username: {user[1]}")


def test_get_user_by_id(user_id):
    # Retrieve a user by ID
    user = get_user_by_id(user_id)
    
    if user:
        print(f"User ID: {user[0]}, Username: {user[1]}")
    else:
        print(f"No user found with ID: {user_id}")

def test_get_all_posts():
    # Retrieve all posts
    posts = get_all_posts()
    
    for post in posts:  
        print(f"Post ID: {post[0]}, User ID: {post[1]}, Content: {post[2]}")

def test_get_post_by_id(post_id):
    # Retrieve a post by ID
    post = get_post_by_id(post_id)
    
    if post:
        print(f"Post ID: {post[0]}, User ID: {post[1]}, Content: {post[2]}")
    else:
        print(f"No post found with ID: {post_id}")

def test_get_timeline(user_id):
    # Retrieve the timeline for a user
    timeline = get_timeline(user_id)
    
    print("Alice's timeline:")
    for post_id, author_name, content, created_at in timeline:
        print(f"[{created_at}] {author_name}: {content}")


if __name__ == "__main__":
    # test_get_all_users()
    # test_get_user_by_id(user_id=1)
    # test_get_all_posts()
    # test_get_post_by_id(post_id=2)
    test_get_timeline(user_id=1)