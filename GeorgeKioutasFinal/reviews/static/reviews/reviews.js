$(document).ready(function(){
    $(".starbutton").click(function(e){
        e.preventDefault();

        // Get the review id and the selected star number from the clicked star
        var reviewId = $(this).data("catid");
        var stars = $(this).data("stars");

        $.ajax({
            type: "GET",
            url: "/rate-review/",
            data: {
                review_id: reviewId,
                stars: stars
            },
            success: function(data) {
                $("#stars" + reviewId).text(data);
            }
        });
    });
});
