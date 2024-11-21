-- CREATE DATABASE blogtest;

USE blogtest;

CREATE TABLE blog_posts(
	id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    content TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,	-- 생성이 되었을 시 현재 시간에 맞춰 데이터가 들어가도록 
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP	-- UPDATE UTC시간에 맞춰 데이터가 덮어씌워지도록
);