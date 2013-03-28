#!/usr/bin/env python

import getpass
import urllib2
import json
import sys
import pprint

entries_json_url = 'https://api.feedbin.me/v1/entries.json'
states_json_url = 'https://api.feedbin.me/v1/entry_states.json'

if len(sys.argv) != 2:
    sys.exit('Needs path to starred.json file as argument.')

# load starred.json
fp = open(sys.argv[1])
starred = json.load(fp)
starred_urls = []

# compile list of urls to be starred
for i in starred['items']:
    for j in i['alternate']:
        starred_urls.append(j['href'])

# get username and password for feedbin.me
fb_username = raw_input('Feedbin email address: ')
fb_passwd = getpass.getpass()

# construct auth handler for feedbin basic auth.
# Right now feedbin.me uses 'Application' as the realm. This is not codified in the API.
fb_auth_handler = urllib2.HTTPBasicAuthHandler()
fb_auth_handler.add_password(realm='Application',
                          uri=[entries_json_url,states_json_url],
                          user=fb_username,
                          passwd=fb_passwd)
opener = urllib2.build_opener(fb_auth_handler)
urllib2.install_opener(opener)

# feedbin spits things out in 100-entry pages.
fb_entries = []
page = 1
while(True): 
    try:
        fetchurl = ''.join((entries_json_url,'?page=',str(page)))
        fp = urllib2.urlopen(fetchurl)
        fb_entries.extend(json.load(fp))
        print "got %s" % fetchurl
        page = page + 1
    except urllib2.HTTPError as ex:
        print "caught HTTP Status %s" % ex.code
        break

starentries = []
for fb_entry in fb_entries:
    if fb_entry['url'] in starred_urls:
        starentries.append(fb_entry['id'])
