$(document).ready(function(){
    $(".read-more").click(function(){
        $(this).next(".more-info").toggle('slow');
        // $(this).removeClass(".more-info");
    });

    $(".months").click(function(){
        $(this).nextAll(".month-events").toggle('slow');
    });

    $(".calendar").click(function () {
        $("#calendar").show();
    });

            addToCart: function() {
			    var cart_frm = jQuery('.product-description').find('.cart-form');
                cart_frm.on("submit", function () {
                    var formData = jQuery(this).serializeArray(),
                        selectedSize = formData[0].value,
                        errorMessage = jQuery('.error-message'),
                        successMessage = jQuery('.success-message');
                    jQuery.ajax({
                        type: cart_frm.attr('method'),
                        url: cart_frm.attr('action'),
                        data: formData,
                        success: function(data) {
                            // insert selected size into success message html
                            jQuery('.selected-size').text(selectedSize);
                            // hide error message and show success message
                            if(errorMessage.is(":visible")){
                                errorMessage.hide();
                            }
                            successMessage.show();
                            // update price in shopping bag
                            jQuery('.price--total').text('£'+data.total_price);
                        },
                        error: function(data, error) {
                            console.log(error);
                            // add error message to html
                            errorMessage.find('span').html(selectedSize + " size is no more available");
                            // hide success message and show error message
                            if(successMessage.is(":visible")){
                                successMessage.hide();
                            }
                            errorMessage.show();
                        }
                    });
                    return false;
                });
            },    

});