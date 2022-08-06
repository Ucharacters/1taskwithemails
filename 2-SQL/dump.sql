BEGIN TRANSACTION;

CREATE TABLE user(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       email TEXT);
INSERT INTO "user" VALUES(1,'Иван','1@1.com');
INSERT INTO "user" VALUES(2,'Владимир','2@1.com');
INSERT INTO "user" VALUES(3,'Кирилл','3@1.com');
INSERT INTO "user" VALUES(4,'Константин','4@1.com');
INSERT INTO "user" VALUES(5,'Пётр','5@1.com');

CREATE TABLE subjects(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT);
INSERT INTO "subjects" VALUES(1,'русский язык');
INSERT INTO "subjects" VALUES(2,'литература');
INSERT INTO "subjects" VALUES(3,'математика');
INSERT INTO "subjects" VALUES(4,'иностранный язык');
INSERT INTO "subjects" VALUES(5,'история');

CREATE TABLE result(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        result FLOAT,
        user_id INTEGER,
        subject INTEGER,
        FOREIGN KEY (user_id) REFERENCES user(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
        FOREIGN KEY (subject) references subjects(id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
    );
INSERT INTO "result" VALUES(1,95.0,4,1);
INSERT INTO "result" VALUES(2,75.0,4,2);
INSERT INTO "result" VALUES(3,85.0,4,3);
INSERT INTO "result" VALUES(4,65.0,4,4);
INSERT INTO "result" VALUES(5,44.0,1,4);
INSERT INTO "result" VALUES(6,34.0,1,2);
INSERT INTO "result" VALUES(7,24.0,1,3);
INSERT INTO "result" VALUES(8,14.0,1,1);
INSERT INTO "result" VALUES(9,93.0,2,2);
INSERT INTO "result" VALUES(10,73.0,2,3);
INSERT INTO "result" VALUES(11,83.0,2,1);
INSERT INTO "result" VALUES(12,97.0,5,2);
INSERT INTO "result" VALUES(13,77.0,5,3);
INSERT INTO "result" VALUES(14,87.0,5,1);
INSERT INTO "result" VALUES(15,77.0,5,5);
INSERT INTO "result" VALUES(16,87.0,5,4);
INSERT INTO "result" VALUES(17,82.0,3,3);
INSERT INTO "result" VALUES(18,62.0,3,2);
COMMIT;

SELECT user.name, result.result, subjects.name
FROM result
JOIN user ON user.id==result.user_id
JOIN subjects ON subjects.id==result.subject
ORDER BY result.result DESC
LIMIT 3;

SELECT user.name, sum(result.result) AS total_score
FROM result
JOIN user ON user.id==result.user_id
GROUP BY user.id
HAVING count(result.result)>=3 AND total_score >= 200
ORDER BY total_score  DESC
LIMIT 3;