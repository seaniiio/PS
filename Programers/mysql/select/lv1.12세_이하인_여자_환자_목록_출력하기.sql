SELECT PT_NAME, PT_NO, GEND_CD, AGE, IFNULL(TLNO, 'NONE') AS TLNO
FROM PATIENT
WHERE GEND_CD = 'W' AND AGE <= 12
ORDER BY AGE DESC, PT_NAME ASC;

/* 
null인 경우 NONE으로 출력해야 하는 조건이 있으므로,ifnull()을 사용한다.
ifnull(컬럼, null일때 바꾸고 싶은 값)
*/