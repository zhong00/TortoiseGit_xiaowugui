<html>
    <body>
        Welcome <?php echo $_GET["fname"];?>
    </body>
</html>
<?php 
$con = mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
if(!$con)
{
    die('Could not connect:'.mysql_error());
}
// if(mysql_query("CREATE DATABASE my_db",$con))
// {
//     echo "DATABASE CREATED";
// }
// else {
//     echo "Error creating database:".mysql_error();
// }
mysql_select_db("bdm257820613_db",$con);
// $sql = "CREATE TABLE Persons(
//     personID int NOT NULL AUTO_INCREMENT,
//     PRIMARY KEY(personID),
//     FirstName varchar(15),
//     LastName varchar(15),
//     Age int
//     )";
// mysql_query($sql,$con);
// $age = intval($_POST["age"]);
$sql = "INSERT INTO Persons (FirstName,LastName) VALUES('$_POST[fname]','$_POST[lname]')";
if(!mysql_query($sql,$con)){
    die('Error:'.mysql_error());
}
mysql_close($con);
?>