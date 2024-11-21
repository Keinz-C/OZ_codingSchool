USE testdatabase;

-- SELECT DISTINCT age FROM users;		-- 쿼리를 활용하여 데이터 분석을 할 때 많이 사용함. 유일한 값만 불러오는 쿼리문
-- SELECT age, age * 100 as age100 from users;		-- 원하는 컬럼의 이름을 바꾸고 싶을 때는 as 명령어를 사용한다.

-- SELECT * FROM users ORDER BY age DESC;		-- DESC 내림차순 ASC는 오름차순

-- SELECT * FROM users WHERE age >= 25;	-- where조건문은 자주 사용하니 공부하자.
-- SELECT * FROM users WHERE username = 'david' AND	-- or, and로 조건에 맞는 것들을 찾을수 있음
-- age = 25

-- SELECT * FROM users WHERE NOT age = 25

-- SELECT * FROM users LIMIT 5, 5;
-- WHERE age BETWEEN 26 AND 50 LIMIT 5, 5;

-- SELECT age, COUNT(*) AS age_count FROM users GROUP BY age;

-- SELECT
	-- username,
    -- age,
    -- CASE WHEN age >= 30 THEN '성인' ELSE '미성년자' END AS age_group	-- 이 경우에 데이터를 저장하는 것이 아니라서 SELCET FORM을 할 땐 보이지 않는다.
-- FROM users;

-- SELECT
-- 	username,
-- 		age,
-- 		ROW_NUMBER() OVER (ORDER BY age DESC) AS 'rank'		-- ROW_NUMBER()는 순서에 따라서 등급을 부여하는 쿼리문이다.
-- FROM users;

-- CHPATER 15 START

-- SET SQL_SAFE_UPDATES = 0; 	-- SQL에서 0은 False이다.

-- UPDATE users
-- SET username = 'SENIOR'
-- WHERE age >= 25;
-- SELECT ROW_COUNT();		-- 업데이트된 레코드 수를 반환하는 문

-- UPDATE users
-- SET username = CASE
-- 	WHEN age >= 60 THEN 'senior_data'		-- 업데이트 쿼리는 조심해서 사용해야 한다. 고유값을 변경했기 때문.
--     ELSE 'YOUNG'
-- END;

-- UPDATE users
-- SET username = 'TOP5_PEOPLE'
-- WHERE age = 25
-- LIMIT 3;		-- 해당 쿼리문은 조건의 제약이 심함.(사용하는데 불편함이 많음)

-- UPDATE users
-- SET email = CONCAT(email, '_new')
-- WHERE email REGEXP '@gmail\.com$';	-- REGEXP를 사용한 정규 표현식 업데이트 쿼리

-- chpater 17 시작

-- DELETE FROM users WHERE username = 'YOUNG' LIMIT 3;

-- DELETE FROM users WHERE age > 65 RETURNING *;	-- mysql에서는 지원하지 않고, Nosql에서 지원함.

SELECT * FROM users;