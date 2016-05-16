$(function() {
    $("#datepicker").datepicker({
        dateFormat: "yy-mm-dd"
    });
});

var count = 0;

function getDate(path, id) {
    var date;
    if (count == 0) {
        date = $('#datepicker').val();
        send(date);
        count++;
    }
    $('#datepicker').change(function() {
        date = $(this).val();
        send(date);
    });

    function send(date) {
        $.ajax({
            url: path,
            method: "GET",
            data: {
                'date': date,
                'movie_id': id,
            },
            success: function(data) {
                seatBooking(data.seats);
            },
            error: function(jqXHR, textStatus) {
                console.log("Request failed: " + textStatus);
            },
        });
    }
}