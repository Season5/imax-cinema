function seatBooking() {
    var occupied = $('.occupied');
    occupied.hide();
    var occupied_seats = []
    var grid = $('.row').find('.tooltip');
    occupied.each(function() {
        occupied_seats.push($(this).text());
        occupied_seats = $.unique(occupied_seats);
    });
    $(grid).each(function() {
        if ($.inArray($(this).attr('data-tooltip'), occupied_seats) !== -1) {
            $(this).css({
                'background': 'red'
            });
        }
    });
    return occupied_seats;
}