from db import get_db_connection


def create_follow(follower_id, followee_id):
    """
    Create a new follow relationship in the database with the given follower_id and followee_id.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the new follow relationship into the follows table
    cursor.execute(
        """
        INSERT INTO follows (follower_id, followee_id) 
        VALUES (%s, %s)
        RETURNING follower_id, followee_id, created_at;
        """, 
        (follower_id, followee_id)
    )
    
    # Fetch the newly created follow record
    follow = cursor.fetchone()
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    # Return the created follow record to the caller
    return follow