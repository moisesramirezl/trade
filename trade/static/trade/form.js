$(function () {

    /* Functions */

    var loadForm = function (url) {
        var btn = $(this);
        var userId = document.getElementById('userId').value
        $.ajax({
            //url: '/stocksList/create/?userId=' + userId,
            url: btn.attr("data-url"),
            type: 'get',
            dataType: 'json',
            beforeSend: function () {
                $("#modal-stock .modal-content").html("");
                $("#modal-stock").modal("show");
            },
            success: function (data) {
                $("#modal-stock .modal-content").html(data.htmlForm);
            }
        });
    };

    var saveForm = function () {
        var form = $(this);
        $.ajax({
            url: form.attr("action"),
            data: form.serialize(),
            type: form.attr("method"),
            dataType: 'json',
            success: function (data) {
                if (data.formIsValid) {
                    $("#stock-table tbody").html(data.html_stock_list);
                    $("#modal-stock").modal("hide");
                }
                else {
                    $("#modal-stock .modal-content").html(data.htmlForm);
                }
            }
        });
        return false;
    };


    $(".js-create-stock").click(loadForm);
    $("#modal-stock").on("submit", ".js-stock-create-form", saveForm);

    $("#stock-table").on("click", ".js-update-stock", loadForm);
    $("#modal-stock").on("submit", ".js-stock-update-form", saveForm);

});
