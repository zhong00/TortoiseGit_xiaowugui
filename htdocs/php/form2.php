<?php 
if($_SERVER['REQUEST_METHOD']=="GET"){
    get();
} elseif($_SERVER['REQUEST_METHOD']=="POST"){
    add();
}

function get(){
    $con = mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
    if(!$con)
    {
        die('Could not connect:'.mysql_error());
    }
    mysql_select_db("bdm257820613_db",$con);
    $sql = "SELECT * FROM Persons WHERE personID=1;";
    $result = mysql_query($sql);
    $row = mysql_fetch_array($result);
    if(!mysql_query($sql,$con)){
        die('Error:'.mysql_error());
    }
    echo "<table border='1'>
    <tr>
    <th>Firstname</th>
    <th>Lastname</th>
    </tr>
    <tr>
    <td>".$row['FirstName']."</td>
    <td></td>
    </tr>
    </table>";    // mysql_close($con);
    mysql_close($con);
    }
function add(){
    $con = mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
    if(!$con)
    {
        die('Could not connect:'.mysql_error());
    }
    mysql_select_db("bdm257820613_db",$con);
    $sql = "INSERT INTO Persons (FirstName,LastName) VALUES('$_POST[fname]','$_POST[lname]')";
    if(!mysql_query($sql,$con)){
        die('Error:'.mysql_error());
    }
    echo "$_POST[fname]"."保存成功";
    mysql_close($con);
}

?>