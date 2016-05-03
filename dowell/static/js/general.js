

$( document ).ready(function() {

  var add_card = function () {
    $("#task_tags").append('<div class="ui card" style="max-width: 200px; max-height: 250px; margin: 2px 3px; float: left;"><div class="content"><label id="head2" class="pull-left header">Add Task Heading</label></div><div class="content"><label id="desc2" class="pull-left">Add Task Description</label></div><div class="content"><label id="date2" class="pull-left" style="margin-right: 50px;">Date</label><label id="time2" class="pull-left">Time</label></div></div>');

    $('.ui.modal')
      .modal('hide')
    ;

    var defaultText = "";
    $('.clickedit').hide()
      .focusout(endEdit)
      .keyup(function (e) {
        if ((e.which && e.which == 13) || (e.keyCode && e.keyCode == 13)) {
            endEdit(e);
            return false;
        } else {
            return true;
        }
    })
    .prev().click(function () {
        $(this).hide();
        $(this).next().show().focus();
    });
  };

  $( '.ui.form' )
    .form({
      username: {
        identifier : 'username',
        rules: [
          {  
            type   : 'empty',
            prompt : 'Please enter a username'
          }
        ]
      },
      email: {
        identifier : 'email',
        rules: [
          {
            type   : 'email',
            prompt : 'Please enter a valid email addres'
          }
        ]
      },
      password: {
        identifier : 'password',
        rules: [
          {
            type   : 'empty',
            prompt : 'Please enter a password'
          },
          {
            type   : 'length[2]',
            prompt : 'Your password must be at least 2 characters'
          }
        ]
      },
      passwordConfirm: {
        identifier : 'confirm-password',
        rules: [
          {
            type   : 'empty',
            prompt : 'Please confirm your password'
          },
          {
            type   : 'match[password]',
            prompt : 'Password doesn\'t match'
          }
        ]
      }
  });



  function endEdit(e) {
      defaultText = event.text;
      var input = $(e.target),
          label = input && input.prev();

      label.text(input.val() === '' ? defaultText : input.val());
      input.hide();
      label.show();
  }

  $(function() {
    $( "#datepicker" ).datepicker({ minDate: 0});
  });

  $(function() {
      $('#durationExample').timepicker({
          'minTime': new Date(),
          'maxTime': '12:00am'
      });
  });
  // Hide Sign Up side on initialization
  $( '.inactive' ).hide();
  $( '.mini.button.signup' ).click(function() {
    // Hide Sign In and show Sign Up side with slide down effect
    $( '.ui.segment.signin' )
      .hide()
      .end()
    .find( '.ui.segment.signup' )
      .slideDown();
  }); 
  $( '.mini.button.signin' ).click(function() {
    // Hide Sign Up and show Sign In side with slide down effect
    $( '.ui.segment.signup' )
      .hide()
      .end()
    .find( '.ui.segment.signin' )
      .slideDown();
  });


document.getElementById('btn_save').onclick = function validate_event(){
  event_head = document.getElementById('head1').value;
  event_desc = document.getElementById('desc1').value;
  event_date = document.getElementById('datepicker').value;
  event_time = document.getElementById('durationExample').value;
  if(event_head == "" || event_desc == "" || event_date == "" || event_time == ""){
    //show warning
    $('.hide_label').show();
    document.getElementById('errMessage').innerHTML = "All Fields Are Required.";
  }else{
    //run button add command
    add_card();
    document.getElementById('head2').innerHTML = event_head;
    document.getElementById('desc2').innerHTML = event_desc;
    document.getElementById('time2').innerHTML = event_time;
    document.getElementById('date2').innerHTML = event_date;
  }
}
});
 

