function custom_ajax(path, csrf, booked_seats) {
    $('.action--buy').click(function() {
        console.log(seating(booked_seats));
        $.ajax({
            url: path,
            type: "POST",
            data: {
                seats: seating(booked_seats),
                csrfmiddlewaretoken: csrf,
            },
            success: function(data) {
                succeed(data);
            },
            error: function(jqXHR, textStatus) {
                console.log("Request failed: " + textStatus);
            }
        });
    });
}

function seating(booked_seats) {
    $('.tooltip').click(function() {
        getSeats(booked_seats);
    });
    return getSeats(booked_seats);
}

function getSeats(booked_seats) {
    var seatValues = [];
    var seat = $('.row').find('.row__seat--selected');
    $(seat).each(function(index, data) {
        if ($.inArray($(data).attr('data-tooltip'), booked_seats) == -1) {
            seatValues.push($(data).attr('data-tooltip'));
            seatValues = $.unique(seatValues);
        }
    });
    return seatValues;
}

function succeed(data) {

    var reg_tkts = $('#id_number_of_regular_tickets');
    var stu_tkts = $('#id_number_of_student_tickets');
    var num_tkts = $('#num_tkt');
    var tk_tkts = $('#tk_tkt');
    var ticketing = $('.ticketing');
    var reg_id = reg_tkts.attr('id');
    var stu_id = stu_tkts.attr('id');
    $('.price').css({
        'height': '100px',
        'overflow-y': 'scroll'
    });
    $('p').css({
        'color': '#000'
    });
    $('span').css({
        'color': '#000'
    });
    // $('#formie').hide();


    var num_seats = data.seats.length;
    $('#seating').text(data.seats.toString());
    ticketing.attr('max', num_seats.toString())
    num_tkts.text(num_seats);
    num_tkts.val(num_seats);
    var total = 0;
    console.log("Seats", num_seats);
    ticketing.change(function() {
        var stu = stu_tkts.val();
        var reg = reg_tkts.val();
        var current = $(this);
        total = +stu + +reg;
        console.log("Total", total);
        if (reg_id === current.attr('id')) {
            var remaining_tkts = (num_seats - +stu);
            console.log("Tkts", remaining_tkts);
            stu_tkts.attr('max', remaining_tkts.toString());
            console.log("Regular");
            if (total > num_seats) {
                total = num_seats;
                current.val(remaining_tkts);
            }
            else {
                tk_tkts.text(total);
                console.log("Total", total);
            }
        }
        else if (stu_id === current.attr('id')) {
            var remaining_tkts = (num_seats - +reg);
            console.log("Tkts", remaining_tkts);
            reg_tkts.attr('max', remaining_tkts.toString());
            console.log("Student");
            if (total > num_seats) {
                total = num_seats;
                current.val(remaining_tkts);
            }
            else {
                tk_tkts.text(total);
                console.log("Total", total);
            }
        }
    });
}