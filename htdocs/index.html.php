<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>demo1</title>
    <link rel="stylesheet" href="demo1.css" type="text/css">
    <script type="text/javascript" src="jquery-3.2.1.min.js"></script>
    <style>
    div.comment {
        color:#000;
        border:0;
    }
    </style>
</head>
<body>
    <h2>目录</h2>
    <div>
    <dl><dt>练习</dt>
        <dd>1)<a href="demo2.html">全选全不选</dd>
        <dd>2)<a href="demo3.html">计算器</dd>
        <dd>3)<a href="demo4.html">遮罩层</dd>
        <dd>4)<a href="handsomeboys.html">我的蓝盆友</dd>
        <dd>5)<a href="demo5.html">demo5</a></dd>
        <dd>6)<a href="demo6.html">demo6</a></dd>
        <dd>6)<a href="nianli.html">日历</a></dd>
    </dl>
    <dl><dt>网页</dt>
        <dd>1)<a href="/weibo/weibo.html">微博首页</a></dd>
        <dd>2)<a href="/jd/jd.html">京东首页</a></dd>
    </dl>
    <dl><dt>更多</dt>
        <dd>1)<a href="#">敬请期待</a></dd>
        <dd>2)<a href="#">敬请期待</a></dd>
    </dl>   
    </div>
    <hr />
    <div class="comment">
        <h3>留言区</h3>
        <textarea rows="3" cols="50" id="content"></textarea><br />
        署名<input id="name" type="text">
        <button id="insert">提交</button>
        <p id="commentarea">
            <?php 
                echo"test";
                // $con=mysql_connect("bdm257820613.my3w.com","bdm257820613","q1w2e3r4t5");
                // mysql_select_db("bdm257820613_db",$con);
                // $sql = "SELECT * FROM comment;"
                // $result = mysql_query($sql,$con);
                // while($row = mysql_fetch_array($result))
                // {
                //     echo $row['content']."By".$row['name']."On".$row["date"];
                    
                // }
                // mysql_close($con);
            ?>
        </p>
    </div>
    
    
    
    <script>
    $("dt").click(function(){
        $(this).parent().siblings().find("dt").css("background-color","blue");
        $(this).parent().siblings().find("dd").hide();
        $(this).parent().find("dd").toggle();
        if($(this).next().is(":visible")){
            $(this).css("background-color","#42DC59");
        } else {
            $(this).css("background-color","blue");
        }
    });
    $("#insert").click(function(){
        var mydate = new Date();
        $.ajax({
            type:"POST",
            url:"php/index.php",
            data:{
                content:$("#content").val(),
                name:$("#name").val(),
                date:mydate.getMonth()+1+"/"+mydate.getDate()
            },
            // dataType:"json",
            success:function(data){
                $("#commentarea").html(data);
            },
            error:function(jqXHR){
                alert("发生错误:"+jqXHR.status);
            }
        });
    });
    </script>
</body>
</html>