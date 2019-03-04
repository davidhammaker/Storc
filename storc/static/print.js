document.getElementById('print').addEventListener('click', function() {
    document.getElementById('button_box').style.display = 'none';
    window.print();
    document.getElementById('button_box').style.display = 'inherit';
});
