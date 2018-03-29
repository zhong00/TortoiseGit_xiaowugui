<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
    if($_SERVER['REQUEST_METHOD']=="GET"){
        get();
    } elseif($_SERVER['REQUEST_METHOD']=="POST"){
        post();
    }
    function post(){
        $con=mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
        mysql_select_db("bdm257820613_db",$con);
        mysql_query("set character set 'utf8'");
        mysql_query("set names 'utf8'");
        $sql= "INSERT INTO comment(content,name,date) VALUES('$_POST[content]','$_POST[name]','$_POST[date]');";
        if(mysql_query($sql,$con)){
            $sql = "SELECT * FROM comment ORDER BY id DESC LIMIT 15; ";
            $result = mysql_query($sql,$con);
            $text="[";
            while($row = mysql_fetch_array($result))
            {
                $text.= '{"name":"' .$row['name'].'","content":"'.$row['content'].'","date":"'.$row['date'].'"},';
            }
            $text = substr($text, 0,strlen($text)-1);
            $text .="]";
            echo $text;
        }
        mysql_close($con);
    }
    function get(){
        $con=mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
        mysql_select_db("bdm257820613_db",$con);
        mysql_query("set names 'utf8'");
        $sql = "SELECT * FROM comment ORDER BY id DESC LIMIT 15; ";
        $result = mysql_query($sql,$con);
        $text="[";
        while($row = mysql_fetch_array($result))
        {
            $text.= '{"name":"' .$row['name'].'","content":"'.$row['content'].'","date":"'.$row['date'].'"},';
        }
        $text = substr($text, 0,strlen($text)-1);
        $text .= "]";
        echo $text;
        mysql_close($con);
    }
?>