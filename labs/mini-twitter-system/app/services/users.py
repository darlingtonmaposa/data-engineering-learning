from db import get_db_connection


def create_user(username):
    """
    Create a new user in the database with the given username.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Insert the new user into the users table
    cursor.execute(
        """
        INSERT INTO users (username) 
        VALUES (%s)
        RETURNING id, username, created_at;
        """, 
        (username,)
    )
    
    # Fetch the newly created user record
    user = cursor.fetchone()
    
    # Commit the transaction and close the connection
    conn.commit()
    cursor.close()
    conn.close()
    
    # Return the created user record to the caller
    return user


def get_all_users():
    """
    Retrieve all users from the database and return them as a list of dictionaries.
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute a query to fetch all users
    cursor.execute(
        """
        SELECT id, username, created_at 
        FROM users;
        """
    )
    
    # Fetch all user records
    users = cursor.fetchall()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    
    return users

    

def get_user_by_id(user_id):    
    """
    Retrieve a user from the database by their ID .
    """
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Execute a query to fetch the user with the specified ID
    cursor.execute(
        """
        SELECT id, username
        FROM users 
        WHERE id = %s;
        """, 
        (user_id,)
    )
    
    # Fetch the user record
    user = cursor.fetchone()
    
    # Close the connection
    cursor.close()
    conn.close()
    
    return user