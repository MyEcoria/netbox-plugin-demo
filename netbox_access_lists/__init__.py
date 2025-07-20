from netbox.plugins import PluginConfig

class NetBoxAccessListsConfig(PluginConfig):
    name = 'netbox_access_lists'
    verbose_name = 'Access Lists'
    description = 'A simple plugin to demonstrate a basic counter.'
    version = '0.1'
    author = 'Your Name'
    author_email = 'your.email@example.com'
    base_url = 'access-lists'
    required_settings = []
    default_settings = {}

config = NetBoxAccessListsConfig