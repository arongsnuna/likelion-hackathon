function showResult(){
    var selectValue = $('#selectValue').val();
    var inputValue = $('.form-control').val();
    var url = 'http://127.0.0.1:8000/' + selectValue + '/search/?q=' + inputValue;
    window.location.href = url;
}

