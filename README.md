# qTorrent

qTorrent is a simple app, which allows you to add torrents to your torrent app, whithout using browser.

## Currently supported sites

* http://torrentz.com
* https://www.iptorrents.com

## Currently supported apps

* [Transmission](https://www.transmissionbt.com/) via [transmissionrpc](https://pythonhosted.org/transmissionrpc/)

## Demo

https://asciinema.org/a/16718

## Dependencies

* Python (developed and tested on 2.7)

If you willing to use `qTorrent` with Transmission, [transmissionrpc](https://pythonhosted.org/transmissionrpc/) is required too.

This app also uses `requests`, `lxml`, and `urwid`, but these requirements are covered in `setup.py` file.

## How to install

```
git clone git@github.com:pagenoare/qTorrent.git
cd qTorrent
python setup.py install
```

## Configuration

Configuration file should be placed at `$HOME/.qtorrent.rc`

Defaults:

```python
[base]
app = transmission
search = torrentz # or iptorrents

[iptorrents]
uid = # value of cookie called `uid`
pass = # value of cookie called `pass`
site_url = https://iptorrents.com/
search_url = {url}t?720p=on&q={query}&qf=&o=seeders

[torrentz]
site_url = http://torrentz.com/
search_url = {url}search?q={query}

[transmission]
host = localhost
port = 9091
```
