-- Creates table id_not_null in database passed as argument of
--   the mysql command.
CREATE TABLE IF NOT EXISTS id_not_null (
       id	INT		DEFAULT 1,
       name	VARCHAR(256)
);
