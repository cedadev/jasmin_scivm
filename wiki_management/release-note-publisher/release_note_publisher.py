#!/usr/bin/env python

import sys
import time
import os

sys.path.append(os.path.join(os.path.dirname(sys.argv[0]), "lib/"))

import config
import release_info
import edit_wiki
import send_email
import make_content

def releases_reverse_chrono(releases):
    "return-reverse chronological list of releases"
    rel = releases[:]
    rel.sort()
    rel.reverse()
    return rel

def future_releases_chrono(releases):
    "return chronological list of future releases"
    rel = filter(lambda release: release.is_in_future(), 
                             releases)
    rel.sort()
    return rel
    
def do_wiki_page(releases):
    rel = releases_reverse_chrono(releases)
    content = make_content.markup_release_notes(rel)
    e = edit_wiki.EditWiki()
    e.edit_wiki(content, verbose=True)

def do_email(releases):
    rel = future_releases_chrono(releases)
    if rel:
        content = make_content.compose_email(rel)
        send_email.verify_and_send_email(content, verbose=True)

def list_all_releases(releases):
    print "Known releases (past and future)"
    rel = releases[:]
    rel.sort()
    for release in rel:
        print "    version %s install date %s" % (release.version, release.install_date)

def main():
    releases = release_info.read_releases()
    list_all_releases(releases)
    do_wiki_page(releases)
    time.sleep(1)
    do_email(releases)


if __name__ == '__main__':
    main()
