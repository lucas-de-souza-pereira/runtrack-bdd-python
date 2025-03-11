mysql> SELECT MIN(age) AS "age du plus jeune etudiant" FROM etudiant;
+----------------------------+
| age du plus jeune etudiant |
+----------------------------+
|                         16 |
+----------------------------+
1 row in set (0.00 sec)

 SELECT * FROM etudiant WHERE age = (SELECT MIN(age) FROM etudiant);
+----+--------+--------+-----+-------------------------------+
| id | nom    | prenom | age | email                         |
+----+--------+--------+-----+-------------------------------+
|  4 | Barnes | Binkie |  16 | binkie.barnes@laplateforme.io |
+----+--------+--------+-----+-------------------------------+
1 row in set (0.02 sec)