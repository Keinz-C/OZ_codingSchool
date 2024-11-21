USE chapter17;

-- CREATE TABLE users2(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     password VARCHAR(4),
--     name VARCHAR(3),
--     gender ENUM('male', 'femail'),
--     email VARCHAR(15),
--     birthday CHAR(6),
--     age TINYINT,
--     company ENUM('samsung', 'LG', 'hyundai')
-- );

-- CREATE TABLE boards(
-- 	id INT PRIMARY KEY AUTO_INCREMENT,
--     title VARCHAR(5),
--     content VARCHAR(10),
--     likes INT CHECK(likes BETWEEN 1 AND 100),
--     img CHAR(1) DEFAULT 'c',
--     created DATE,
--     user_id INT,
--     FOREIGN KEY (user_id) REFERENCES users2(id)
-- );