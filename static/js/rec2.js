// Get the modal
var modal = document.getElementById("myModal2");

// Get the image and insert it inside the modal - use its "alt" text as a caption
var img = document.getElementById("myImg2");
var modalImg = document.getElementById("img02");
var elements = document.getElementById("nav");
img.onclick = function(){
  modal.style.display = "block";
  modalImg.src = this.src;
  nav.style.display = "none"
}

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[1];

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
  nav.style.display = "block"
}