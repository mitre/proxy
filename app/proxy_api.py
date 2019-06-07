from aiohttp import web
from aiohttp_jinja2 import template

from plugins.proxy.app.proxy_svc import ProxyService

class ProxyApi:

    def __init__(self, services):
        self.proxy_svc = ProxyService(services)

    @template('proxy.html')
    async def landing(self, request):
        return dict(proxy_types=self.proxy_svc.get_available_proxy_types())

    async def rest_api(self, request):
        data = dict(await request.json())
        index = data.pop('index')
        options = dict(
            POST=dict(
                launch_proxy=lambda d: self.launch_proxy(proxy=d)
            )
        )
        output = await options[request.method][index](data)
        return web.json_response(output)

    """ PRIVATE """

    async def _launch_proxy(self, proxy):
        await self.proxy_svc.render_proxy_config(proxy)