var slideIndex = 1;
showSlides(slideIndex);
//shows first slide
// Next/previous controls
function plusSlides(n) {
  showSlides(slideIndex += n);
}
// move on to next slide

// Thumbnail image controls
function currentSlide(n) {
  showSlides(slideIndex = n);
}
// which slide will show up first? Which slide you are on. //

function showSlides(n) {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  var dots = document.getElementsByClassName("dot");
  if (n > slides.length) {slideIndex = 1}
  if (n < 1) {slideIndex = slides.length}
  for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
  }
  for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
  }
  slides[slideIndex-1].style.display = "block";
  dots[slideIndex-1].className += " active";
}
