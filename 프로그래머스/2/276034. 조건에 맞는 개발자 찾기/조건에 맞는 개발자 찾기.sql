SELECT DISTINCT A.ID, A.EMAIL, A.FIRST_NAME, A.LAST_NAME
FROM DEVELOPERS A, SKILLCODES B
WHERE (A.SKILL_CODE & B.CODE) = B.CODE AND (B.NAME = 'C#' or B.NAME = 'Python')
ORDER BY A.ID ASC;