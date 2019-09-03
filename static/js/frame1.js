function getCookie(cname) {
    let name = cname + "=";
    let ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i].trim();
        if (c.indexOf(name) === 0)
            return c.substring(name.length, c.length);
    }
    return "";
}

// 修改书籍信息时显示原来信息
function change_book(b_isbn, b_title, b_price, b_author, b_des, b_type, b_number, b_on_sale) {
    $('#change_isbn').val(b_isbn);
    $('#change_title').val(b_title);
    $('#change_price').val(b_price);
    $('#change_author').val(b_author);
    $('#change_des').val(b_des);
    $('#change_type').val(b_type);
    $('#change_number').val(b_number);
    $('#change_on_sale').val(b_on_sale);
    document.cookie = "b_isbn=" + b_isbn;
}

// 提交修改信息
function change_submit() {
    let post_data = {
        "isbn": getCookie('b_isbn'),
        "title": $('#change_title').val(),
        "price": $('#change_price').val(),
        "author": $('#change_author').val(),
        "des": $('#change_des').val(),
        "type": $('#change_type').val(),
        "number": $('#change_number').val(),
        "on_sale": $('#change_on_sale').val(),
    };
    $.ajax({
        url: "/manager/change_book_info",
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

// 删除书籍
function del_book(b_isbn) {
    let post_data = {"isbn": b_isbn};
    $.ajax({
        url: " /manager/delete_book",
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
                swal({icon: 'error', text: "删除书籍失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

// 增加书籍
function add_submit() {
    let post_data = new FormData($("#my_form1")[0]);
    $.ajax({
        url: " /manager/add_book",
        type: "POST",
        data: post_data,
        cache: false,
        processData: false,
        contentType: false,
        success: function (data) {
            data = JSON.parse(data);
            if (data["status"] === 1) {
                swal({icon: 'success', text: "操作成功"}).then(() => {
                    window.location.reload();
                });
                $('#add_isbn').val("");
                $('#add_title').val("");
                $('#add_price').val("");
                $('#add_author').val("");
                $('#add_des').val("");
                $('#add_type').val("");
                $('#add_img').val("");
                $('#add_number').val("");
                $('#add_on_sale').val("");
                $("#add_choose_file").val("");
            }
            else
                swal({icon: 'error', text: "添加失败"});
        },
        error: function () {
            swal({icon: 'error', text: "服务异常"});
        }
    });
}

function add_no() {
    $('#add_isbn').val("");
    $('#add_title').val("");
    $('#add_price').val("");
    $('#add_author').val("");
    $('#add_des').val("");
    $('#add_type').val("");
    $('#add_img').val("");
    $('#add_number').val("");
    $('#add_on_sale').val("");
    $("#add_choose_file").val("");
}

//查询书籍
function search_submit() {
    let isbn = $('#search_isbn').val();
    let title = $('#search_title').val();
    let author = $('#search_author').val();
    let type_ = $('#search_type').val();
    let on_sale = $("#search_on_sale").val();
    window.location.href = "/manager/search_book/?a=" + isbn + "&b=" + title + "&c=" + author + "&d=" + type_ + "&e=" + on_sale;

}




$(function () {
    $("#add_choose_file").click(function () {
        $("#add_img").click();
    });
    $("#add_img").change(function () {
        $("#add_choose_file").val($(this).val().replace("C:\\fakepath\\", ""));
    })
});