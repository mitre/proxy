from plugins.proxy.app.proxy_api import ProxyApi

name = 'Proxy'
description = 'Spawn a reverse proxy service in front of the Caldera app'
address = '/plugin/proxy/gui'


async def initialize(app, services):
    proxy_api = ProxyApi()
    services.get('auth_svc').set_unauthorized_static('/proxy', 'plugins/proxy/static', append_version=True)
    services.get('auth_svc').set_authorized_route('GET', '/plugin/proxy/gui', proxy_api.landing)
    services.get('auth_svc').set_authorized_route('POST', '/plugin/proxy/build', proxy_api.build_proxy)