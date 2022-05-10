function post(path, params, method='post') {
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

document.getElementById("europe").addEventListener("click", (event) => {
    event.preventDefault();
    post('/draw', {region: "Europe"});
});

document.getElementById("world").addEventListener("click", (event) => {
    event.preventDefault();
    post('/draw', {region: "World"});
});