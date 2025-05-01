# Creating table for clock in and out to calculate the hours

create_working_hours="""CREATE TABLE IF NOT EXISTS working_hours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    badgenum INTEGER NOT NULL,
    clockin TIMESTAMP,
    clockout TIMESTAMP,
    clockstate BOOLEAN DEFAULT FALSE,
    clockhours INTEGER,
    FOREIGN KEY (user_profile_id) REFERENCES user(id)
);"""

# Creating simple user table for simple join 
create_user_table="""CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL
);"""
