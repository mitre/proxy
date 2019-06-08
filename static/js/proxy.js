function restRequest(type, data, callback, endpoint='/plugin/proxy/rest') {
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
    let proxy_cfg = {
        'index':'create_proxy',
        'proxy_name':$('#proxy_name').val(),
        'cert_path':$('#cert_path').val(),
        'http_port':$('#http_port').val(),
        'https_port':$('#https_port').val(),
        'caldera_ip':$('#caldera_ip').val(),
        'caldera_port':$('#caldera_port').val(),
        'launch_proxy':$('#launch_proxy').val()
    };
    restRequest('POST', proxy_cfg, createProxyCallback);
}

function createProxyCallback(data) {
    $('#proxy_config').text(data.config);
}

