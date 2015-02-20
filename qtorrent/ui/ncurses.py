import urwid

from qtorrent.config import config

from qtorrent.handlers.search import fetch_torrent_list, download_torrent_file
from qtorrent.handlers.app import start_torrent


def generate_torrent_list(choices):
    body = []
    for entry in choices:
        button = urwid.Button(
            '{title} (Size: {size}, Seeders: {seeders})'.format(**entry)
        )
        urwid.connect_signal(
            button, 'click', item_chosen, entry['download_url']
        )
        body.append(urwid.AttrMap(button, None, focus_map='reversed'))
    return body


def item_chosen(button, choice):
    response = urwid.Text([u'Adding torrent to transmission: ', choice, u'\n'])
    if config.get('base', 'search') == 'iptorrents':
        choice = download_torrent_file(choice)
    start_torrent(choice)
    top.set_footer(response)


class Asdf(urwid.Edit):

    def keypress(self, size, key):
        if key != 'enter':
            return super(Asdf, self).keypress(size, key)

        choices = fetch_torrent_list(self.edit_text)
        top.set_body(
            urwid.ListBox(
                urwid.SimpleFocusListWalker(generate_torrent_list(choices))
            )
        )
        top.focus_part = 'body'

ask = Asdf('Search: ')

placeholder = urwid.ListBox(urwid.SimpleFocusListWalker([]))
top = urwid.Frame(placeholder, header=ask, focus_part='header')


def body_key_handler(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()
    if key == '/':
        top.focus_part = 'header'
        return


def main():
    try:
        urwid.MainLoop(top, unhandled_input=body_key_handler).run()
    except KeyboardInterrupt:
        raise urwid.ExitMainLoop()
