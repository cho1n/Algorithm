SELECT BOOK_ID, date_format(PUBLISHED_DATE, '%Y-%m-%d') as PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' and YEAR(PUBLISHED_DATE) = 2021
ORDER BY PUBLISHED_DATE;