document.getElementById("add-q").addEventListener("click",addOne);
var n=1;

function addOne() {
    html='<div class="row" id="row'+n+'">\
    <div class="col-8">\
        <label for="">Question '+n+ '</label>\
        <input type="text" id="row" name="input">\
        <button class="btn btn-outline-danger" id="'+n+'" onclick="remove(this)">Remove</button>\
        </div>\
        </div>'
    form=document.getElementById("input-fields");
    form.innerHTML+=html;
    n++;
}

function remove(button) {
    let div=document.getElementById("row"+button.id);
    div.remove();
}