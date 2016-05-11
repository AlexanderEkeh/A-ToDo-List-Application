var add_card = function (new_card) {$("#task_tags").append(new_card);}

    var pg_title = document.title, suggest = "";
    if (pg_title.search("Travel") === -1) {
        suggest = "Ask for Suggestion";
    } else {
        suggest = "Ask for Direction";
    }

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