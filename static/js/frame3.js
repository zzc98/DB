function change_sell(u_id, u_isbn, u_name, u_number, u_price1, u_price2, u_address, u_phone) {
    $('#change_id').val(u_id);
    $('#change_isbn').val(u_isbn);
    $('#change_customer').val(u_name);
    $('#change_number').val(u_number);
    $('#change_price1').val(u_price1);
    $('#change_price2').val(u_price2);
    $('#change_address').val(u_address);
    $('#change_phone').val(u_phone);
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
        'state': $("#change_state").val(),
    };
    $.ajax({
        url: "/manager/change_sell_info",
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
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function del_sell(sell_id) {
    let post_data = {
        "id": sell_id,
    };
    $.ajax({
        url: " /manager/delete_sell",
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


function search_submit() {
    let u_id = $('#search_id').val();
    let u_isbn = $('#search_isbn').val();
    let u_name = $('#search_name').val();
    window.location.href = "/manager/search_sell/?a=" + u_id + "&b=" + u_isbn + "&c=" + u_name;
}

function add_no() {
    $("#add_isbn").val("");
    $("#add_customer").val("");
    $("#add_number").val("");
    $("#add_price1").val("");
    $("#add_price2").val("");
    $("#add_address").val("");
    $("#add_phone").val("");
}