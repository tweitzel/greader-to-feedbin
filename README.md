greader-to-feedbin
==================

stars your google reader entries (exported from google takeout) in feedbin.me

This is very ugly and a stopgap; please fork and fix it up if it pleases you!

Caveat: can't star things that were starred before feedbin existed. Sadface.

example usage:
```
python greader-to-feedbin.py myaddress\@gmail.com-takeout/Reader/starred.json
load starred.json
Feedbin email address: feedbin@example.com
Password:
got https://api.feedbin.me/v1/entries.json?page=1
got https://api.feedbin.me/v1/entries.json?page=2
got https://api.feedbin.me/v1/entries.json?page=3
got https://api.feedbin.me/v1/entries.json?page=4
got https://api.feedbin.me/v1/entries.json?page=5
got https://api.feedbin.me/v1/entries.json?page=6
got https://api.feedbin.me/v1/entries.json?page=7
got https://api.feedbin.me/v1/entries.json?page=8
got https://api.feedbin.me/v1/entries.json?page=9
got https://api.feedbin.me/v1/entries.json?page=10
got https://api.feedbin.me/v1/entries.json?page=11
got https://api.feedbin.me/v1/entries.json?page=12
got https://api.feedbin.me/v1/entries.json?page=13
got https://api.feedbin.me/v1/entries.json?page=14
got https://api.feedbin.me/v1/entries.json?page=15
got https://api.feedbin.me/v1/entries.json?page=16
got https://api.feedbin.me/v1/entries.json?page=17
got https://api.feedbin.me/v1/entries.json?page=18
got https://api.feedbin.me/v1/entries.json?page=19
got https://api.feedbin.me/v1/entries.json?page=20
got https://api.feedbin.me/v1/entries.json?page=21
got https://api.feedbin.me/v1/entries.json?page=22
got https://api.feedbin.me/v1/entries.json?page=23
got https://api.feedbin.me/v1/entries.json?page=24
got https://api.feedbin.me/v1/entries.json?page=25
got https://api.feedbin.me/v1/entries.json?page=26
got https://api.feedbin.me/v1/entries.json?page=27
got https://api.feedbin.me/v1/entries.json?page=28
got https://api.feedbin.me/v1/entries.json?page=29
got https://api.feedbin.me/v1/entries.json?page=30
got https://api.feedbin.me/v1/entries.json?page=31
got https://api.feedbin.me/v1/entries.json?page=32
got https://api.feedbin.me/v1/entries.json?page=33
got https://api.feedbin.me/v1/entries.json?page=34
got https://api.feedbin.me/v1/entries.json?page=35
got https://api.feedbin.me/v1/entries.json?page=36
got https://api.feedbin.me/v1/entries.json?page=37
got https://api.feedbin.me/v1/entries.json?page=38
got https://api.feedbin.me/v1/entries.json?page=39
got https://api.feedbin.me/v1/entries.json?page=40
got https://api.feedbin.me/v1/entries.json?page=41
got https://api.feedbin.me/v1/entries.json?page=42
got https://api.feedbin.me/v1/entries.json?page=43
got https://api.feedbin.me/v1/entries.json?page=44
got https://api.feedbin.me/v1/entries.json?page=45
got https://api.feedbin.me/v1/entries.json?page=46
got https://api.feedbin.me/v1/entries.json?page=47
got https://api.feedbin.me/v1/entries.json?page=48
got https://api.feedbin.me/v1/entries.json?page=49
got https://api.feedbin.me/v1/entries.json?page=50
got https://api.feedbin.me/v1/entries.json?page=51
got https://api.feedbin.me/v1/entries.json?page=52
got https://api.feedbin.me/v1/entries.json?page=53
got https://api.feedbin.me/v1/entries.json?page=54
got https://api.feedbin.me/v1/entries.json?page=55
caught HTTP Status 404
sending request
{'entry_states': [{'entry_id': 1033483,
                   'starred': True,
                   'starred_updated_at': '2013-03-29T22:16:20'},
                  {'entry_id': 1019386,
                   'starred': True,
                   'starred_updated_at': '2013-03-29T22:16:20'},
                  {'entry_id': 1019126,
                   'starred': True,
                   'starred_updated_at': '2013-03-29T22:16:20'},
                  {'entry_id': 794835,
                   'starred': True,
                   'starred_updated_at': '2013-03-29T22:16:20'},
                  {'entry_id': 217012,
                   'starred': True,
                   'starred_updated_at': '2013-03-29T22:16:20'}]}
response
{u'failed': [],
 u'succeeded': [{u'entry_id': 1033483,
                 u'read': True,
                 u'read_updated_at': u'2013-03-29T05:46:11.361861Z',
                 u'starred': True,
                 u'starred_updated_at': u'2013-03-29T22:16:20.000000Z',
                 u'updated_at': u'2013-03-29T22:16:20.000000Z'},
                {u'entry_id': 1019386,
                 u'read': True,
                 u'read_updated_at': u'2013-03-28T04:08:33.577096Z',
                 u'starred': True,
                 u'starred_updated_at': u'2013-03-29T22:16:20.000000Z',
                 u'updated_at': u'2013-03-29T22:16:20.000000Z'},
                {u'entry_id': 1019126,
                 u'read': True,
                 u'read_updated_at': u'2013-03-29T19:28:56.255968Z',
                 u'starred': True,
                 u'starred_updated_at': u'2013-03-29T22:16:20.000000Z',
                 u'updated_at': u'2013-03-29T22:16:20.000000Z'},
                {u'entry_id': 794835,
                 u'read': True,
                 u'read_updated_at': u'2013-03-29T19:28:59.222384Z',
                 u'starred': True,
                 u'starred_updated_at': u'2013-03-29T22:16:20.000000Z',
                 u'updated_at': u'2013-03-29T22:16:20.000000Z'},
                {u'entry_id': 217012,
                 u'read': True,
                 u'read_updated_at': u'2013-03-28T04:24:48.527188Z',
                 u'starred': True,
                 u'starred_updated_at': u'2013-03-29T22:16:20.000000Z',
                 u'updated_at': u'2013-03-29T22:16:20.000000Z'}]}
```
