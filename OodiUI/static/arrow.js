$(document).ready(function(){
  function arrow_signal() {
    $.ajax({
      url: '/get_arrow',
      success: function(data) {
        if (data == "+") {
          console.log("you will be directed to right");

        }
        if (data == "-") {
          console.log("empty file meh");
        }
        if (data == "l") {
          console.log("look to your left");
        }
        if (data == "rl") {
          console.log("look at both sides");
        }
      }

    });
    setTimeout(arrow_signal,10000);
  }
  arrow_signal();

    /*$.get('/get_arrow', (data, err) => {
      if (err) {
        console.log("no arrow found");
      } else {
        console.log("found an arrow");// set image with data
      }
    });
    setTimeout(arrow_signal, 5000);
  }
  arrow_signal();*/
});

  /*function arrow_signal() {
    // Logic first without delay
    $.ajax({
      url:'/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt',
      error: function(){
        console.log("file does not exist");
      },
      success: function(){
        $.get('/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt', function(data){
            $.post("/get_arrow", {"arrow_data": data})
          });
        }
      });

    // Set a new run in two seconds
    setTimeout(arrow_signal, 2000);
  }

  // Start running
  arrow_signal();

});*/
