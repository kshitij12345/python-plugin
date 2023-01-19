import pkg_resources

def load_plugins():
    plugins = list()
    for entry_point in pkg_resources.iter_entry_points('plugins'):
        plugins.append(entry_point.load())
    return plugins

plugins = load_plugins()

for plugin in plugins:
    plugin.do_something()
