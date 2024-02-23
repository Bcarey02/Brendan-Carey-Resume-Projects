
#1- Write the SQL code that creates the tables and enforces Primary and foreign key constraints.
#Your SQL Code Goes Below:

use 310brendan; #Your database Schema Name instead
SET FOREIGN_KEY_CHECKS=0;

#a
DROP TABLE dept CASCADE;
Create TABLE dept (
#Rest of your code
dname varchar(64) PRIMARY KEY NOT NULL,
school varchar(64) NOT NULL
);

#b
DROP TABLE course CASCADE;
#The PK for Course is a Composite, it is made-up of (prefix, cnumber)
CREATE TABLE course(
#Rest of your code
prefix varchar(8) NOT NULL,
cnumber decimal(4,0) NOT NULL,
PRIMARY KEY(prefix, cnumber),
courseName varchar(32) NOT NULL,
deptName varchar(64),
foreign key(deptName) references dept(dname) on update cascade
);


#c
DROP TABLE courseSection CASCADE;
#(prefix, cnumber) is a FK that points to the dept PK
CREATE TABLE courseSection(
#Rest of your code
crn Decimal(6,0) not null,
prefix varchar(8),
cnumber decimal(4,0),
capacity DECIMAL(2,0),
semester VARCHAR(16),
year DECIMAL(4,0),
foreign key(prefix, cnumber) references course(prefix, cnumber) on update cascade
);

#
SET FOREIGN_KEY_CHECKS=1;

#2- Reverse Engineer your schema according to the guidelines in the word document
# and upload it to Moodle as a PNG
## File --> Export as PNG to save the diagram into a shape file with yourLnameFname.png

#3 Insert 3-Department Records into the dept table. 
## Your SQL Code Goes Below:
describe dept;
insert into dept values("Finance","Business");
insert into dept values("Accounting","Business");
insert into dept values("Engineering","Science");


select * from dept;

#4 Insert 6 Courses into the Course table; 
## make sure you assign them to different departments. 
## Your SQL Code Goes Below:
describe course;
delete from course where prefix="ACCT";
insert into course values("ENG",101,"Intro to Engineering","Engineering");
insert into course values("ENG",201,"Advanced Engineering","Engineering");
insert into course values("FIN",101,"Intro to Finance","Finance");
insert into course values("FIN",201,"Advanced Finance","Finance");
insert into course values("ACCT",101,"Financial Accounting","Accounting");
insert into course values("ACCT",201,"Managerial Accounting","Accounting");


select * from course;

#5 Insert 12 course-sections into the courseSection table across different years and semesters. 
## No more than 3 course sections for a given year and a given semester. 
## Your SQL Code Goes Below:
describe courseSection;
insert into courseSection values(32432,"ENG",101,50,"FALL","2023");
insert into courseSection values(75634,"ENG",201,32,"FALL","2023");
insert into courseSection values(98652,"FIN",101,32,"FALL","2023");
insert into courseSection values(76541,"ACCT",101,32,"SPRING","2023");
insert into courseSection values(94501,"ENG",101,50,"SPRING","2023");
insert into courseSection values(63681,"ENG",201,32,"SPRING","2023");
insert into courseSection values(38731,"FIN",101,32,"FALL","2022");
insert into courseSection values(17560,"ACCT",101,32,"FALL","2022");
insert into courseSection values(84565,"ENG",101,50,"FALL","2022");
insert into courseSection values(34552,"ENG",201,32,"SPRING","2022");
insert into courseSection values(16552,"FIN",101,40,"SPRING","2022");
insert into courseSection values(47219,"ACCT",101,32,"SPRING","2022");



select * from courseSection

