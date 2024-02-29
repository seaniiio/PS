WITH USER_2021_INFO AS (
    SELECT USER_ID, JOINED
     FROM USER_INFO
     WHERE YEAR(JOINED) = 2021
)

SELECT YEAR(A.SALES_DATE) AS YEAR, MONTH(A.SALES_DATE) AS MONTH, COUNT(DISTINCT A.USER_ID) AS PUCHASED_USERS, ROUND(COUNT(DISTINCT A.USER_ID) / (SELECT COUNT(*) FROM USER_2021_INFO), 1) AS PUCHASED_RATIO
FROM ONLINE_SALE AS A JOIN USER_2021_INFO AS B ON A.USER_ID = B.USER_ID
GROUP BY YEAR, MONTH
ORDER BY YEAR, MONTH;