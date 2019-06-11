import os
from subprocess import Popen


class ProxyService:

    async def spawn_proxy_service(self, rendered, proxy_conf):
        path = await self._save_proxy_config(rendered, proxy_conf)
        proxy_args = [proxy_conf['proxy_name'], '-V', '-f', path]
        try:
            return Popen(proxy_args)
        except FileNotFoundError:
            return '%s could not be started because the path does not exist.' % proxy_conf['proxy_name']

    @staticmethod
    async def render_proxy_config(env, proxy_cfg):
        proxy_cfg['cert_path'] = os.path.abspath(proxy_cfg['cert_path'])
        try:
            t = env.get_template('%s.conf' % proxy_cfg['proxy_name'])
            return t.render(proxy_cfg)
        except Exception:
            return None

    @staticmethod
    async def get_available_proxy_types():
        return [t.split('.')[0] for t in os.listdir(os.path.abspath(os.path.join('plugins', 'proxy', 'templates')))
                if '.conf' in t]

    """ PRIVATE """

    @staticmethod
    async def _save_proxy_config(rendered, proxy_conf):
        save_path = os.path.abspath(os.path.join('plugins', 'proxy', 'conf', proxy_conf['proxy_name']+'-rendered.conf'))
        with open(save_path, "w") as c:
            c.write(rendered)
        return save_path
