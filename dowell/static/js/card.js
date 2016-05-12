var add_card = function (new_card) {$("#task_tags").append(new_card);}

    var pg_title = document.title, suggest = "";
    if (pg_title.search("Travel") === -1) {
        suggest = "Ask for Suggestion";
    } else {
        suggest = "Ask for Direction";
    }

var add_element = function (event_head, event_desc, event_date, event_time, task_id){	
	
		a_card = '<div id="' + task_id + '"class="ui card" style="display:inline-block;max-width: 200px; margin: 2px 3px; float: left;"><div class="content overflow_header" style="height: 35px; font-size: 15px; font-weight: bold;"><label class="the_head">' + event_head + '</label></div><div class="content overflow" style="height: 110px;font-size: 12px;"><label class="pull-left the_desc">' + event_desc + '</label></div><div class="content" style="height; 40px; font-size: 12px;"><label class="pull-left the_date" style="float: left">'+ event_date +'</label><div class="ui dropdown" style="float: right;margin-left:20px;"><i class="options icon"></i><div class="menu"><div class="item" onclick="getdata(this.parentNode.parentNode.parentNode.parentNode);">\
                        Edit\
				</div><div class="item" onclick="reminder_comment(this.parentNode.parentNode.parentNode.parentNode);">\
					Add Reminder\
						</div><div class="item" onclick="request_comment(this.parentNode.parentNode.parentNode.parentNode);">\
					' + suggest + '\
				</div><div class="item" onclick="delete_event(this.parentNode.parentNode.parentNode.parentNode);">\
					Remove\
				</div></div></div><label class="pull-left the_time" style="float: right">'+ event_time +'</label></div></div>';

    add_card(a_card);
}
  $(function() {
    $( "#reminder_date" ).datepicker({ minDate: 0});
  });

  $(function() {
      $('#reminder_time').timepicker({
          'minTime': new Date(),
          'maxTime': '12:00am'
      });
  });
var reminder_comment = function(card){
	var card_id = card.id;
	formaction_edit('reminder_form', card_id, "/addtask");
	$('.large.test.modal').modal('show');
}

var request_comment = function(card){
	var card_id = card.id;
	formaction_edit('request_form', card_id, "/addtask");
	$('.small.test.modal').modal('show');
}

var delete_event = function(card){
	var card_id = card.id;
	formaction_edit('delete_form', card_id, "/deltask");
	$('.ui.basic.modal').modal('show');
	console.log(card_id);
}

function formaction_edit( my_form , card_id, action_name){
    if( document.getElementById(my_form).action == action_name ) {
        document.getElementById(my_form).action += card_id;
    }else{
        document.getElementById(my_form).action = action_name + card_id;
    }
}

function formaction_fresh(my_form, action_name){
    document.getElementById(my_form).action = action_name;
}

var getdata = function(card_val){
	console.log(card_val.id);
	var card_head = card_val.getElementsByClassName('the_head')[0].innerHTML;
	var card_desc = card_val.getElementsByClassName('the_desc')[0].innerHTML;
	var card_date = card_val.getElementsByClassName('the_date')[0].innerHTML;
	var card_time = card_val.getElementsByClassName('the_time')[0].innerHTML;
	
	document.getElementById("task_head").value = card_head;
	document.getElementById("task_desc").value = card_desc;
	document.getElementById("task_date").value = card_date;
	document.getElementById("task_time").value = card_time;
	formaction_edit('taskform', card_val.id, "/addtask");
	$('#uimodal').modal('show');$('.hide_label').hide();	
	console.log(card_val.id, card_head, card_desc, card_date, card_time);
}
