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

    async def rest_api(self, request):
        data = dict(await request.json())
        index = data.pop('index')
        options = dict(
            POST=dict(
                create_proxy=lambda d: self._launch_proxy(request=request, proxy=d)
            )
        )
        output = await options[request.method][index](data)
        return web.json_response(output)

    """ PRIVATE """

    async def _launch_proxy(self, request, proxy):
        env = request.app[aiohttp_jinja2.APP_KEY]
        rendered = await self.proxy_svc.render_proxy_config(env, proxy)
        if rendered:
            return dict(config=rendered)
        return None
