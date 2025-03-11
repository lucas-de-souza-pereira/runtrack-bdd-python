 SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant);
+----+-------+--------+-----+-----------------------------+
| id | nom   | prenom | age | email                       |
+----+-------+--------+-----+-----------------------------+
|  2 | Steak | Chuck  |  45 | chuck.steak@laplateforme.io |
+----+-------+--------+-----+-----------------------------+
1 row in set (0.00 sec)


SELECT MAX(age) AS "age du plus agé etudiant" FROM etudiant;
+--------------------------+
| age du plus agé etudiant |
+--------------------------+
|                       45 |
+--------------------------+
1 row in set (0.00 sec)