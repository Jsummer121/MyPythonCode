var type, sort;
$(function () {
    $('#userImg').hide()
    listenTopSearchHover()
    goSearchPage()
    changeSearchType()
})
//增加浏览器兼容提示
$(function () {

    function isHighBrowser() {
        const userAgent = navigator.userAgent //取得浏览器的userAgent字符串

        //判断Chrome浏览器
        const isChrome = userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Edge") == -1 && userAgent.indexOf("BIDUBrowser") == -1 && userAgent.indexOf("BIDUBrowser") == -1 && userAgent.indexOf("Firefox") == -1

        //判断搜狗浏览器
        const isSougou = userAgent.toLowerCase().indexOf('se 2.x') > -1

        // 360浏览器
        const is360 = userAgent.toLowerCase().indexOf('qihu 360se') > -1

        // qq浏览器
        const isQQ = userAgent.toLowerCase().indexOf('qqbrowser') > -1

        return [isChrome, isSougou, is360, isQQ].some(item => (item == true))
    }

    function showBrowserTip() {
        var html = `
        <div class="fixBrowserTipBox" id="fixBrowserTipBox">
            <div class="fixContiner">
                <div class="fixContentLeft">
                    <div class="fixCLeftContent">
                        <div><img src="https://cdn.code.znzmo.com/zhimo2.0_static/img/browsertip.png" alt=""></div>
                    </div>
                    <div class="fixCRightContent">
                        <div class="fixCtxt">
                            <div class="tipHead">很抱歉，3D侠在您当前的浏览器存在兼容问题</div>
                            <div class="tipBody">为保证您有更好的使用体验，建议您使用<a href="https://www.google.cn/chrome/" target="_blank">Chrome(谷歌)浏览器</a>浏览3D侠</div>
                        </div>
                    </div>
                </div>
                <div class="fixContentRight">
                    <a class="clsoeTip" href="https://www.google.cn/chrome/" target="_blank">立即下载</a>
                    <span class="clsoeTip">关闭</span>
                </div>
            </div>
        </div>
    `;
        $('body').append(html);
        $('body').on('click','.clsoeTip',function () {
            window.localStorage.setItem('browserDay',new Date().getDate())
            $('#fixBrowserTipBox').remove()
        })
    }

    function ifShowBrowserTip() {
        let nowDate = window.localStorage.getItem('browserDay')
        if(new Date().getDate() == nowDate) {
            return
        }
        if(isHighBrowser()){
            return
        }
        showBrowserTip()
    }

    ifShowBrowserTip()
})

//全局登录跳转
$(function () {
    //get_member_set()
    if (location.href == 'https://www.3dxia.com/static/index.html') {
        window.location.href = 'https://www.3dxia.com/'
    }
    $(function () {
        //get_member_set()
        if (location.href == 'https://www.3dxia.com/static/index.html') {
            window.location.href = 'https://www.3dxia.com/'
        }
        function hasPhoneNo() {
            request({
                url: '/personCenter/accountInfo.do',
                async:false,
                success: function (res) {
                    // $.loading.close()
                    if (res.ret == 0) {
                        //这里增加 账号状态判断
                        if(res.data.accountState!==1){
                            alertLogError();
                            return;
                        }
                        if (!res.data.phoneNo) {
                            if (location.href !== 'https://www.3dxia.com/static/register.html') {
                                if (sessionStorage.getItem('upbindPhone') == 'yes') {
                                    logout()
                                } else {
                                    window.location.href = 'https://www.3dxia.com/static/register.html';
                                }
                            }
                        } else {
                            location.href = service;
                        }
                    }
                }
            })
        }
        var code = $.getUrlParam('code');
        var loginType = $.getUrlParam('logintype');
        var service = window.localStorage.getItem('service');
        if (code) {
            var _callback = function () {
                alert(res.msg)
            }
            switch (loginType) {
                case 'weixin':
                    request({
                        url: '/login/wxlogin.do',
                        data: {
                            code: code
                        },
                        type: 'POST',
                        success: function (res) {
                            if (res.ret == 0) {
                                hasPhoneNo();
                            } else {
                                alert(res.msg);
                            }
                        },
                        error: _callback
                    })
                    break;
                case 'qq':
                    request({
                        url: '/login/qqlogin.do',
                        data: {
                            code: code
                        },
                        type: 'POST',
                        success: function (res) {
                            if (res.ret == 0) {
                                hasPhoneNo();
                            } else {
                                alert(res.msg);
                            }
                        },
                        error: _callback
                    })
            }
        }
    });
});

/**
 * 提示登录异常
 */
