SELECT A.BOOK_ID, B.AUTHOR_NAME, DATE_FORMAT(A.PUBLISHED_DATE,'%Y-%m-%d')
FROM BOOK AS A JOIN AUTHOR AS B ON A.AUTHOR_ID = B.AUTHOR_ID
WHERE A.CATEGORY = '경제'
ORDER BY A.PUBLISHED_DATE;
