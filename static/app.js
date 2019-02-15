(function($){
    "use strict";

    $("select[name='product']").on("change", function() {
        let productId = $(this).val();
        $.ajax({
            method: 'get',
            url: '/product/' + productId,
            success: function(data) {
                console.log(data)
            }
        })
    });
})(jQuery)