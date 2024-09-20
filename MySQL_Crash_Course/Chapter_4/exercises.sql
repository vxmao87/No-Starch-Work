-- 4-1
CREATE DATABASE IF NOT EXISTS rapper;

USE rapper;

CREATE TABLE album
(
	rapper_id				smallint UNSIGNED,
    album_name				varchar(100),
    explicit_lyrics_flag	bool,
    album_revenue			decimal(12,2),
    album_content			longblob
);
