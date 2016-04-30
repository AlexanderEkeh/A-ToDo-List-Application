function endEdit(e) {
    defaultText = event.text;
    var input = $(e.target),
        label = input && input.prev();

    label.text(input.val() === '' ? defaultText : input.val());
    input.hide();
    label.show();
}
      $("#btn_add").click(function () {
          $("#task_tags").append('<div class="ui card" style="max-width: 200px; margin: 2px 3px; float: left;"><div class="content"><label class="pull-left">Add Task Heading</label><input class="clickedit" type="text" /><div class="clearfix"></div></div><div class="content"><label class="pull-left">Add Task Description</label><input class="clickedit" type="text" /><div class="clearfix"></div></div></div>');
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

