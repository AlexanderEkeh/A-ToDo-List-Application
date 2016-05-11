$(document).ready(function() {

    var add_card = function (new_card) {$("#task_tags").append(new_card);

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



  function endEdit(e) {
      defaultText = event.text;
      var input = $(e.target),
          label = input && input.prev();

      label.text(input.val() === '' ? defaultText : input.val());
      input.hide();
      label.show();
  }

  $(function() {
    $( "#task_date" ).datepicker({ minDate: 0});
  });

  $(function() {
      $('#task_time').timepicker({
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

var add_element = function (event_head, event_desc, event_date, event_time, event_id){	
	
		a_card = '<div class="ui card" style="display:inline-block;max-width: 200px; margin: 2px 3px; float: left;"><div class="content overflow_header" style="height: 35px; font-size: 15px; font-weight: bold;"><label >' + event_head + '</label></div><div class="content overflow" style="height: 110px;font-size: 12px;"><label class="pull-left">' + event_desc + '</label></div><div class="content" style="height; 40px; font-size: 12px;"><label class="pull-left" style="float: left">'+ event_date +'</label><div class="ui dropdown" style="float: right;margin-left:20px;"><i class="options icon"></i><div class="menu"><div class="item" id="{{event_id}}">\
                        Edit\
                    	</div><div class="item">\
                        Add Reminder\
                    	</div><div class="item">\
                        ' + suggest + '\
                    	</div><div class="item">\
                        Remove\
                    	</div></div></div><label class="pull-left" style="float: right">'+ event_time +'</label></div></div>';

    add_card(a_card);
}

 $('.ui.dropdown').dropdown('hide');
});


//if(document.getElementById('btn_save')!=null)