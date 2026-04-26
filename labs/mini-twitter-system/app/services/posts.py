from db import get_db_connection
from services.timeline import add_post_to_timeline

def create_post(user_id, content):
    """
    Create a new post in the database with the given user_id and content.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        # Insert the new post into the posts table
        cursor.execute(
            """
            INSERT INTO posts (user_id, content) 
            VALUES (%s, %s)
            RETURNING id;
            """, 
            (user_id, content)
        )
        
        # Fetch the newly created post record
        post_id = cursor.fetchone()[0]  # Get the post ID from the returned record
        
        # Commit the transaction and close the connection
        conn.commit()
        cursor.close()
        conn.close()
        

        add_post_to_timeline(user_id, post_id)  # Add the new post to the timelines of followers

        # Return the created post record to the caller
        return post_id # Return the post ID instead of the full record, since we only need the ID for timeline updates

    except Exception as e:
        conn.rollback()  # Rollback in case of any error
        raise e  # Re-raise the exception after rollback

    finally:
        cursor.close()
        conn.close()


def get_all_posts():            
    """
    Retrieve all posts from the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute a query to fetch all posts
    cursor.execute(
        """
        SELECT id, user_id, content, created_at 
        FROM posts;
        """
    )
    
    # Fetch all post records
    posts = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return posts

def get_post_by_id(post_id):
    """
    Retrieve a post from the database by its ID.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute a query to fetch the post with the specified ID
    cursor.execute(
        """
        SELECT id, user_id, content, created_at 
        FROM posts 
        WHERE id = %s;
        """, 
        (post_id,)
    )
    
    # Fetch the post record
    post = cursor.fetchone()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return post