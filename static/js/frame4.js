function change_pre_sell(u_id, u_isbn, u_customer, u_number, u_price1, u_price2, u_address, u_phone, u_finish) {
    $('#change_id').val(u_id);
    $('#change_isbn').val(u_isbn);
    $('#change_customer').val(u_customer);
    $('#change_number').val(u_number);
    $('#change_price1').val(u_price1);
    $('#change_price2').val(u_price2);
    $('#change_address').val(u_address);
    $("#change_phone").val(u_phone);
    $('#change_finish').val(u_finish);
}

function change_submit() {
    let post_data = {
        'id': $('#change_id').val(),
        'isbn': $('#change_isbn').val(),
        'customer': $('#change_customer').val(),
        'number': $('#change_number').val(),
        'price1': $('#change_price1').val(),
        'price2': $('#change_price2').val(),
        'address': $('#change_address').val(),
        'phone': $('#change_phone').val(),
        'finish': $('#change_finish').val(),
    };
    $.ajax({
        url: "/manager/change_pre_sell_info",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
              swal({icon: 'success', text: "操作成功"}).then(() => {
                    window.location.reload();
                });
            }
            else
               swal({icon: 'error', text: "操作失败"});
            $('#change_id').val("");
            $('#change_isbn').val("");
            $('#change_customer').val("");
            $('#change_number').val("");
            $('#change_price1').val("");
            $('#change_price2').val("");
            $('#change_address').val("");
            $('#change_phone').val("");
            $('#change_finish').val("");
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function del_pre_sell(pre_sell_id) {
    let post_data = {
        "id": pre_sell_id,
    };
    $.ajax({
        url: " /manager/delete_pre_sell",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
                swal({icon: 'success', text: "操作成功"}).then(() => {
                    window.location.reload();
                });
            }
            else
               swal({icon: 'error', text: "操作失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}


function add_submit() {
    let post_data = {
        "isbn": $('#add_isbn').val(),
        "customer": $('#add_customer').val(),
        "number": $('#add_number').val(),
        "price1": $('#add_price1').val(),
        "price2": $('#add_price2').val(),
        "address": $('#add_address').val(),
        "phone": $('#add_phone').val(),
        "finish": $('#add_finish').val(),
    };
    $.ajax({
        url: " /manager/add_pre_sell",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
               swal({icon: 'success', text: "操作成功"}).then(() => {
                    window.location.reload();
                });
                $('#add_isbn').val("");
                $('#add_customer').val("");
                $('#add_number').val("");
                $('#add_price1').val("");
                $('#add_price2').val("");
                $('#add_address').val("");
                $('#add_phone').val("");
                $('#add_finish').val("");
            }
            else
                swal({icon: 'error', text: "操作失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function search_submit() {
    let u_id = $('#search_id').val();
    let u_isbn = $('#search_isbn').val();
    let u_name = $('#search_name').val();
    let u_finish = $('#search_finish').val();
    window.location.href = "/manager/search_pre_sell/?a=" + u_id + "&b=" + u_isbn + "&c=" + u_name + "&d=" + u_finish;
}

function add_no() {
    $("#add_isbn").val("");
    $("#add_customer").val("");
    $("#add_number").val("");
    $("#add_price1").val("");
    $("#add_price2").val("");
    $("#add_address").val("");
    $("#add_phone").val("");
    $("#add_finish").val("");
}