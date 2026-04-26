from db import get_db_connection


# This function is called when a user creates a new post or when a followee creates a post.
def add_post_to_timeline(author_id, post_id):
    """
    Adds a post to a user's timeline by inserting a record into the timeline table.
    This function is called when a user creates a new post or when a followee creates a post.

    Args:
        author_id (int): The ID of the user who created the post.
        post_id (int): The ID of the post being added to the timeline.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Step 1: Find the author's followers   
        cursor.execute(
            """
            SELECT follower_id 
            FROM follows 
            WHERE followee_id = %s;
            """, 
            (author_id,)
        )

        followers = cursor.fetchall()

        # Step 2: insert a timeline entry for each follower
        for follower in followers:
            follower_id = follower[0]
            cursor.execute(
                """
                -- Insert a new timeline entry for the follower and post
                INSERT INTO timeline (user_id, post_id) 
                VALUES (%s, %s)
                -- Ensure that we don't insert duplicate timeline entries for the same user and post
                ON CONFLICT (user_id, post_id) DO NOTHING;
                """, 
                (follower_id, post_id) 
            )

        conn.commit()  # Commit after each insert to ensure timeline is updated immediately


    except Exception as e:
        conn.rollback()  # Rollback in case of any error
        raise e  # Re-raise the exception after rollback
    finally:
        cursor.close()
        conn.close()



def get_timeline(user_id):
    """
    Retrieves the timeline for a given user by fetching posts from the database.
    The timeline includes posts from the user and their followers, ordered by creation time.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # Fetch user followees and their posts for the timeline
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

