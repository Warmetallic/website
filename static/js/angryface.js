$(document).ready(function(){
    $("#face").dblclick(function(){
        var obj = document.createElement("audio");
        obj.src = "mchammer.mp3"; 
        obj.play(); 
    });
  });