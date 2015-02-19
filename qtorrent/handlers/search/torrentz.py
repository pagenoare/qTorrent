import requests
from lxml.html import fromstring

from qtorrent.config import config

BASE_URL = config.get('torrentz', 'site_url')
SEARCH_URL = config.get('torrentz', 'search_url')


def parse_torrent(torrent):
    link = torrent.find('dt').find('a')
    return {
        'title': link.text_content(),
        'download_url': link.get('href')[1:],
        'size': torrent.find_class('s')[0].text_content(),
        'seeders': torrent.find_class('u')[0].text_content()
    }


def fetch_torrent_list(search_text):
    content = requests.get(
        SEARCH_URL.format(url=BASE_URL, query=search_text)
    ).content

    parser = fromstring(content)
    results = parser.find_class('results')
    if not results:
        return

    torrents = results[0].findall('dl')

    data = [parse_torrent(torrent) for torrent in torrents]
    return data