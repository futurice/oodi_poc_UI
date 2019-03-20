$(document).ready(function(){
  function home_signal() {
    $.ajax({
      url: '/back_home',
      success: function(data) {
        var redirect_home = function(){
          window.location.replace("/");
        };
        if (data == "-") {
          console.log("Home far away");
        }
        else if (data == "home") {
          console.log("Back home yay");
          setTimeout(redirect_home, 5000);
        }
      }

    });
    setTimeout(home_signal,2000);
  }
  home_signal();
});