import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader
from subprocess import Popen

class ProxyService:

    def __init__(self):
        pass

    def spawn_proxy_service(proxy, conf_path):
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

    def render_proxy_config(cfg):
        env = Environment(
            loader=FileSystemLoader(searchpath='conf')
        )
        template = env.get_template(cfg['proxy_template'])
        rendered = '%s-%s-rendered.conf' % (cfg['proxy_name'], datetime.now().strftime('%Y%H%M%S'))
        with open(os.path.abspath(os.path.join('conf', rendered)), 'w') as f:
            f.write(template.render(cert_path=cfg['cert_path'],
                                    http_port=cfg['http_port'],
                                    https_port=cfg['https_port'],
                                    caldera_ip=cfg['caldera_ip'],
                                    caldera_port=cfg['caldera_port']))
        print("%s config rendered at %s" % (cfg['proxy_name'], rendered))
        return os.path.join('conf', rendered)

    @staticmethod
    async def get_available_proxy_types():
        return [t.split('.')[0] for t in os.listdir(os.path.abspath(os.path.join('plugins', 'proxy', 'templates')))
                if '.conf' in t]
