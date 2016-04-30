$(document).ready(function(){
      $("#btn_add").click(function () {
          $("#task_tags").append('<div class="ui card my_card"><div class="content"><label class="pull-left">Add Task Heading</label><input class="clickedit" type="text" /><div class="clearfix"></div></div><div class="content"><label class="pull-left">Add Task Description</label><input class="clickedit" type="text" /><div class="clearfix"></div></div></div>');
        });
});

$("#btn_add").click(function(){
  $.getScript('../static/js/general.js', function() {
  });
});
/*https://git.heroku.com/obscure-river-93607.git*/

var defaultText = "";

function endEdit(e) {
    defaultText = event.text;
    var input = $(e.target),
        label = input && input.prev();

    label.text(input.val() === '' ? defaultText : input.val());
    input.hide();
    label.show();
}

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


/*
$(document).ready(function(){
      $("#btnAddAddress").click(function () {
      $("#container").append('<div class="address"><div class="input-reg rb-item input-group"><span class="input-group-addon">Address </span><input type="text" class="form-control" placeholder="Insert text here"></div><div align="center"><iframe class="map-img" width="100%" height="400" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://maps.google.com/maps?hl=en&amp;ie=UTF8&amp;ll=37.0625,-95.677068&amp;spn=56.506174,79.013672&amp;t=m&amp;z=4&amp;output=embed"></iframe></div></div>');
    });
});
*/