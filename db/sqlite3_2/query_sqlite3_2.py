working_hours_per_user="""CREATE TABLE IF NOT EXISTS working_hours_per_user(
    id INT PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(50) NOT NULL,
    total_hours INT NOT NULL
);"""