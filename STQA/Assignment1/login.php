<?php
$username = $_GET["username"];
$password = $_GET["password"];

if ($username == "abc" && $password == "abc") {
    echo "Login Successful...!";
} else {
    echo "Authentication failed...!";
}
?>
