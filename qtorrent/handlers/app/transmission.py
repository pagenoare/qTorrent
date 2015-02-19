import transmissionrpc

from qtorrent.config import config


def start_torrent(torrent):
    tc = transmissionrpc.Client(
        config.get('transmission', 'host'),
        port=config.get('transmission', 'port')
    )
    if config.get('base', 'search') == 'iptorrents':
        tc.add_torrent('file://{}'.format(torrent))

    if config.get('base', 'search') == 'torrentz':
        tc.add_torrent('magnet:?xt=urn:btih:{}'.format(torrent))

