#!/usr/bin/env python

"""
Produces automatic documentation of RPMs and write it directly to the wiki.
"""

import re
from cStringIO import StringIO

import autodoc
import config
from tracWikiClient import TracWikiClient

class UpdateWiki:

    def __init__(self, just_testing = False):
        self.just_testing = just_testing

    def _write_autodoc_table_to_fh(self, fh):
        m = autodoc.MakeDocumentation(verbose = False)
        m.add_all_packages()
        m.write_trac_table(fh)

    def _get_autodoc_table_as_string(self):
        if self.just_testing:
            return "testing\n1\n2\n3\n"
        fh = StringIO()
        self._write_autodoc_table_to_fh(fh)
        return fh.getvalue()

    def _get_updated_content(self, content):
        regexp = ("(.*%s.*?}}})(.*)({{{.*?%s.*)$" % 
                  (config.wiki_token_1, config.wiki_token_2))
        rem = re.match(regexp, content, flags=re.DOTALL)
        if not rem:
            raise Exception("Cannot find comments containing special tokens in page contents.")
        head = rem.group(1) + "\n\n"
        new_table = self._get_autodoc_table_as_string()
        tail = "\n" + rem.group(3)
        return head + new_table + tail

    def update_wiki(self):
        twc = TracWikiClient(top_level_url = config.wiki_top_url,
                             creds_file = config.wiki_creds_file)
        content = twc.read_page(config.wiki_page)
        updated_content = self._get_updated_content(content)
        twc.write_page(config.wiki_page, updated_content,
                       comment="automated update")

if __name__ == '__main__':
    #u = UpdateWiki(just_testing = True)
    u = UpdateWiki()
    u.update_wiki()
