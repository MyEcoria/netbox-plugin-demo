from netbox.plugins import PluginConfig

class NetBoxAccessListsConfig(PluginConfig):
    name = 'counter_plugin'
    verbose_name = 'Access Lists'
    description = 'A simple plugin to demonstrate a basic counter.'
    version = '0.3'
    author = 'MyEcoria'
    author_email = 'contact@myecoria.com'
    base_url = 'counter-plugin'
    required_settings = []
    default_settings = {}

config = NetBoxAccessListsConfig