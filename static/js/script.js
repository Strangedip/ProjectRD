function switchTheme() {
    if (document.getElementById('btn-theme').innerHTML === 'Light') {
        document.body.classList.toggle('dark');
        document.getElementById('btn-theme').innerHTML = 'Dark'
    }
    else {
        document.body.classList.toggle('dark');
        document.getElementById('btn-theme').innerHTML = 'Light'
    }
}



function toggleForm() {
    if (document.getElementById('new-item-form').style.display === "none") {
        document.getElementById('new-item-form').style.display = "block";
        document.getElementById('btn-add-item').innerHTML = 'Close';
    }
    else if (document.getElementById('new-item-form').style.display != "none") {
        document.getElementById('new-item-form').style.display = "none";
        document.getElementById('btn-add-item').innerHTML = 'Add new item';
    }
}