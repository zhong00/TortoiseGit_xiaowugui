<?php
header('Access-Control-Allow-Origin:*');
header('Access-Control-Allow-Methods:POST,GET');
header('Access-Control-Allow-Credentials:true');
header("Content-Type: application/json;charset=utf-8");
    if($_SERVER['REQUEST_METHOD']=="GET"){
        get();
    } 
    
    function get(){
        $con=mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
        mysql_select_db("bdm257820613_db",$con);
        mysql_query("set names 'utf8'");
        $sql = "SELECT * FROM movie ORDER BY id ; ";
        $result = mysql_query($sql,$con);
        $text="[";
        while($row = mysql_fetch_array($result))
        {
            $text.= '{"title":"' .$row['title'].'","region":"'.$row['region'].'","director":"'.$row['director'].
            '","actors":"'.$row['actors'].'","rate":"'.$row['rate'].'"},';
        }
        // $text = substr($text, 0,strlen($text)-1);
        $text .= "]";
        echo $text;
        mysql_close($con);
    }
?>