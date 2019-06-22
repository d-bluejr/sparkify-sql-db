Summary<br>
The purpose of this project is to create and load a star schema for storing Sparkify's app data. The files persisted are song JSON files and log files from the app. Using proper ETL techniques, the schema will store the songs, artists, users, and time as dimension tables and the song play data as the fact table.

Schema<br>
Name: sparkify<br>
Tables:<br>
    artists (artist_id, name, location, latittude, longitude) - the artist data of the songs in the app <br>
    songs (song_id, title, artist_id, year, duration) - the song data of the songs in the app<br>
    songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) - the play data for a song played by a user on the app<br>
    time (start_time, hour, day, week, month, year, weekday) - the song timestamp data broken into different units of measurement<br>
    users (user_id, first_name, last_name, gender, level) - the user data for the app<br>

How to Run<br>
Run the following files in the below order to create and populate the database:<br>
1. create_tables.py
2. etl.py

Files<br>
create_tables.py - The script used to drop and create the tables where possible. Provides the control logic for drops and creations. <br>
etl.py - The script used to load the song JSON file and app log file data. Provides the control logic for the ETL process.<br>
sql_queries.py - The script used to store all of queries used for the project. Provides a centrilized location for query changes.<br>

ETL Process Explanation<br>
The files are loaded via the following process:<br>
1. The song files are loaded and used to populate the song and artist tables.<br>
2. The log files are loaded and used to populate the time, user, and songplay tables.<br>
