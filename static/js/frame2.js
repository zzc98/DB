function change_user(u_id, u_name, u_password, u_phone, u_credit, u_sex, u_birthday, u_address) {
    $('#change_id').val(u_id);
    $('#change_name').val(u_name);
    $('#change_password').val(u_password);
    $('#change_phone').val(u_phone);
    $('#change_credit').val(u_credit);
    $("#change_sex").val(u_sex);
    $("#change_address").val(u_address);
}

function change_submit() {
    let post_data = {
        'uid': $('#change_id').val(),
        "name": $('#change_name').val(),
        "password": $('#change_password').val(),
        "phone": $('#change_phone').val(),
        "credit": $('#change_credit').val(),
        "sex": $('#change_sex').val(),
        "birthday": $('#change_birthday').val(),
        "address": $('#change_address').val()
    };
    $.ajax({
        url: "/manager/change_user_info",
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
            $('#change_name').val("");
            $('#change_password').val("");
            $('#change_phone').val("");
            $('#change_credit').val("");
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function del_user(uid) {
    let post_data = {
        "uid": uid,
    };
    $.ajax({
        url: " /manager/delete_user",
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
        "name": $('#add_name').val(),
        "password": $('#add_password').val(),
        "phone": $('#add_phone').val(),
        "credit": $('#add_credit').val(),
        "sex": $("#add_sex").val(),
        "birthday": $("#add_birthday").val(),
        "address": $("#add_address").val()
    };
    $.ajax({
        url: " /manager/add_user",
        type: "POST",
        data: post_data,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
                swal({icon: 'success', text: '添加成功，ID号是' + data['uid']}).then(() => {
                    window.location.reload();
                });
                $('#add_name').val("");
                $('#add_password').val("");
                $('#add_phone').val("");
                $('#add_credit').val("");
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
    let uid = $('#search_id').val();
    let uname = $('#search_name').val();
    window.location.href = "/manager/search_user/?a=" + uid + "&b=" + uname;
}

function add_no() {
    $("#add_name").val("");
    $("#add_password").val("");
    $("#add_phone").val("");
    $("#add_credit").val("");
}