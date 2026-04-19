-- SQL schema for a simple social media application

-- Stores user accounts in the system.
-- Each row represents one user.
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE, -- Username should be unique so that each account has one public identity.
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Stores posts made by users.
-- Each row represents one post made by a user.
CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Stores the "follow" relationships between users.
-- Each row represents one user following another user.
CREATE TABLE IF NOT EXISTS follows (
    follower_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    followee_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (follower_id, followee_id), -- Composite primary key to prevent duplicate follow relationships
    CHECK (follower_id <> followee_id) -- Prevent users from following themselves
);


