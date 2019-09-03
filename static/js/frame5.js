function change_back(u_id, u_isbn, u_name, u_number, u_money, u_finish) {
    $('#change_id').val(u_id);
    $('#change_isbn').val(u_isbn);
    $('#change_customer').val(u_name);
    $('#change_number').val(u_number);
    $('#change_money').val(u_money);
    $('#change_finish').val(u_finish);
}

function change_submit() {
    let post_data = {
        'id': $('#change_id').val(),
        'isbn': $('#change_isbn').val(),
        'customer': $('#change_customer').val(),
        'number': $('#change_number').val(),
        'money': $('#change_money').val(),
        'finish': $('#change_finish').val(),
    };
    $.ajax({
        url: "/manager/change_back_info",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 2) {
                swal({icon: 'error', text: "操作异常！没有此书或没有此顾客"});
            }
            else if (data["status"] === 1) {
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
            $('#change_money').val("");
            $('#change_finish').val("");
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function del_back(back_id) {
    swal({
        title: "警告",
        text: "您确定删除该顾客及其信息？",
        icon: "warning",
        buttons: true,
        dangerMode: true,
    }).then((o) => {
        if (o) {
            let post_data = {
                "id": back_id,
            };
            $.ajax({
                url: " /manager/delete_back",
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
    });
}


function add_submit() {
    let post_data = {
        "isbn": $('#add_isbn').val(),
        "customer": $('#add_customer').val(),
        "number": $('#add_number').val(),
        "money": $('#add_money').val(),
        "finish": $('#add_finish').val(),
    };
    $.ajax({
        url: " /manager/add_back",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
                swal({icon: 'success', text: '添加成功，ID号是' + data['id']}).then(() => {
                    window.location.reload();
                });
                $('#add_isbn').val("");
                $('#add_customer').val("");
                $('#add_number').val("");
                $('#add_money').val("");
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
    window.location.href = "/manager/search_back/?a=" + u_id + "&b=" + u_isbn + "&c=" + u_name + "&d=" + u_finish;
}


function add_no() {
    $("#add_isbn").val("");
    $("#add_customer").val("");
    $("#add_number").val("");
    $("#add_money").val("");
    $("#add_finish").val("");
}