from db import get_db_connection

def create_post(user_id, content):
    """
    Create a new post in the database with the given user_id and content.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the new post into the posts table
    cursor.execute(
        """
        INSERT INTO posts (user_id, content) 
        VALUES (%s, %s)
        RETURNING id, user_id, content, created_at;
        """, 
        (user_id, content)
    )
    
    # Fetch the newly created post record
    post = cursor.fetchone()
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    # Return the created post record to the caller
    return post


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