# TABLE NAMES

# The table names are stored in variables to make modifications of table names in queries simplier and unified
song_plays = "songplays"
users = "users"
songs = "songs"
artists = "artists"
time = "time"

# DROP TABLES

# The beginning part of all the drop queries are the same, so a variable is used to store and reuse that
drop_starter = "DROP TABLE IF EXISTS "

# The drop queries are constructed using the drop starter variable along with the table names
songplay_table_drop = drop_starter + song_plays
user_table_drop = drop_starter + users
song_table_drop = drop_starter + songs
artist_table_drop = drop_starter + artists
time_table_drop = drop_starter + time

# CREATE TABLES

# The beginning part of all the create queries are the same, so a variable is used to store and reuse that
create_starter = "CREATE TABLE IF NOT EXISTS "

# The create queries are created using the create starter variable, the table name, and the list of column definitions
songplay_table_create = create_starter + song_plays + (""" 
        (
            songplay_id   serial    primary key, 
            start_time    bigint    not null, 
            user_id       varchar   not null, 
            level         varchar, 
            song_id       varchar, 
            artist_id     varchar, 
            session_id    int, 
            location      varchar, 
            user_agent    varchar
        );
    """)
user_table_create = create_starter + users + (""" 
        (
            user_id       varchar   primary key, 
            first_name    varchar, 
            last_name     varchar, 
            gender        varchar, 
            level         varchar
        );
    """)
song_table_create = create_starter + songs + (""" 
        (
            song_id       varchar   primary key, 
            title         varchar, 
            artist_id     varchar, 
            year          int, 
            duration      float
        );
    """)
artist_table_create = create_starter + artists + (""" 
        (
            artist_id     varchar   primary key, 
            name          varchar, 
            location      varchar, 
            latitude      float, 
            longitude     float
        );
    """)
time_table_create = create_starter + time + (""" 
        (
            start_time    bigint    primary key, 
            hour          int, 
            day           int, 
            week          int, 
            month         int, 
            year          int, 
            weekday       varchar
        );
    """)

# INSERT RECORDS

# The beginning and middle part of all the insert queries are the same, so variables are used to store and reuse those
insert_starter = "INSERT INTO "
insert_values_mid = ") VALUES ("
insert_conflict_mid = ") ON CONFLICT"
insert_nothing_ender = " DO NOTHING"
insert_update_ender = "(user_id) DO UPDATE SET level=excluded.level"

# The insert queries are created using the insert starter variables, table name, column names, the mid value variable, and the insert variable blocks
songplay_table_insert = insert_starter + song_plays + " (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent" + insert_values_mid + "%s,%s,%s,%s,%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
user_table_insert = insert_starter + users + " (user_id, first_name, last_name, gender, level" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_update_ender
song_table_insert = insert_starter + songs + " (song_id, title, artist_id, year, duration" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
artist_table_insert = insert_starter + artists + " (artist_id, name, location, latitude, longitude" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
time_table_insert = insert_starter + time + " (start_time, hour, day, week, month, year, weekday" + insert_values_mid + "%s,%s,%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender

# FIND SONGS

song_select = "SELECT s.song_id, s.artist_id FROM songs s inner join artists a on (s.artist_id = a.artist_id) where s.title = %s and a.name = %s and s.duration = %s"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]# TABLE NAMES

# The table names are stored in variables to make modifications of table names in queries simplier and unified
song_plays = "songplays"
users = "users"
songs = "songs"
artists = "artists"
time = "time"

# DROP TABLES

# The beginning part of all the drop queries are the same, so a variable is used to store and reuse that
drop_starter = "DROP TABLE IF EXISTS "

# The drop queries are constructed using the drop starter variable along with the table names
songplay_table_drop = drop_starter + song_plays
user_table_drop = drop_starter + users
song_table_drop = drop_starter + songs
artist_table_drop = drop_starter + artists
time_table_drop = drop_starter + time

# CREATE TABLES

# The beginning part of all the create queries are the same, so a variable is used to store and reuse that
create_starter = "CREATE TABLE IF NOT EXISTS "

# The create queries are created using the create starter variable, the table name, and the list of column definitions
songplay_table_create = create_starter + song_plays + (""" 
        (
            songplay_id   serial    primary key, 
            start_time    bigint    not null, 
            user_id       varchar   not null, 
            level         varchar, 
            song_id       varchar, 
            artist_id     varchar, 
            session_id    int, 
            location      varchar, 
            user_agent    varchar
        );
    """)
user_table_create = create_starter + users + (""" 
        (
            user_id       varchar   primary key, 
            first_name    varchar, 
            last_name     varchar, 
            gender        varchar, 
            level         varchar
        );
    """)
song_table_create = create_starter + songs + (""" 
        (
            song_id       varchar   primary key, 
            title         varchar, 
            artist_id     varchar, 
            year          int, 
            duration      float
        );
    """)
artist_table_create = create_starter + artists + (""" 
        (
            artist_id     varchar   primary key, 
            name          varchar, 
            location      varchar, 
            latitude      float, 
            longitude     float
        );
    """)
time_table_create = create_starter + time + (""" 
        (
            start_time    bigint    primary key, 
            hour          int, 
            day           int, 
            week          int, 
            month         int, 
            year          int, 
            weekday       varchar
        );
    """)

# INSERT RECORDS

# The beginning and middle part of all the insert queries are the same, so variables are used to store and reuse those
insert_starter = "INSERT INTO "
insert_values_mid = ") VALUES ("
insert_conflict_mid = ") ON CONFLICT"
insert_nothing_ender = " DO NOTHING"
insert_update_ender = "(user_id) DO UPDATE SET level=excluded.level"

# The insert queries are created using the insert starter variables, table name, column names, the mid value variable, and the insert variable blocks
songplay_table_insert = insert_starter + song_plays + " (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent" + insert_values_mid + "%s,%s,%s,%s,%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
user_table_insert = insert_starter + users + " (user_id, first_name, last_name, gender, level" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_update_ender
song_table_insert = insert_starter + songs + " (song_id, title, artist_id, year, duration" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
artist_table_insert = insert_starter + artists + " (artist_id, name, location, latitude, longitude" + insert_values_mid + "%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender
time_table_insert = insert_starter + time + " (start_time, hour, day, week, month, year, weekday" + insert_values_mid + "%s,%s,%s,%s,%s,%s,%s" + insert_conflict_mid + insert_nothing_ender

# FIND SONGS

song_select = "SELECT s.song_id, s.artist_id FROM songs s inner join artists a on (s.artist_id = a.artist_id) where s.title = %s and a.name = %s and s.duration = %s"

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create,
                        time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]