SELECT A.EMP_NO, A.EMP_NAME, (CASE WHEN B.AVG_SCORE >= 96 THEN 'S'
                                WHEN B.AVG_SCORE >= 90 THEN 'A'
                                WHEN B.AVG_SCORE >= 80 THEN 'B'
                              ELSE 'C'
                              END) AS GRADE,
                              (CASE WHEN B.AVG_SCORE >= 96 THEN A.SAL * 0.2
                                WHEN B.AVG_SCORE >= 90 THEN A.SAL * 0.15
                                WHEN B.AVG_SCORE >= 80 THEN A.SAL * 0.1
                              ELSE 0
                              END) AS BONUS
FROM HR_EMPLOYEES AS A JOIN (SELECT EMP_NO, AVG(SCORE) AS AVG_SCORE
                             FROM HR_GRADE
                             GROUP BY EMP_NO) AS B ON A.EMP_NO = B.EMP_NO
ORDER BY A.EMP_NO