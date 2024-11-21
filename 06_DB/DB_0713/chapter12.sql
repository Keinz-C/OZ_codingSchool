-- CREATE DATABASE testdatabase; 
-- USE testdatabase;
-- 파이썬과 같이 한 코드 안에 다양한 값을 넣을 땐 쉼표로 구분 지어야 한다.
-- CREATE TABLE users(
-- 	id INT AUTO_INCREMENT PRIMARY KEY,	-- id를 숫자로 만들 것이고(INT), 고유한 키라고 설정(PRIMARY KEY) / 유일성을 보장하고 검색 속도를 향상시키기 위해 사용
--     username VARCHAR(30) NOT NULL,	-- username에 null값(빈값)을 입력하지 못하게 하는 코드(NOT NULL)
--     email VARCHAR(100) UNIQUE,	-- VARCHAR(100)의 100은 100글자까지 입력 가능하다는 뜻 / UNIQUE는 유니크한 값이기 때문에 작성하는 코드
--     is_business VARCHAR(10) DEFAULT False,	-- 기본적으로 비즈니스 계정은 False값이고, 신청을 받아 통과되면 True 값을 반환 / False는 0으로 반
--     
--     age INT CHECK (age >= 10)	-- 더블체킹, 웹 프레임워크랑 DB에 데이터를 넣을때도 체크하도록 작성하는 코
--     );

USE testdatabase;

-- CREATE TABLE users(
-- 	user_id INT PRIMARY KEY,
--     name VARCHAR(20),
--     age INT
-- );

-- INSERT INTO users(user_id, name, age)
-- VALUES (1,'Alice', 25), 
--        (2, 'Bob', 23),
--        (3, 'Carolina', 29),
--        (4, 'Jack', 43),
--        (5, 'Hans', 17);

-- CREATE TABLE orders(
-- 	order_id INT PRIMARY KEY,
--     user_id INT,
--     order_date DATE
-- );

-- INSERT INTO orders(order_id, user_id, order_date)
-- VALUES (101, 1, '2024-01-01'),
-- 	   (102, 2, '2024-07-26'),
--        (103, 3, '2023-01-05'),
--        (104, 4, '2023-11-25'),
--        (105, 5, '2022-02-13');