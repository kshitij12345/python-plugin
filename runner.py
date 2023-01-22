import pkg_resources

def load_plugins():
    plugins = dict()
    for entry_point in pkg_resources.iter_entry_points('my-plugins'):
        plugins[entry_point.name] = entry_point.load()
    return plugins

plugins = load_plugins()

for name, plugin in plugins.items():
    print(f"Executing plugin {name}")
    plugin.do_something()
