-- Creates table unique in database passed as argument of
--   the mysql command.
CREATE TABLE IF NOT EXISTS unique_id (
       id	INT		DEFAULT 1	UNIQUE,
       name	VARCHAR(256)
);
