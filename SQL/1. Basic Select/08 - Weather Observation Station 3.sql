-- MySQL
SELECT DISTINCT CITY
FROM STATION
WHERE ID % 2 = 0;

-- Oracle
SELECT DISTINCT CITY
FROM STATION
WHERE MOD(ID, 2) = 0; 