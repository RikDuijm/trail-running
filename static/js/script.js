$(document).ready(function(){
    $(".read-more").click(function(){
        $(this).next(".more-info").slideToggle("slow");
        // $(this).removeClass(".more-info");
    });

    $(".months").click(function(){
        $(this).nextAll(".month-events").slideToggle('slow');
    });

    $(".calendar").click(function () {
        $("#calendar").show();
    });

});