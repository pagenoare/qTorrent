import ConfigParser
import os.path


class ImproperlyConfigured(Exception):
    pass


CONFIG_PATH = os.path.expanduser('~/.qtorrent.rc')

config = ConfigParser.ConfigParser()

config.read(CONFIG_PATH)

# set defaults if doesnt exist
if not config.has_section('base'):
    config.add_section('base')

if not config.has_option('base', 'search'):
    config.set('base', 'search', 'torrentz')

if not config.has_option('base', 'app'):
    config.set('base', 'app', 'transmission')

# config checks for iptorrents engine
if config.get('base', 'search') == 'iptorrents':
    if not config.has_section('iptorrents'):
        raise ImproperlyConfigured(
            'Missing configuration for iptorrents engine'
        )

    if not config.has_option('iptorrents', 'uid'):
        raise ImproperlyConfigured(
            'Missing `uid` for iptorrents engine'
        )

    if not config.has_option('iptorrents', 'pass'):
        raise ImproperlyConfigured(
            'Missing `pass` for iptorrents engine'
        )

    if not config.has_option('iptorrents', 'site_url'):
        config.set(
            'iptorrents',
            'site_url',
            'https://www.iptorrents.com/'
        )

    if not config.has_option('iptorrents', 'search_url'):
        config.set(
            'iptorrents',
            'search_url',
            '{url}t?720p=on&q={query}&qf=&o=seeders'
        )

# config checks for torrentz engine
if config.get('base', 'search') == 'torrentz':
    if not config.has_section('torrentz'):
        config.add_section('torrentz')

    if not config.has_option('torrentz', 'site_url'):
        config.set(
            'torrentz',
            'site_url',
            'http://torrentz.com/'
        )

    if not config.has_option('torrentz', 'search_url'):
        config.set(
            'torrentz',
            'search_url',
            '{url}search?q={query}'
        )

# config checks for transmission
if config.get('base', 'app') == 'transmission':
    if not config.has_section('transmission'):
        config.add_section('transmission')

    if not config.has_option('transmission', 'host'):
        config.set(
            'transmission',
            'host',
            'localhost'
        )

    if not config.has_option('transmission', 'port'):
        config.set(
            'transmission',
            'port',
            '9091'
        )
