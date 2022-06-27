<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="index.php"  method='post'>
        Username: <input type="text" name="username"><br>
        Password: <input type="password" name="password"><br>
                Confirm password: <input type="password" name="pass_ver"><br>
        <p>
            Screen will return to login page once account created.
        </p>
                <br>
                <input type="submit" onclick=save()>
    </form>
    </script>
</body>
</html>
[root@bladebox brython-runner]# cat index.php
<?php

        error_reporting(E_ALL);
        ini_set('display_errors', 1);

        //config
    $config = array(

        "db_host"       => "127.0.0.1",
        "db_login"      => "root",
        "db_passwd" => ""
    );

    //connecting to database
    $conn = mysqli_connect($config['db_host'],$config['db_login'],$config['db_passwd']);
    if(mysqli_connect_errno()) {
        printf("Boohoo. Connect failed: %s\n", mysqli_connect_error());
        exit();
    }

    echo 'Connection successfull!   ';

    //create database
    $sql = "CREATE DATABASE user_details";
    if($conn->query($sql) === TRUE) {
        echo '   database created!   ';
    } else {
        echo '   failed to create database   ';
    }

        //selecting the database
        $select = mysqli_select_db($conn, 'user_details');
        if(!$select) {
                echo '   no database selected   ';
        }

        //creating the tables
        $table = "CREATE TABLE users (usernames VARCHAR(50) NOT NULL UNIQUE, passwords VARCHAR50) NOT NULL, id INT AUTO_INCREMENT PRIMARY KEY)";
    if($conn->query($table) === TRUE){
        echo '   table created!   ';
    } else {
        echo '   failed to create table   ';
    }

        $names = $_POST['username'];
        $pass_plain = $_POST['password'];
        $password_verification = $_POST['pass_ver'];

        if($pass_plain !== $password_verification){
                header("Location: http://192.168.1.7/brython-runner/register.html");
                exit();
        }


        $pass = md5($pass_plain);
        $structure  = "./USER_FOLDER/".$names."";

        $sql_query = "INSERT INTO users (usernames, passwords) VALUES ('$names', '$pass')";
    if($conn->query($sql_query) === TRUE) {
        echo '  New record added';
                if (!mkdir($structure, 0777, true)) {
                die('Failed to create directories...');
                }
                header("Location: http://192.168.1.7/");
                exit();
    } else {
                echo '  didnt work loser';
                header("Location: http://192.168.1.7/brython-runner/register.html");
                exit();
    }

        $conn->close();
?>