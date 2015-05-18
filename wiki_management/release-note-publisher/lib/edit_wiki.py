#!/usr/bin/env python

"""
update a wiki page, putting new content between the tokens that have been
set up to demarcate the automated content part of the page (replacing 
any existing content between those tokens)
"""

import re

import config
import util
from trac_wiki_client import TracWikiClient

class EditWiki:

    def substitute_content(self, content, new_content):
        regexp = ("(.*%s.*?}}})(.*)({{{.*?%s.*)$" % 
                  (config.wiki_token_1, config.wiki_token_2))
        rem = re.match(regexp, content, flags=re.DOTALL)
        if not rem:
            raise Exception("Cannot find comments containing special tokens in page contents.")
        head = rem.group(1) + "\n\n"
        tail = "\n" + rem.group(3)
        return head + new_content + tail

    def edit_wiki(self, new_content, verbose=False):
        twc = util.call_verbose("Logging into wiki", verbose,
                                TracWikiClient,
                                top_level_url = config.wiki_top_url,
                                creds_file = config.wiki_creds_file)
        content = util.call_verbose("Fetching wiki content", verbose, 
                                    twc.read_page,
                                    config.wiki_page)
        updated_content = self.substitute_content(content, new_content)
        util.call_verbose("Writing updated wiki content", verbose,
                          twc.write_page,
                          config.wiki_page, updated_content,
                          comment="automated update")

if __name__ == '__main__':
    e = EditWiki()
    e.edit_wiki("hello world\ntesting...")
