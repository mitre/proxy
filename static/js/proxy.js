function restRequest(type, data, callback, endpoint='/plugin/proxy/build') {
    $.ajax({
       url: endpoint,
       type: type,
       contentType: 'application/json',
       data: JSON.stringify(data),
       success:function(data) { callback(data); },
       error: function (xhr, ajaxOptions, thrownError) { console.log(thrownError); }
    });
}

function createProxy() {
    let p_name = $('#proxy_name').val(),
        c_path = $('#cert_path').val(),
        h_port = $('#http_port').val(),
        s_port = $('#https_port').val(),
        c_ip = $('#caldera_ip').val(),
        c_port = $('#caldera_port').val(),
        l_proxy = $('#launch_proxy').val();
    let proxy_cfg = {
        'index':'create_proxy',
        'proxy_name':(p_name) ? p_name : 'haproxy',
        'cert_path':(c_path) ? c_path : 'plugins/proxy/conf/ssl_cert.pem',
        'http_port':(h_port) ? h_port : 80,
        'https_port':(s_port) ? s_port : 443,
        'caldera_ip':(c_ip) ? c_ip : 'localhost',
        'caldera_port':(c_port) ? c_port : 8888,
        'launch_proxy':(l_proxy) ? l_proxy : false
    };
    restRequest('POST', proxy_cfg, createProxyCallback);
}

function createProxyCallback(data) {
    $('#proxy_config').text(data.config);
    if('proxy_pid' in data) {
        flash('flash-proxy-bar', 'Launched proxy with PID ' + data.proxy_pid);
    }else{
        flash('flash-proxy-bar', 'Rendered reverse proxy configuration');
    }
}

function flash(id, msg) {
    $(function () {
        document.getElementById(id).innerHTML = msg;
        $('#' + id).delay(1000).fadeIn('normal', function () {
            $(this).delay(1000).fadeOut();
        });
    });
}

