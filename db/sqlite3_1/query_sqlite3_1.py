# Creating simple user table

create_user_table="""CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    FOREIGN KEY(working_hours_id) REFERENCES working_hours(id));"""


# Creating table for clock in and out to calculate the hours

create_working_hours="""CREATE TABLE IF NOT EXISTS working_hours (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    badgenum INTEGER NOT NULL,
    clockin TIMESTAMP,
    clockout TIMESTAMP,
    clockstate BOOLEAN DEFAULT FALSE,
    clockhours INTEGER);"""