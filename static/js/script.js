$(document).ready(function(){
    $(".read-more").click(function(){
        $(this).next(".more-info").toggle('slow');
        // $(this).removeClass(".more-info");
    });

    $(".months").click(function(){
        $(this).nextAll(".month-events").toggle('slow');
    });


});