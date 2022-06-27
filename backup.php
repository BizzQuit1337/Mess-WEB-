<?php
    //config
    $config = array(

        "db_host"       => "127.0.0.1",
        "db_login"      => "root",
        "db_passwd" => "",
        "db_name" => "user_details"
    );

    //connecting to database
    $conn = mysqli_connect($config['db_host'],$config['db_login'],$config['db_passwd'],$config['db_name']);
    if(mysqli_connect_errno()) {
        printf("Boohoo. Connect failed: %s\n", mysqli_connect_error());
        exit();
    }

    echo 'connection succefull!!!!!'.'<br>';

    $name = $_POST['username'];
    $pass_plain = $_POST['password'];
    $pass = password_hash('$pass_plain', PASSWORD_DEFAULT);

    echo "you typed: " .$name."  ".$pass_plain.'<br>';


    $tables = "SELECT * FROM users";
    $result = mysqli_query($conn, $tables);

    while($row = mysqli_fetch_array($result)){
        if($row["passwords"] === $pass_plain){
            echo 'seacrit found'.'<br>';

        }
        break;
    }

    while($row2 = mysqli_fetch_array($result)){
        if($row2["usernames"] === $name){
            echo 'user found'.'<br>';

        }
        break;
    }

?>