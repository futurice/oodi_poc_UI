$(document).ready(function(){

  function arrow_signal() {
    // Logic first without delay
    $.ajax({
      url:'/Users/nulm/Desktop/OodiMir/OodiUI/static/direction.txt',
      type:'HEAD',
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

});
