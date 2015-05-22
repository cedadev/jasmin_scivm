import mechanize

class TracWikiClient(object):

    def __init__(self,
                 top_level_url = "http://team.ceda.ac.uk/trac/ceda/",
                 creds_file = "/tmp/creds"):
        self.top_level_url = top_level_url
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        self._setup_creds(creds_file)

    def _setup_creds(self, creds_file):
        user, password = self._read_creds_file(creds_file)
        self.browser.add_password(self.top_level_url,
                                  user, password)
        login_url = self.get_login_url()
        response = self.browser.open(login_url)
        if "logged in as %s" % user not in response.read():
            raise Exception("login failure")

    def _read_creds_file(self, path):
        """
        read credentials file containing username, password on separate lines,
        return 2-element tuple (user, password)
        """
        f = open(path)
        user = f.readline().replace("\n", "")
        password = f.readline().replace("\n", "")
        f.close()
        return user, password

    def get_page_url(self, page_name):
        return "%s/wiki/%s" % (self.top_level_url, page_name)

    def get_login_url(self):
        return "%s/login" % self.top_level_url

    def read_page(self, page_name):
        """
        get raw content of page
        """
        url = self.get_page_url(page_name)
        return self.browser.open(url + "?format=txt").read()
    
    def write_page(self, page_name, new_contents, comment=""):
        """
        write raw content to page 
        """
        url = self.get_page_url(page_name)
        response = self.browser.open(url + "?action=edit")
        forms = mechanize.ParseResponse(response, 
                                        backwards_compat=False)
        edit_form = self._find_edit_form(forms)
        old_contents = edit_form.get_value(name="text")
        if old_contents.replace("\r\n", "\n") == new_contents.replace("\r\n", "\n"):
            print "No changes to make"
            return
        edit_form.set_value(name="text", value=new_contents)
        edit_form.set_value(name="comment", value=comment)
        request = edit_form.click(name="save")
        response = self.browser.open(request)
        response_text = response.read()
        if "Your changes have been saved" not in response_text:
            #print "Previous content: '%s'" % old_contents
            #print "Attempted new content: '%s'" % new_contents
            raise Exception("error writing page")
        
    def _get_form_id(self, form):
        try:
            return form.attrs["id"]
        except KeyError:
            return None

    def _find_edit_form(self, forms):
        matching_forms = filter(
            lambda form: self._get_form_id(form) == "edit", 
            forms)
        assert(len(matching_forms) == 1)
        return matching_forms[0]


if __name__ == '__main__':
    c = TracWikiClient()
    content = c.get_page("TestPage")
    print content
    c.write_page("TestPage", """supercalifragilistic
{{{
   1 & 2 + 3 blah... // etc etc
}}}
expialidocious
""", comment="testing editing trac wiki from Python")

