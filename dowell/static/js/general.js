$( document ).ready(function() {

  function endEdit(e) {
      defaultText = event.text;
      var input = $(e.target),
          label = input && input.prev();

      label.text(input.val() === '' ? defaultText : input.val());
      input.hide();
      label.show();
  }


  $("#btn_add").click(function () {
    $("#task_tags").append('<div class="ui card" style="max-width: 200px; max-height: 300px; margin: 2px 3px; float: left;"><div class="content"><label class="pull-left">Add Task Heading</label><input class="clickedit" type="text" /><div class="clearfix"></div></div><div class="content"><label class="pull-left">Add Task Description</label><input class="clickedit" type="text" /><div class="clearfix"></div></div></div>');
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
  });

  /*
  function submitForm() {
        var formData = {
            field1: getFieldValue('someId')
        };
  
      $.ajax({ type: 'GET', url: '/personal', data: formData, success: onFormSubmitted });
  }
*/


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

