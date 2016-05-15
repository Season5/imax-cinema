$(function() {
    $("#datepicker").datepicker({
        dateFormat: "yy-mm-dd"
    });
});

function getDate(path, id) {
    var date;
    $('#datepicker').change(function() {
        date = $(this).val();
        $.ajax({
            url: path,
            method: "GET",
            data: {
                'date': date,
                'movie_id': id,
            },
            success: function(data) {
                return seatBooking(data.seats);
            },
            error: function(jqXHR, textStatus) {
                console.log("Request failed: " + textStatus);
            },
        });
    });
}