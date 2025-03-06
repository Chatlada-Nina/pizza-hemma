/*
This code was learned from Boutique Ado project-CI Learning platform and modified as the project needed.
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#35724c',
        fontFamily: '"Chivo", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style: style});
card.mount('#card-element');


    // Handle realtime validation errors on the card element

card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span role="alert">
                <i class="fa-solid fa-xmark"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';        
    }
});


// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            var html = `
                <span role="alert">
                    <i class="fa-solid fa-xmark"></i>
                </span>
                <span>${result.error.message}</span>`;
            $(errorDiv).html(html);
            card.update({ 'disabled': false});
            $('#submit-button').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});


// Update delivery cost and grand total based on delivery method
function updateTotals() {
    const deliveryMethod = document.querySelector('select[name="delivery_method"]').value;
    const totalElement = document.getElementById('total');
    const deliveryCostElement = document.getElementById('delivery-cost');
    const grandTotalElement = document.getElementById('grand-total');
    const chargedAmountElement = document.getElementById('charged-amount');

    let total = parseFloat(totalElement.textContent);
    let deliveryCost = 0;
    
    if (deliveryMethod === 'delivery') {
        // Calculate delivery cost based on the conditions
        if (total < window.deliveryData.freeDeliveryThreshold) {
            deliveryCost = total * window.deliveryData.standardDeliveryPercentage / 100;
        } else {
            deliveryCost = 0;
        }
    }

    const grandTotal = total + deliveryCost;
    
    deliveryCostElement.textContent = deliveryCost.toFixed(2);
    grandTotalElement.textContent = grandTotal.toFixed(2);
    chargedAmountElement.textContent = grandTotal.toFixed(2) + 'sek';
}

document.querySelector('select[name="delivery_method"]').addEventListener('change', updateTotals);
document.addEventListener('DOMContentLoaded', updateTotals);