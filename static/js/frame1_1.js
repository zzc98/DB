let k_id;

// 修改类别信息时显示原来信息
function change_kind(kind_id, kind_name) {
    $("#change_kind_id").val(kind_id);
    $("#change_kind_name").val(kind_name);
    k_id = kind_id;
}

// 提交修改信息
function change_submit() {
    let post_data = {
        "kind_id": k_id,
        "kind_name": $("#change_kind_name").val()
    };
    $.ajax({
        url: "/manager/change_kind",
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
                swal({icon: 'error', text: "修改失败"});
            $('#change_isbn').val("");
            $('#change_title').val("");
            $('#change_price').val("");
            $('#change_author').val("");
            $('#change_des').val("");
            $('#change_type').val("");
            $('#change_number').val("");
            $('#change_on_sale').val("");
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

// 删除类别
function del_kind(kind_id) {
    let post_data = {
        "kind_id": kind_id
    };
    $.ajax({
        url: " /manager/delete_kind",
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
                swal({icon: 'error', text: "修改失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

// 增加类别
function add_submit() {
    let post_data = {"kind_name": $('#add_kind_name').val()};
    $.ajax({
        url: " /manager/add_kind",
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
                swal({icon: 'error', text: "添加类别失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

//取消增加类别
function add_no() {
    $('#add_kind_name').val("");
}
