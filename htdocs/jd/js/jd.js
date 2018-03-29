$(document).ready(function(){
    var $sub = $("#sub");
    var sub_id;
    $(".leftside>ul li").on("mouseover",function(){
        $sub.addClass("none");
        $("#sub .sub_content").addClass("none");
        sub_id = $(this).attr("data-id");
        if($("#"+sub_id)){
            $("#"+sub_id).removeClass("none");
            $sub.removeClass("none");
        }
    })
    $(".leftside>ul").on("mouseout",function(){
        $sub.addClass("none");
        $("#sub .sub_content").addClass("none");
    })
    $(".rightside .notice .tab li:nth-child(1) a").on("mouseover",function(){
        $(".rightside .notice .content ul:nth-child(1)").removeClass("none");
        $(".rightside .notice .content ul:nth-child(2)").addClass("none");
        $(this).parent().css("border-bottom","solid 1px red");
        $(this).parent().next().css("border-bottom","none");
    });
    $(".rightside .notice .tab li:nth-child(2) a").on("mouseover",function(){
        $(".rightside .notice .content ul:nth-child(2)").removeClass("none");
        $(".rightside .notice .content ul:nth-child(1)").addClass("none");
        $(this).parent().css("border-bottom","solid 1px red");
        $(this).parent().prev().css("border-bottom","none");
    });
    $(".search .search-input input").on("click",function(){
        $(this).val(" ");
        $(this).css({"border":"1px solid red","outline":"none"});

    });
});
