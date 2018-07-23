PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE urls(full_url varchar(50), smol_url varchar(10));
INSERT INTO "urls" VALUES('www.rubyisgood.c','sm.ol/rubyn');
COMMIT; 
