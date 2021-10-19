
var yoco = new window.YocoSDK({
    publicKey: 'pk_test_ed3c54a6gOol69qa7f45',
  });
  

  window.onload = function myYoco(money) {

    yoco.showPopup({
      amountInCents: money,
      currency: 'ZAR',
      name: 'MY STORE',
      description: 'Awesome description',
      callback: function (result) {
        // This function returns a token that your server can use to capture a payment
        if (result.error) {
          const errorMessage = result.error.message;
          alert("error occured: " + errorMessage);
        } else {
            alert("card successfully tokenised: " + result.id);
            fetch('/pay', {
                    method: 'post',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ token: result.id })
                }).then(res => res.json())
                   .then(data => {
                        if(data.errorCode){
                            alert(data.displayMessage);
                        }
                        else{
                            alert(data.status);
                        }
                    }).catch(error => {
                        alert(error.message);
                    })
        }

      }
    })
  };