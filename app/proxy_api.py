from aiohttp import web
import aiohttp_jinja2
from aiohttp_jinja2 import template
from plugins.proxy.app.proxy_svc import ProxyService


class ProxyApi:

    def __init__(self):
        self.proxy_svc = ProxyService()

    @template('proxy.html')
    async def landing(self, request):
        return dict(proxy_types=await self.proxy_svc.get_available_proxy_types())

    async def build_proxy(self, request):
        data = dict(await request.json())
        output = await self._create_proxy(request=request, proxy_conf=data)
        return web.json_response(output)

    """ PRIVATE """

    async def _create_proxy(self, request, proxy_conf):
        env = request.app[aiohttp_jinja2.APP_KEY]
        rendered = await self.proxy_svc.render_proxy_config(env, proxy_conf)
        if rendered and proxy_conf['launch_proxy']:
            proxy_process = await self.proxy_svc.spawn_proxy_service(rendered, proxy_conf)
            proxy_dict = dict(config=rendered, proxy_pid=proxy_process.pid)
        elif rendered:
            proxy_dict = dict(config=rendered)
        else:
            proxy_dict = None
        return proxy_dict
