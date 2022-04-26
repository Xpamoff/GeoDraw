function init() {
    let ctx = tablet.getContext('2d');
    let some = document.getElementsByClassName('transparent')[0];
    let dataURL = "1";
    ctx.lineWidth = 10;
    ctx.rect(0, 0, 700, 500);
    ctx.fillStyle = 'white';
    ctx.fill;
    let paint = false;
    tablet.addEventListener("mousedown", Down);
    tablet.addEventListener("mouseup",   Up);
    tablet.addEventListener("mousemove", Move);
    function Down(e){
         paint = true;
         ctx.beginPath();
         ctx.moveTo(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
    }
    function Up(e){
         paint = false;
         ctx.closePath();
         dataURL = tablet.toDataURL("image/jpeg");
         some.value = dataURL;
    }
    function Move(e){
        if( paint == true ){
            ctx.lineTo(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
            ctx.stroke();
        }
    }
}
function saveUrl(){
    var dataURL = tablet.toDataURL("image/jpeg");
    let some = document.getElementsByClassName('transparent')[0];
    some.value = dataURL;
}
init();