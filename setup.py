try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Weather Data Management',
    'author': 'Vasudev Kumanduri',
    'url': 'No url defined yet',
    'download_url': 'No download URL yet',
    'author_email': 'cdi_v@yahoo.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['WMD'],
    'scripts': [],
    'name': 'weather_data_mgmt'
}

setup(**config)

