from setuptools import setup

setup(
    name='plugin_a',
    entry_points={
        'my-plugins': [
            'plugin_a = plugin_a:plugin',
        ],
    }
)
