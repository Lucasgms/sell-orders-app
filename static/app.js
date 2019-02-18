(function ($) {
    "use strict";

    $("select[name='product']").on("change", function () {
        let productId = $(this).val();
        $("#amount").attr("disabled", true);
        $.ajax({
            method: 'get',
            url: '/product/' + productId,
            success: function (data) {
                setItemAmount(data.multiplier);
                setItemPriceSugestion(data.unit_price)
            }
        })
    });

    $("input[name='amount']").on("focusout", function() {
        const amount = $(this).val();
        const multiplier = $(this).data('multiplier');
        const module = amount % multiplier;

        if(module != 0) {
            $(this).val(amount - module);
        }
    });

    $("form[action='/order/new']").before("submit", function(e) {
        event.preventDefault();
       console.log('ta querendo enviar');
    });

    function setItemAmount(multiplier) {
        const $amountInput = $("#amount");
        const $amountAddon = $("#amount-addon");
        const amountValue = $amountInput.val() || null;

        console.log(amountValue);
        if (amountValue) {
            if (amountValue < multiplier || (amountValue % multiplier != 0)) {
                $amountInput.val(multiplier);
            }
        }

        $amountAddon.html("Multiplicador: " + multiplier);
        $amountInput.data("multiplier", multiplier)
        $amountInput.attr({"min": multiplier, "disabled": false });
    }

    function setItemPriceSugestion(price) {
        const $priceInput = $("#price");
        const priceValue = $priceInput.val() || null;
        if(!priceValue) {
            $priceInput.val(price);
            $priceInput.attr("disabled", false);
        }
    }

})(jQuery)