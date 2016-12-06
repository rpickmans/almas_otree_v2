$(function () {
    // var form = $('#id_raven_p1_form');
    // var checked_val = form.filter("input[name='raven_p1']:checked").val();
    // alert(checked_val)

    $('#raven_form_p').on('change', function() {
        alert($('input[name="raven_p1"]:checked', '#raven_form_p').val());
    });
});