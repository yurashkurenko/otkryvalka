BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "users" (
	"id"	INTEGER NOT NULL UNIQUE,
	"user"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "boxes" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	TEXT,
	"api"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "boxusers" (
	"id"	INTEGER NOT NULL UNIQUE,
	"box"	TEXT,
	"users"	TEXT,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "budget" (
	"codename"	varchar(255),
	"daily_limit"	integer,
	PRIMARY KEY("codename")
);
CREATE TABLE IF NOT EXISTS "category" (
	"codename"	varchar(255),
	"name"	varchar(255),
	"is_base_expense"	boolean,
	"aliases"	text,
	PRIMARY KEY("codename")
);
CREATE TABLE IF NOT EXISTS "expense" (
	"id"	integer,
	"amount"	integer,
	"created"	datetime,
	"category_codename"	integer,
	"raw_text"	text,
	FOREIGN KEY("category_codename") REFERENCES "category"("codename"),
	PRIMARY KEY("id")
);
INSERT INTO "users" VALUES (1,'yurasoft10');
INSERT INTO "users" VALUES (4,'yurasoft10');
INSERT INTO "users" VALUES (5,'yurasoft10');
INSERT INTO "users" VALUES (6,'yurasoft10');
INSERT INTO "users" VALUES (7,'yurasoft10');
INSERT INTO "users" VALUES (8,'yurasoft10');
INSERT INTO "users" VALUES (9,'yurasoft1');
INSERT INTO "users" VALUES (10,'yurasoft1-');
INSERT INTO "users" VALUES (11,'yurasoft1+');
INSERT INTO "users" VALUES (12,'yurasoft1');
INSERT INTO "users" VALUES (13,'yurasoft1-');
INSERT INTO "users" VALUES (14,'yurasoft1+');
INSERT INTO "users" VALUES (15,'yurasoft1');
INSERT INTO "users" VALUES (16,'yurasoft1-');
INSERT INTO "users" VALUES (17,'yurasoft1+');
INSERT INTO "users" VALUES (18,'yurasoft1');
INSERT INTO "users" VALUES (19,'yurasoft1-');
INSERT INTO "users" VALUES (20,'yurasoft1+');
INSERT INTO "users" VALUES (21,'yurasoft1');
INSERT INTO "users" VALUES (22,'yurasoft1-');
INSERT INTO "users" VALUES (23,'yurasoft1+');
INSERT INTO "budget" VALUES ('base',500);
INSERT INTO "category" VALUES ('products','РїСЂРѕРґСѓРєС‚С‹',1,'РµРґР°');
INSERT INTO "category" VALUES ('coffee','РєРѕС„Рµ',1,'');
INSERT INTO "category" VALUES ('dinner','РѕР±РµРґ',1,'СЃС‚РѕР»РѕРІР°СЏ, Р»Р°РЅС‡, Р±РёР·РЅРµСЃ-Р»Р°РЅС‡, Р±РёР·РЅРµСЃ Р»Р°РЅС‡');
INSERT INTO "category" VALUES ('cafe','РєР°С„Рµ',1,'СЂРµСЃС‚РѕСЂР°РЅ, СЂРµСЃС‚, РјР°Рє, РјР°РєРґРѕРЅР°Р»СЊРґСЃ, РјР°РєРґР°Рє, kfc, ilpatio, il patio');
INSERT INTO "category" VALUES ('transport','РѕР±С‰. С‚СЂР°РЅСЃРїРѕСЂС‚',0,'РјРµС‚СЂРѕ, Р°РІС‚РѕР±СѓСЃ, metro');
INSERT INTO "category" VALUES ('taxi','С‚Р°РєСЃРё',0,'СЏРЅРґРµРєСЃ С‚Р°РєСЃРё, yandex taxi');
INSERT INTO "category" VALUES ('phone','С‚РµР»РµС„РѕРЅ',0,'С‚РµР»Рµ2, СЃРІСЏР·СЊ');
INSERT INTO "category" VALUES ('books','РєРЅРёРіРё',0,'Р»РёС‚РµСЂР°С‚СѓСЂР°, Р»РёС‚СЂР°, Р»РёС‚-СЂР°');
INSERT INTO "category" VALUES ('internet','РёРЅС‚РµСЂРЅРµС‚',0,'РёРЅРµС‚, inet');
INSERT INTO "category" VALUES ('subscriptions','РїРѕРґРїРёСЃРєРё',0,'РїРѕРґРїРёСЃРєР°');
INSERT INTO "category" VALUES ('other','РїСЂРѕС‡РµРµ',1,'');
COMMIT;
