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



--  select * from linki 
--  where id < 105;
--DROP TABLE linki;

--vstavljanje podatkov noter

INSERT INTO linki(
    comick_link,
    id,
    al_link, 
    ap_link,
    mu_link,
    raw_link,  
    mb_link,
    bw_link,
    mal_link,
    md_link,
    cover_url
)
VALUES(https://comick.dev/comic/osekkai-joshi-koi-o-suru,100,NA,NA,NA,https://comic-walker.com/detail/KC_008412_S/episodes/KC_0084120000300011_E?episodeType=latest,NA,de998d3269-d9af-448b-a1d3-c7ef7ce64853/?adpcnt=7qM_SasK,NA,NA,https://meo.comick.pictures/EOdpN2-s.jpg);


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

ALTER TABLE basic_info
ADD CONSTRAINT basic_info_pkey PRIMARY KEY (comick_link);


--tabela tags

CREATE TABLE tags(
    id INTEGER,
    comick_link TEXT,
    tag TEXT,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

INSERT INTO tags(
    id,
    comick_link,
    tag
)
VALUES(2697,'https://comick.dev/comic/villainess-level-99-i-may-be-the-hidden-boss-but-i-m-not-the-demon-lordiWcu','Female Protagonist');

--column id was used only for testing purposes when gathering data so it has no value(not unique or anything)
ALTER TABLE tags
DROP COLUMN id;

--table translation

CREATE TABLE translation(
    comick_link TEXT PRIMARY KEY,
    official_translation BOOLEAN,
    fan_translation BOOLEAN,
    number_fan_translated NUMERIC,
    number_together NUMERIC,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

INSERT INTO translation(
    comick_link,
    official_translation,
    fan_translation,
    number_fan_translated,
    number_together_light)
    VALUES('https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','True','True','24','91');

--description

create TABLE description(
    id integer PRIMARY KEY,
    comick_link TEXT UNIQUE,
    description TEXT,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

INSERT INTO description(
    id,
    comick_link,
    description
)
VALUES(100,'https://comick.dev/comic/osekkai-joshi-koi-o-suru',NULL);--fix shiboyugi

--relations

CREATE TABLE relations(
    comick_link text,
    related_link text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
    --FOREIGN KEY(related_link) REFERENCES linki(comick_link) under normal circumstances would do that but because data wasnt taken on the same day there are entries that arent in comick_link
);


INSERT INTO relations(
    comick_link,
    related_link)
    VALUES('https://comick.dev/comic/the-young-lady-who-was-blessed-by-the-gorilla-god-is-adored-in-the-royal-knight-order','https://comick.dev/comic/gorilla-no-kami-kara-kago-sareta-reijou-wa-ouritsu-kishidan-de-kawaigarareru');

-- Delete one of each duplicate pair
WITH duplicates AS (
    SELECT
        ctid,  -- PostgreSQL row identifier
        ROW_NUMBER() OVER (
            PARTITION BY LEAST(comick_link, related_link),
                         GREATEST(comick_link, related_link)
            ORDER BY comick_link
        ) AS rn
    FROM relations
)
DELETE FROM relations
WHERE ctid IN (
    SELECT ctid
    FROM duplicates
    WHERE rn > 1
);

CREATE UNIQUE INDEX unique_pair_idx
ON relations (LEAST(comick_link, related_link), GREATEST(comick_link, related_link));

--recommendations

CREATE TABLE recommendations(
    comick_link text,
    recommended_link text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
    --FOREIGN KEY(recommended_link) REFERENCES linki(comick_link) under normal circumstances would do that but because data wasnt taken on the same day there are entries that arent in comick_link
);

INSERT INTO recommendations(
    comick_link,
    recommended_link)
VALUES('https://comick.dev/comic/02-one-punch-man-official','https://comick.dev/comic/heion-sedai-no-idaten-tachi');

-- Remove duplicates in recommendations
WITH duplicates AS (
    SELECT
        ctid,  -- PostgreSQL row identifier
        ROW_NUMBER() OVER (
            PARTITION BY LEAST(comick_link, recommended_link),
                         GREATEST(comick_link, recommended_link)
            ORDER BY comick_link
        ) AS rn
    FROM recommendations
)


DELETE FROM recommendations
WHERE ctid IN (
    SELECT ctid
    FROM duplicates
    WHERE rn > 1
);

-- Enforce canonical uniqueness without extra columns
CREATE UNIQUE INDEX unique_recommendation_idx
ON recommendations (
    LEAST(comick_link, recommended_link),
    GREATEST(comick_link, recommended_link)
);

--genres

CREATE TABLE genres(
    id INTEGER,--will be removed(testing purposes before) missing data will have to be added
    comick_link text,
    genre text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

INSERT INTO genres(
    id,
    comick_link,
    genre)
    VALUES(11220,'https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','Action');

ALTER TABLE genres
ADD CONSTRAINT unique_comick_genre UNIQUE (comick_link, genre);

--titles
create table titles(
    id INTEGER, --removed
    comick_link text,
    title text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);

INSERT INTO titles 
values(11220,'https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','Playing Death Games to Put Food on the Table')
--delete from titles

--themes

CREATE TABLE themes(
    id INTEGER,--will be removed(testing purposes before) missing data will have to be added
    comick_link text,
    themes text,
    FOREIGN KEY(comick_link) REFERENCES linki(comick_link)
);


INSERT INTO themes
    VALUES(11220,'https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu,'Survival');


alter table themes drop column id

SELECT comick_link, title, COUNT(*) AS count
FROM titles
GROUP BY comick_link, title
HAVING COUNT(*) > 1;

select * from titles where comick_link='https://comick.dev/comic/삼이는 재생한다'

SELECT comick_link, genre, COUNT(*) AS count
FROM genres
GROUP BY comick_link, genre
HAVING COUNT(*) > 1;


ALTER TABLE titles
ADD CONSTRAINT unique_comick_title UNIQUE (comick_link, title);

--authors

Create table authors(
id integer primary key,
comick_link text,
author text,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));

insert into authors values(14796,'https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','Yuuji Ukai');

--artists

Create table artists(
id integer primary key,
comick_link text,
artist text,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));


insert into artists values(14266,'https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','Banzai Kotobuki Dai Enkai');

--ratings

Create table ratings(
comick_link text primary key,
ranked integer,
followed integer,
bay_rating numeric,
FOREIGN KEY(comick_link) REFERENCES linki(comick_link));


insert into ratings values('https://comick.dev/comic/shibou-yuugi-de-meshi-wo-kuu','7289','1806','6.28');
