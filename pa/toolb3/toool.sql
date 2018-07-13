CREATE TABLE users(
id INT NOT NULL AUTO_INCREMENT PRIMARY KEY ,
username VARCHAR(200),
name VARCHAR(200),
sex VARCHAR(200),
partment VARCHAR(200),
age INT ,
instr VARCHAR(200),
mail VARCHAR(200),
address VARCHAR(200),
code VARCHAR(200),
mobile VARCHAR(200),
phone VARCHAR(200),
station VARCHAR(200),
province VARCHAR(200),
city VARCHAR(200),
expl VARCHAR(200)
)
COLLATE='utf8_general_ci'
ENGINE=MyISAM
AUTO_INCREMENT=1;

INSERT INTO users(username, name, sex, partment, age, instr, mail, address, code, mobile, phone, station, province, city, expl)
VALUES ('默认值','默认b值','女','默认值',22,'默认值','默认值','默认值','默认值','默认值','默认值','默认值','默认值','默认值','默认值')