function alertLogError() {
    layer.closeAll()
    layer.open({
        type: 1,
        title: false,
        shade: 0,
        closeBtn: 0,
        time: 3000,
        skin: 'pop-form',
        content: `<div class="clockLayer">
                            <div style="width:45px">
                                <img src="/static/images/icon_clock_err.png"/>
                            </div>
                            <p>该账号已被禁用,请联系客服!</p>
                        </div>`
    });
    if($('#password_notice')){
        $('#password_notice').text('该账号已被禁用,请联系客服!');
    }
}
//全局ajax
function request(options) {
    options.dataType = options.dataType || 'json';
    options.type = options.type || 'GET';
    if (!options.completeURL) {
        options.url = 'https://www.3dxia.com' + options.url;
        // options.url =  options.url;
    }
    options.data = options.data || {};
    var arr = {};
    arr.timestamp = parseInt((new Date()).getTime() / 1000);
    var success = options.success
    options.success = function (res) {
        if (res.ret == '00005' && location.pathname != '/static/login.html' && !$.getUrlParam('code')) {
            location.href = '/static/login.html?service=' + encodeURIComponent(location.href)
        } else {
            success(res)
        }
    }
    $.ajax(options)
}

function logout() {
    // $.loading.open()
    request({
        url: '/login/invalidateSession.do',
        type: 'POST',
        success: function (res) {
            // $.loading.close()
            if (res.ret == 0) {
                window.sessionStorage.setItem('upbindPhone', '');
                $.popup.msg('退出成功', 1);
                if (location.href.indexOf('/static/') > -1) {
                    window.location.href = 'https://www.3dxia.com/static/login.html'
                } else {
                    setTimeout(function () {
                        window.location.reload();
                    }, 1500)

                }

                //setTimeout('window.location.href="/static/login.html";', 1000);
            } else {
                $.popup.msg(res.msg, 0);
            }
        }
    })
}

// 尾部链接切换
$('.link-title li').click(function () {
    var index = $(this).index();
    $(this).addClass('active').siblings('li').removeClass('active');
    $('.link-content ul').eq(index).addClass('active').siblings('ul').removeClass('active');
});

(function (w) {
    var timerId;
    var j = jQuery,
        _e = {
            popup: {
                msg: function (title, success) {
                    layer.closeAll()
                    layer.open({
                        type: 1,
                        title: false,
                        shade: 0,
                        closeBtn: 0,
                        time: 2000,
                        skin: 'pop-form',
                        content: `<div class="clockLayer">
                            <div style="width:45px">
                                <img src="/static/images/${success ? 'icon_clock_success.png' : 'icon_clock_err.png'}"/>
                            </div>
                            <p>${title}</p>
                        </div>`
                    })
                }
            },
            loading: {
                open: function () {
                    layer.load(2, {
                        shade: [0.5, 'block']
                    })
                },
                close: function () {
                    layer.closeAll('loading')
                }
            },
            getUrlParam: function (name) {
                var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
                var r = window.location.search.substr(1).match(reg);
                return r === null ? null : decodeURIComponent(r[2]);
            },
            payment: function (params, callback) {
                return new Promise(function (resolve, reject) {
                    if (timerId) {
                        clearTimeout(timerId);
                    }
                    request({
                        url: '/personCenter/pay.do',
                        type: 'POST',
                        data: params,
                        success: function (res) {
                            if (res.ret == 0) {
                                if ('function' == typeof callback) {
                                    var pollingFunc = function () {
                                        request({
                                            url: '/personCenter/ifBranch.do',
                                            data: {
                                                payVipOrderId: res.data
                                            },
                                            type: 'POST',
                                            success: function (res) {
                                                if (res.ret == 0) {
                                                    callback();
                                                } else {
                                                    timerId = setTimeout(pollingFunc, 1000);
                                                }
                                            },
                                            error: function () {
                                                timerId = setTimeout(pollingFunc, 1000);
                                            }
                                        });
                                    }
                                    pollingFunc();
                                }
                                resolve(res.data);
                            } else {
                                reject(res.msg);
                            }
                        },
                        error: function () {
                            reject('网络异常');
                        }
                    })
                })
            },
            alipay: function (orderID, subject) {
                return new Promise(function (resolve, reject) {
                    request({
                        url: 'https://api.znzmo.com/pay/alipayUrl.do',
                        completeURL: true,
                        type: 'POST',
                        data: {
                            out_trade_no: orderID,
                            type: 3,
                            subject: subject || '在线支付',
                            qr_pay_mode: 4
                        },
                        success: function (res) {
                            if (res.ret == 0) {
                                resolve(res)
                            } else {
                                reject(res)
                            }
                        },
                        error: function () {
                            reject({ ret: 0, msg: '网络异常' })
                        }
                    })
                })
            },
            wxpay: function (orderID) {
                return 'https://api.znzmo.com/erweima/geterweima.do?type=3&id=' + orderID
            }
        }
    j.extend(_e)
})(window)

