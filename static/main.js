function post(path, params, method='post') {
    // The rest of this code assumes you are not using a library.
    // It can be made less verbose if you use one.
    const form = document.createElement('form');
    form.method = method;
    form.action = path;

    for (const key in params) {
      if (params.hasOwnProperty(key)) {
        const hiddenField = document.createElement('input');
        hiddenField.type = 'hidden';
        hiddenField.name = key;
        hiddenField.value = params[key];
    
        form.appendChild(hiddenField);
      }
    }

    document.body.appendChild(form);
    form.submit();
}

function Down(e){
    paint = true;
    ctx.beginPath();
    ctx.moveTo(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
}
function Up(e){
    paint = false;
    ctx.closePath();
}

function Move(e){
    if( paint == true ){
        ctx.lineTo(e.pageX - this.offsetLeft, e.pageY - this.offsetTop);
        ctx.stroke();
    }
}

document.getElementById("sumBtn").addEventListener("click", (event) => {
    event.preventDefault();
    var dataURL = tablet.toDataURL("image/jpeg");
    post('/compare', {url: dataURL});
});

let tablet = document.getElementById('tablet');
let ctx = tablet.getContext('2d');
let paint = false;
ctx.lineWidth = 10;
ctx.rect(0, 0, 700, 500);
ctx.fillStyle = 'white';
ctx.fill();

tablet.addEventListener("mousedown", Down);
tablet.addEventListener("mouseup",   Up);
tablet.addEventListener("mousemove", Move);