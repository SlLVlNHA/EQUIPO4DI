function show(){
  var pswrd = document.getElementById('pswrd');
  var icon = document.querySelector('.fas');
  if (pswrd.type === "password") {
    pswrd.type = "text";
    pswrd.style.marginTop = "20px";
    icon.style.color = "#FA7F91";           
    pswrd.classList.add('focus-border'); // 
  }else{
    pswrd.type = "password";
    icon.style.color = "#4C8D86";            // Cambia el color del borde del input
    pswrd.classList.remove('focus-border');
  }
}

var lockIcon = document.querySelector('.fa-lock');  
lockIcon.addEventListener('click', function() {            
  document.getElementById('pswrd').focus();
});

var lockIcon = document.getElementById('lock-icon');
var tooltip = document.getElementById('tooltip');

lockIcon.addEventListener('mouseenter', function() {
  tooltip.style.display = 'block';
});

lockIcon.addEventListener('mouseleave', function() {
  tooltip.style.display = 'none';
});