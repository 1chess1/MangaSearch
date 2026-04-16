--ustarjanje tabel


--tabela linki

 create TABLE linki(
    comick_link TEXT NOT NULL,
    id INTEGER PRIMARY KEY NOT NULL,
    al_link TEXT, 
    ap_link TEXT,
    mu_link TEXT,
    raw_link TEXT,  
    mb_link TEXT,
    bw_link TEXT,
    mal_link TEXT,
    md_link TEXT,
    cover_url TEXT 
 );



--vstavljanje podatkov noter

--tabela basic_info

CREATE TABLE basic_info(
    comick_link TEXT,
    origination TEXT,
    demographic INTEGER,
    published INTEGER,
    status INTEGER,
    format TEXT,
    anime BOOLEAN,
    FOREIGN KEY (comick_link) REFERENCES linki(comick_link)
);


--tabela tags

CREATE TABLE tags(
    id INTEGER,
    comick_link TEXT,
    tag TEXT,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

--table translation

CREATE TABLE translation(
    comick_link TEXT PRIMARY KEY,
    official_translation BOOLEAN,
    fan_translation BOOLEAN,
    number_fan_translated NUMERIC,
    number_together NUMERIC,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);


--description

create TABLE description(
    id integer PRIMARY KEY,
    comick_link TEXT UNIQUE,
    description TEXT,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

--relations

CREATE TABLE relations(
    comick_link text,
    related_link text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
    --FOREIGN KEY(related_link) REFERENCES linki(comick_link) under normal circumstances would do that but because data wasnt taken on the same day there are entries that arent in comick_link
);

--recommendations

CREATE TABLE recommendations(
    comick_link text,
    recommended_link text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
    --FOREIGN KEY(recommended_link) REFERENCES linki(comick_link) under normal circumstances would do that but because data wasnt taken on the same day there are entries that arent in comick_link
);

--genres

CREATE TABLE genres(
    comick_link text,
    genre text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

--titles
create table titles(
    comick_link text,
    title text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

--themes

CREATE TABLE themes(
    comick_link text,
    themes text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);


--authors

Create table authors(
id integer primary key,
comick_link text,
author text,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));


--artists

Create table artists(
id integer primary key,
comick_link text,
artist text,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));


--ratings

Create table ratings(
comick_link text primary key,
ranked integer,
followed integer,
bay_rating numeric,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));

create table users(
    user_id  serial primary key, 
    username text UNIQUE,
    email text UNIQUE,
    password text
);

create table reading(
    reading_id serial primary key,
    user_id INTEGER,
    comick_link TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id),
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

create table clicks(
    clicks_id serial primary key,
    user_id INTEGER,
    clicked_link TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

create TABLE searches(
    searches_id serial PRIMARY key,
    user_id INTEGER,
    searched TEXT,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);


create table user_analysis(--maybe adding stuff
    user_id integer PRIMARY KEY,
    gender_count INTEGER,
    gender_guess TEXT,
    age_count INTEGER,
    age_guess INTEGER,
    user_rank_genres_count INTEGER,
    user_rank_genres INTEGER,
    user_rank_title_count INTEGER,
    user_rank_title INTEGER,
    user_rank_quality_count INTEGER,
    user_rank_quality INTEGER,
    user_rank INTEGER,
    danger_count INTEGER,
    danger_alert BOOLEAN,
    bot_alert BOOLEAN,
    a_rank INTEGER,
    a_count INTEGER,
    FOREIGN KEY(user_id) REFERENCES users(user_id)
);

