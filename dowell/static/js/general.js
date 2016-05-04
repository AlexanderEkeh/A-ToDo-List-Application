$( document ).ready(function() {
var count = 0;
  var add_card = function (new_card) {
    $("#task_tags").append(new_card);

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


  $("#btn_task").click(function(){
    $('.ui.modal').modal('show');
    $('.hide_label').hide();
    document.getElementById('head1').value = "";
    document.getElementById('desc1').value = "";
    document.getElementById('datepicker').value = "";
    document.getElementById('durationExample').value = "";
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


    document.getElementById('btn_save').onclick(function validate_event(){
      var a_card = "";
      count += 1
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
        a_card = '<div class="ui card" style="max-width: 200px; max-height: 250px; margin: 2px 3px; float: left;"><div class="content"><label class="pull-left header">' + event_head + '</label></div><div class="content"><label class="pull-left">' + event_desc + '</label></div><div class="content"><label class="pull-left" style="margin-right: 50px;">' + event_date + '</label><label class="pull-left">' + event_time + '</label></div></div>';

        add_card(a_card);
      }
    }
);

);