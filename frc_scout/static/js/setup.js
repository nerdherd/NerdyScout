$(document).ready(function()  {
  //Send new info to server
  $('form').submit(function() {
    form = $(this)
    $.ajax({
      type: 'GET',
      url: $(this).attr('action'),
      data: $(this).serialize(),
      success: function(data) {
        //Toast info
        Materialize.toast(data.message, data.message.length * 150);
      }
    });
    return false;
  });
});
