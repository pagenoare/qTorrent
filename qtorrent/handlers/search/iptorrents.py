import requests
from lxml.html import fromstring

from qtorrent.config import config

cookies = {
    'uid': config.get('iptorrents', 'uid'),
    'pass': config.get('iptorrents', 'pass')
}

BASE_URL = config.get('iptorrents', 'site_url')
SEARCH_URL = config.get('iptorrents', 'search_url')


def parse_torrent(torrent):
    additional_info = torrent.find_class('ac')
    return {
        'title': torrent.find_class('t_title')[0].text,
        'download_url': additional_info[1].find('a').get('href'),
        'size': additional_info[3].text_content(),
        'seeders': additional_info[5].text_content()
    }


def fetch_torrent_list(search_text):
    content = requests.get(
        SEARCH_URL.format(url=BASE_URL, query=search_text), cookies=cookies
    ).content

    parser = fromstring(content)

    torrents = parser.get_element_by_id('torrents').find('table').findall('tr')

    data = [parse_torrent(torrent) for torrent in torrents[1:]]
    return data


def download_torrent_file(url):
    tr = requests.get(BASE_URL + url, cookies=cookies)

    with open('file.torrent', 'w') as f:
        f.write(tr.content)

    return 'file.torrent'