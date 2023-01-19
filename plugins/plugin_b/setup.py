from setuptools import setup

setup(
    name='plugin_b',
    entry_points={
        'plugins': [
            'plugin_b = plugin_b:plugin',
        ],
    }
)