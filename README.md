Summary
The purpose of this project is to create and load a star schema for storing Sparkify's app data. The files persisted are song JSON files and log files from the app. Using proper ETL techniques, the schema will store the songs, artists, users, and time as dimension tables and the song play data as the fact table.

Schema
Name: sparkify
Tables:
    artists (artist_id, name, location, latittude, longitude) - the artist data of the songs in the app 
    songs (song_id, title, artist_id, year, duration) - the song data of the songs in the app
    songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) - the play data for a song played by a user on the app
    time (start_time, hour, day, week, month, year, weekday) - the song timestamp data broken into different units of measurement
    users (user_id, first_name, last_name, gender, level) - the user data for the app

How to Run
Run the following files in the below order to create and populate the database:
1. create_tables.py
2. etl.py

Files
create_tables.py - The script used to drop and create the tables where possible. Provides the control logic for drops and creations. 
etl.py - The script used to load the song JSON file and app log file data. Provides the control logic for the ETL process.
sql_queries.py - The script used to store all of queries used for the project. Provides a centrilized location for query changes.

ETL Process Explanation
The files are loaded via the following process:
1. The song files are loaded and used to populate the song and artist tables.
2. The log files are loaded and used to populate the time, user, and songplay tables.
