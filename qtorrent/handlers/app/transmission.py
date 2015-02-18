import transmissionrpc


def start_torrent(torrent_file):
    tc = transmissionrpc.Client('localhost', port=9091)
    tc.add_torrent('file://{}'.format(torrent_file))