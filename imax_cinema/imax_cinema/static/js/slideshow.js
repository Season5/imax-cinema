var count = 0;

$(document).ready(function slide() {
 var div = $('.cb-slideshow');
 var images = div.find('li');
 var timeOut = 5000;
 var easing = 'linear';
 var totalLength = images.length;
 if (count==0){
    count++;
     for(var x  = 1; x < totalLength; x++){
        $(images[x]).find('div').css({
            'z-index':0,
        });
     }
 }
 $(images).each(function(index, image) {
  var button = $(image).find('div');
  var bg = $(image).find('span');
  $(bg).css({
   'opacity': 0
  });
  setTimeout(function() {
   $(button).css({
    'z-index': 1000
   });
   $(bg).animate({
    'opacity': 1,
   }, timeOut, function() {
    $(button).css({
    'z-index': 0
   });
    $(bg).delay((timeOut / 2)).animate({
     'opacity': 0,
    });
   });
   if (index == totalLength - 1) {
    setTimeout(slide, timeOut);
   }
  }, (timeOut * index));
 });
});