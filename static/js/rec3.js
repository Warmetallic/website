// Get the modal
var modal = document.getElementById("myModal3");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg3");
var modalImg = document.getElementById("img03");
var elements = document.getElementById("nav");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  nav.style.display = "none"
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[2];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  nav.style.display = "block"
}