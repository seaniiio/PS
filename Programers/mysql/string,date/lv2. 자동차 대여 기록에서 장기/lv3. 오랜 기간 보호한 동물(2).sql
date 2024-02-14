SELECT A.ANIMAL_ID, A.NAME
FROM ANIMAL_INS AS A JOIN ANIMAL_OUTS AS B ON A.ANIMAL_ID = B.ANIMAL_ID
ORDER BY DATEDIFF(DATE_FORMAT(B.DATETIME, '%Y-%m-%d'), DATE_FORMAT(A.DATETIME, '%Y-%m-%d')) DESC
LIMIT 2;