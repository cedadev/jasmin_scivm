#!/usr/bin/env python

"""
update a wiki page, putting new content between the tokens that have been
set up to demarcate the automated content part of the page (replacing 
any existing content between those tokens)
"""

import re

import config
import util
from github_wiki_client import GithubWikiClient

class EditWiki:

    def substitute_content(self, content, new_content):
        regexp = ("(.*%s.*?-->)(.*)(<!--.*?%s.*)$" % 
                  (config.wiki_token_1, config.wiki_token_2))
        rem = re.match(regexp, content, flags=re.DOTALL)
        if not rem:
            raise Exception("Cannot find comments containing special tokens in page contents.")
        head = rem.group(1) + "\n\n"
        tail = "\n" + rem.group(3)
        return head + new_content + tail

    def edit_wiki(self, new_content, verbose=False):
        gwc = util.call_verbose("Logging into wiki", verbose,
                                GithubWikiClient,
                                path = config.wiki_path,
                                local_path = config.wiki_workdir,
                                creds_file = config.wiki_creds_file)
        content = util.call_verbose("Fetching wiki content", verbose, 
                                    gwc.read_page,
                                    config.wiki_page)
        updated_content = self.substitute_content(content, new_content)
        if content == updated_content:
            print "no changes to make"
        else:
            util.call_verbose("Writing updated wiki content", verbose,
                              gwc.write_page,
                              config.wiki_page, updated_content,
                              message="automated update")

if __name__ == '__main__':
    e = EditWiki()
    e.edit_wiki("hello world\ntesting...")
