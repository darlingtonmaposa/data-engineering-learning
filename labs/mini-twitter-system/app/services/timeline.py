from db import get_db_connection


def get_timeline(user_id):
    """
    Retrieves the timeline for a given user by fetching posts from the database.
    The timeline includes posts from the user and their followers, ordered by creation time.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch posts from the user and their followers
    query = """
        SELECT p.id, u.username, p.content, p.created_at
        FROM follows f
        JOIN posts p ON f.followee_id = p.user_id
        JOIN users u ON p.user_id = u.id
        WHERE f.follower_id = %s
        ORDER BY p.created_at DESC, p.id DESC
    """
    cursor.execute(query, (user_id,))
    posts = cursor.fetchall()

    cursor.close()
    conn.close()

    return posts            