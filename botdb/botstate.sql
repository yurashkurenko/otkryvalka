BEGIN TRANSACTION;
INSERT INTO "botstate" VALUES (1,'пользователи','основной',NULL,NULL,'пользователи основной уровень','добавление удаление назад');
INSERT INTO "botstate" VALUES (2,'пользователи','добавление',NULL,NULL,'пользователи добавление','добавление список назад');
INSERT INTO "botstate" VALUES (3,'пользователи','удаление',NULL,NULL,'пользователи удаление','удаление список назад');
INSERT INTO "botstate" VALUES (4,'боксы','основной',NULL,NULL,'боксы основной уровень','добавление удаление назад');
INSERT INTO "botstate" VALUES (5,'боксы','добавление',NULL,NULL,'боксы добавление','добавление список назад');
INSERT INTO "botstate" VALUES (6,'боксы','удаление',NULL,NULL,'боксы удаление','удаление список назад');
INSERT INTO "botstate" VALUES (7,'управление','основной',NULL,NULL,'управление основной уровень','бокс пользователи назад');
INSERT INTO "botstate" VALUES (8,'управление','боксы',NULL,NULL,'управление выбор бокса','выбор назад');
INSERT INTO "botstate" VALUES (9,'управление','пользователи',NULL,NULL,'управление выбор пользователей','выбор назад');
INSERT INTO "botstate" VALUES (10,'основной','основной',NULL,NULL,'управление','пользователи боксы управление');
COMMIT;