$('#userlogin').on('click', function () {
    window.location.href = 'https://www.3dxia.com/static/login.html?service=' + encodeURIComponent(window.location.href);
    return false;

})

$(function () {
    // $.loading.open()
    request({
        url: '/personCenter/accountInfo.do',
        async:false,
        success: function (res) {

            // $.loading.close()
            if (res.ret == 0) {
                getMessageNotificationNums();
                window.user = res.data;
                $('.header .login,.header .register').hide();
                $('#userInfo').hide();
                $('#userImg').show();
                $('.successloginname').text(user.nickName).attr('href', '/static/member.html');
                $('.successloginname').after('&nbsp;&nbsp;<a onclick="logout();"style="cursor: pointer">退出</a>');
                $('#userImg ul').prepend(`<li><a href="https://www.3dxia.com/static/member.html" style="width:60px;text-align:center;overflow:hidden;white-space:nowrap;text-overflow:ellipsis">${user.nickName}</a></li>`);
                $('#accountId_details').val(user.accountId);
                $("#infoImg").attr("src",user.iconUrl);
                if (!user.phoneNo) {
                    if (location.href !== 'https://www.3dxia.com/static/register.html') {
                        if (sessionStorage.getItem('upbindPhone') == 'yes') {
                            logout()
                        } else {
                            window.location.href = 'https://www.3dxia.com/static/register.html';
                        }
                    }
                }
            }
        }
    });

});

//系统消息
function getMessageNotificationNums() {
    request({
        url: '/personCenterMsg/getMessageNotificationNums.do',
        success: function (res) {
            // $.loading.close()
            if (res.ret == 0) {
                if (res.data - 0 > 0) {
                    $('.header ul .for-news .tag span').text(res.data);
                    $('.header ul .for-news .tag').show();
                }
            }
        }
    })
}

//全局搜索功能
$(function () {
    $("#btn_search").click(function () {
        htmlname = $("#text_search").val();
        searchname = $("#active-search").html();
        searchname = searchname ? searchname.trim() : ''
        if (searchname == '3D模型') {
            searchname = 0
        } else if (searchname == 'SU模型') {
            searchname = 1
        } else {
            searchname = 7
        }
        if (htmlname != '') {
            funisskid(htmlname, searchname);
        }
    });

    // $("#text_search").focus(function () {
    //     $('html').bind('keydown', function (e) {
    //         if (e.keyCode == 13) {
    //             htmlname = $("#text_search").val();
    //             if (htmlname != '') {
    //                 funisskid(htmlname);
    //             }
    //         }
    //     });
    // });

    $('body').on('keydown', function (e) {
        if (e.keyCode == 13 && $('#text_search').is(':focus')) {
            htmlname = $("#text_search").val();
            searchname = $("#active-search").html();
            searchname = searchname ? searchname.trim() : ''
            if (searchname == '3D模型') {
                searchname = 0
            } else if (searchname == 'SU模型') {
                searchname = 1
            } else {
                searchname = 7
            }

            if(htmlname != ''){
                funisskid(htmlname, searchname);
            }

        }
    })
});

function funisskid(htmlname, searchname) {
    if (/^[0-9]*$/.test(htmlname) == true) {
        if (searchname == 0) {
            window.open('https://www.3dxia.com/3dmoxing/' + htmlname + '.html');
        } else if (searchname == 1) {
            window.open('https://www.3dxia.com/su/' + htmlname + '.html');
        } else if (searchname == 7) {
            window.open('https://www.3dxia.com/texture/' + htmlname + '.html');
        }
    } else {
        if (searchname == 0) {
            window.open('https://www.3dxia.com/3dmoxing/keywords/'+htmlname+'_0_0_0_0.html');
        } else if (searchname == 1) {
            window.open('https://www.3dxia.com/su/keywords/'+htmlname+'_0_0_0_0.html');
        } else if (searchname == 7) {
            window.open('https://www.3dxia.com/texture/keywords/'+htmlname+'_0_0_0_0.html');
        }
    }
}

