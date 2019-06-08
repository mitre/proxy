import os
from subprocess import Popen


class ProxyService:

    def __init__(self):
        pass

    def spawn_proxy_service(self, proxy, conf_path):
        if proxy == 'haproxy':
            proxy_args = [proxy, '-V', '-f', conf_path]
        elif proxy == 'nginx':
            proxy_args = [proxy, '-V', '-c', conf_path]
        else:
            print('Invalid or unsupported proxy selected.')
            return
        try:
            return Popen(proxy_args)
        except FileNotFoundError:
            print('%s is could not be started because the path does not exist.' % proxy)

    @staticmethod
    async def render_proxy_config(env, proxy_cfg):
        try:
            t = env.get_template('%s.conf' % proxy_cfg['proxy_name'])
            return t.render(proxy_cfg)
        except Exception:
            return None

    @staticmethod
    async def get_available_proxy_types():
        return [t.split('.')[0] for t in os.listdir(os.path.abspath(os.path.join('plugins', 'proxy', 'templates')))
                if '.conf' in t]
