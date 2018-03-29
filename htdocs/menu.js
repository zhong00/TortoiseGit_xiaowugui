/*
侧边fix的菜单
 */
$(document).ready(function(){
    $("body").append("<div class='side-menu'></div>");
    $(".side-menu").append("<ul><li><a href='#web_page'>网页<img src='' alt='' /></a></li><li><a href='#phone_page'>移动端<img src='' alt='' /></a></li><li><a href='#js'>练习<img src='' alt='' /></a></li></ul>")
    .css({"position":"fixed","left":0,"top":"50%","background-color":"#34495e","padding":"10px","border-top-right-radius":"10px","border-bottom-right-radius":"10px","border":"1px solid #34495e"});
    $(".side-menu a").click(function(){
        var href = $(this).attr("href");
        $("#tab-header [href='"+href+"']").tab('show');
        return false;
    })
});