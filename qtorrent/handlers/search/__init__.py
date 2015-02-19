from importlib import import_module

from qtorrent.config import config

fetch_torrent_list = import_module(
    'qtorrent.handlers.search.{}'.format(config.get('base', 'search'))
).fetch_torrent_list
