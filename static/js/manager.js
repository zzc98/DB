function Height(obj) {
    let cwin = obj;
    if (document.getElementById) {
        if (cwin && !window.opera) {
            if (cwin.contentDocument && cwin.contentDocument.body.offsetHeight)
                cwin.height = cwin.contentDocument.body.offsetHeight;
            else if (cwin.Document && cwin.Document.body.scrollHeight)
                cwin.height = cwin.Document.body.scrollHeight;
        }
    }
}


$(function () {
    let frameContent = $("#frameContent");
    let frame1 = $("#frame1");
    let frame2 = $("#frame2");
    let frame3 = $("#frame3");
    let frame6 = $("#frame6");
    let frame7 = $("#frame7");
    let frame8 = $("#frame8");
    let frame9 = $("#frame9");
    let frame10 = $("#frame10");
    let frame11 = $("#frame11");
    $("#menu1").click(function () {
        $("#wrap1").slideToggle("slow");
        let img1 = $("#status_img1");
        if (img1.attr("src") === "/static/img/hide.png")
            img1.attr("src", "/static/img/show.png");
        else
            img1.attr("src", "/static/img/hide.png");
    });
    $("#menu2").click(function () {
        $("#wrap2").slideToggle("slow");
        let img2 = $("#status_img2");
        if (img2.attr("src") === "/static/img/hide.png")
            img2.attr("src", "/static/img/show.png");
        else
            img2.attr("src", "/static/img/hide.png");
    });
    $("#menu3").click(function () {
        $("#wrap3").slideToggle("slow");
        let img3 = $("#status_img3");
        if (img3.attr("src") === "/static/img/hide.png")
            img3.attr("src", "/static/img/show.png");
        else
            img3.attr("src", "/static/img/hide.png");
    });
    $("#menu4").click(function () {
        $("#wrap4").slideToggle("slow");
        let img4 = $("#status_img");
        if (img4.attr("src") === "/static/img/hide.png")
            img4.attr("src", "/static/img/show.png");
        else
            img4.attr("src", "/static/img/hide.png");
    });

    frame1.click(function () {
        frameContent.attr("src", "/manager/bookinfo");
        frame1.css("background", '#428bca');
        frame1.css("color", '#ffffff');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame2.click(function () {
        frameContent.attr("src", "/manager/bookkind");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#428bca');
        frame2.css("color", '#ffffff');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame3.click(function () {
        frameContent.attr("src", "/manager/customerinfo");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#428bca');
        frame3.css("color", '#ffffff');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame6.click(function () {
        frameContent.attr("src", "/manager/sellinfo");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#428bca');
        frame6.css("color", '#ffffff');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame7.click(function () {
        frameContent.attr("src", "/manager/pre_sellinfo");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#428bca');
        frame7.css("color", '#ffffff');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame8.click(function () {
        frameContent.attr("src", "/manager/backinfo");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#428bca');
        frame8.css("color", '#ffffff');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame9.click(function () {
        frameContent.attr("src", "/manager/chart1");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#428bca');
        frame9.css("color", '#ffffff');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame10.click(function () {
        frameContent.attr("src", "/manager/chart2");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#428bca');
        frame10.css("color", '#ffffff');
        frame11.css("background", '#fafafa');
        frame11.css("color", '#000');
    });
    frame11.click(function () {
        frameContent.attr("src", "/manager/chart3");
        frame1.css("background", '#fafafa');
        frame1.css("color", '#000');
        frame2.css("background", '#fafafa');
        frame2.css("color", '#000');
        frame3.css("background", '#fafafa');
        frame3.css("color", '#000');
        frame6.css("background", '#fafafa');
        frame6.css("color", '#000');
        frame7.css("background", '#fafafa');
        frame7.css("color", '#000');
        frame8.css("background", '#fafafa');
        frame8.css("color", '#000');
        frame9.css("background", '#fafafa');
        frame9.css("color", '#000');
        frame10.css("background", '#fafafa');
        frame10.css("color", '#000');
        frame11.css("background", '#428bca');
        frame11.css("color", '#ffffff');
    });
});