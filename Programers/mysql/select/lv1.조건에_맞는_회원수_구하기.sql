SELECT COUNT(*) AS USERS
FROM USER_INFO
WHERE YEAR(JOINED) = 2021
AND AGE BETWEEN 20 AND 29;

/* 전체 회원 수를 세기 위해 집계함수 count를 이용한다.count(*) */