$(function () {
    $('.feedback .feed').on('click', function () {
        newPage = layer.open({
            type: 1,
            title: false,
            closeBtn: 0,
            area: ['560px', 'auto'],
            shadeClose: true,
            skin: 'pop-form',
            content: `<div class="modal-content5">
            <span class="close"></span>
            <div class="modal-content-top">
                <p>意见反馈</p>
            </div>
            <form class="modal-box">
                <div class="modal-item">
                    <div>
                        <textarea id="makeERRtextarea" placeholder="感谢您百忙之中提出宝贵的建议，我们会认真阅读，您的支持将给予我们很大的帮助，是对我们最大的鼓励，谢谢！"></textarea>
                    </div>
                </div>
                <div class="modal-item">
                    <div class="right">
                        <input type="submit" id="makeERRSubmit" value="提交"/>
                    </div>
                </div>
            </form>
        </div>`
        })
        return false;
    })
})
$(document).on('click', '#makeERRSubmit', function (e) {
    var sugContent = $('#makeERRtextarea').val();
    e.preventDefault();
    if (sugContent.trim() == '') {
        layer.open({
            type: 1,
            title: false,
            shade: 0,
            closeBtn: 0,
            time: 1000,
            skin: 'pop-form',
            content: `<div class="clockLayer">
                <div>
                    <img src="/static/images/icon_clock_err.png"/>
                </div>
                <p>请填写意见!</p>
            </div>`
        });
    } else {
        request({
            url: '/other/addSuggesstion.do',
            type: 'POST',
            data: {
                sugContent: sugContent,
            },
            success: function (res) {
                if (res.ret == 0) {
                    layer.closeAll();
                    layer.open({
                        type: 1,
                        title: false,
                        shade: 0,
                        closeBtn: 0,
                        time: 1000,
                        skin: 'pop-form',
                        content: `<div class="clockLayer">
                            <div>
                                <img src="/static/images/icon_clock_success.png"/>
                            </div>
                            <p>提交成功!</p>
                        </div>`
                    });
                }
            }
        })
    }
})
$(document).on('click', '.modal-content5 .close', function (e) {
    layer.closeAll()
})

$("body").on('click', '.searchChoice', function (e) {
    let $this = $(e.target);
    $("#active-search").html($this.html())
})
function listenTopSearchHover() {
    $('#topSearch .dropdownSelection').mouseover(function() {
        $('#dropdownSelectionContent').removeClass('hideContent');
    });
    $('#topSearch .dropdownSelection').mouseout(function() {
        $('#dropdownSelectionContent').addClass('hideContent');
    });
    $('#dropdownSelectionContent').mouseover(function() {
        $('#dropdownSelectionContent').removeClass('hideContent');
    });
    $('#dropdownSelectionContent').mouseout(function() {
        $('#dropdownSelectionContent').addClass('hideContent');
    });
    $('#searchPlaceholdDiv').mouseover(function() {
        $('#dropdownSelectionContent').removeClass('hideContent');
    });
    $('#searchPlaceholdDiv').mouseout(function() {
        $('#dropdownSelectionContent').addClass('hideContent');
    });
}
// 转化搜索类型字段
function searchType(type) {
    if(type == '3D模型') {
        return '3dmoxing';
    } else if(type == 'SU模型') {
        return 'su';
    } else {
        return 'texture';
    }
}
// 拼搜索跳转url
function searchUrl(searchValue) {
    // 搜索中的模型类型
    var searchModelType;
    // 判断哪个搜索框
    if(whichSearch == 'first') {
        searchModelType = searchType($('#topType').text());
        var searchname;
        if (searchModelType=='3dmoxing'){
            searchname = 0;
        }else if (searchModelType=='su'){
            searchname = 1;
        } else {
            searchname = 7;
        }
        return funisskid(searchValue,searchname);
    }
}

// 搜索跳转
function goSearchPage() {
    // 第一个搜索框
    // 点击确定
    $('#topSearchIcon').click(function() {
        var searchValue = $('#topSearchInput').val();
        whichSearch = 'first';
        !searchValue ? null : searchUrl(searchValue);
    });

    // 按下回车
    $('#topSearchInput').bind('keypress', function(e) {
        if(e.keyCode == '13') {
            var searchValue = $('#topSearchInput').val();
            whichSearch = 'first';
            !searchValue ? null : searchUrl(searchValue);
        }
    });


    // 第二个搜索框
    // 点击确定
    $('#secondSearchIcon').click(function() {
        var searchValue = $('#secondSearchInput').val();
        whichSearch = 'second';
        !searchValue ? null : searchUrl(searchValue);
    });

    // 按下回车
    $('#secondSearchInput').bind('keypress', function(e) {
        if(e.keyCode == '13') {
            var searchValue = $('#secondSearchInput').val();
            whichSearch = 'second';
            !searchValue ? null : searchUrl(searchValue);
        }
    });
}
// 切换搜索类型
function changeSearchType() {
    $('#dropdownSelectionContent a div').click(function () {
        // console.warn($(this).text());
        // console.warn($('#topType').text());
        $('#topType span').text($(this).text());
    });
    $('#dropdownSecondSelectionContent a div').click(function () {
        // console.warn($(this).text());
        // console.warn($('.dropdownSelection div').text());
        $('.dropdownSelection div').text($(this).text());
    });
}
