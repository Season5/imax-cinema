function seatBooking(seats) {
    var grid = $('.row').find('.tooltip');
    $(grid).addClass('gray');
    $(grid).removeAttr('id');
    $(grid).removeClass('booked');

    $(grid).each(function() {
        if ($.inArray($(this).attr('data-tooltip'), seats) !== -1) {
            $(this).removeClass('gray');
            $(this).addClass('booked');
            $(this).attr('id', 'red');
        } else {
            $(this).click(function(){
                $(this).toggleClass('blue');
            });
        }
    });
    return seats;
}