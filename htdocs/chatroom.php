<?php
// header("Content-Type: text/json;charset=utf-8");
// header("Cache-Control: no-cache, must-revalidate");
// header("Content-Type: text/plain;charset=utf-8");
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true'); 
header("Content-Type: application/json;charset=utf-8"); 

function saveContent(){
    $con = mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
    if(!$con){
        die("Could not connect:".mysql_error());
    }
    mysql_select_db("bdm257820613_db",$con);
    mysql_query("set character set 'utf8'");
    mysql_query("set names 'utf8'");
    $sql = "INSERT INTO message(name,content) VALUES('$_POST[name]','$_POST[content]')";
    if(!mysql_query($sql,$con)){
        die('Error:'.mysql_error());
    }else {
        $sql = "SELECT * FROM message ORDER BY id DESC LIMIT 10";
        $result =  mysql_query($sql,$con);
        $text = "[";
        while($row = mysql_fetch_array($result))
        {
            $text = $text.'{"name":"'.$row['name'].'","content":"'.$row['content'].'"},';
        }
        $text=substr($text,0,$text.strlen($text)-1);
        $text=$text."]";
        echo $text;
        mysql_close($con);
    }
}
function getContent(){
    $con = mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
    if(!$con){
        die("Could not connect:".mysql_error());
    }
    mysql_select_db("bdm257820613_db",$con);
    mysql_query("set character set 'utf8'");
    mysql_query("set names 'utf8'");
    $sql = "SELECT * FROM message ORDER BY id DESC LIMIT 10";
    $result =  mysql_query($sql,$con);
    $text = "[";
    while($row = mysql_fetch_array($result))
    {
        $text = $text.'{"name":"'.$row['name'].'","content":"'.$row['content'].'"},';
    }
    $text=substr($text,0,$text.strlen($text)-1);
    $text=$text."]";
    echo $text;
    mysql_close($con);
}
if($_SERVER['REQUEST_METHOD']=="GET"){
    getContent();
} elseif($_SERVER['REQUEST_METHOD']=="POST"){
    saveContent();
}

?>