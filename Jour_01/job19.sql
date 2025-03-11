mysql> SELECT COUNT(*) FROM etudiant;
+----------+
| COUNT(*) |
+----------+
|        5 |
+----------+
1 row in set (0.09 sec)

mysql> SELECT COUNT(id) FROM etudiant
    -> ;
+-----------+
| COUNT(id) |
+-----------+
|         5 |
+-----------+
1 row in set (0.01 sec)