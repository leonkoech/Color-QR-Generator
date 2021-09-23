function validateForm() {
    var textInput = document.getElementById('text-input');
    var background = document.getElementById('background');
    var qrCode = document.getElementById('qrCode');
    if (textInput == '') {
        alert("text cannot be null");
    }
}
function validate(val) {
    if(val==0){
        var highlight = document.getElementById('bgcolorhighlight');
 
        var element = document.getElementById('bgswitch');
    
       
        if (element.checked) {
            highlight.style.display = "block";
        }
        else {
            highlight.style.display = "none";
        }
    }
    else{
        var highlight = document.getElementById('qrcolorhighlight');
        var element = document.getElementById('qrswitch');
       
        if (element.checked) {
            highlight.style.display = "block";
        }
        else {
            highlight.style.display = "none";
        }
    }
   
}
function switcher(){
    console.log('qr switch')
   
}