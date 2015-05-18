import os
from git import Repo

class GithubWikiClient:

    def __init__(self, creds_file = "/home/jap/.github_auth", path="cedadev/jasmin_scivm", local_path = "/tmp/wiki"):
        username, password = self._read_creds_file(creds_file)
        url = self._make_url(username, password, path)        
        self.url = url
        self.local_path = local_path
        if os.path.exists(local_path):
            self.repo = Repo(local_path)
        else:
            self.repo = Repo.clone_from(url, local_path)
        self.origin = self.repo.remote("origin")
        self._check_url()

    def _read_creds_file(self, creds_file):
        f = open(creds_file)
        username = f.readline().replace("\n", "")
        password = f.readline().replace("\n", "")
        f.close()
        return username, password

    def _make_url(self, username, password, path):
        return "https://%s:%s@github.com/%s.wiki.git" % (username, password, path)

    def _get_url(self):
        return self.origin.config_reader.get("url")

    def _check_url(self):
        url_found = self._get_url()
        if self.url != url_found:
            raise Exception("repo at %s is clone of %s, not %s" % (self.local_path, url_found, self.url))

    def _read_file(self, path):
        f = open(path)
        s = f.read()
        f.close()
        return s

    def _write_file(self, path, content):
        f = open(path, "w")
        f.write(content)
        f.close()

    def _page_rel_path(self, page_name):
        return "%s.md" % page_name

    def _page_path(self, page_name):
        return os.path.join(self.local_path, self._page_rel_path(page_name))

    def read_page(self, page_name):
        self.origin.pull()
        page_path = self._page_path(page_name)
        return self._read_file(page_path)

    def write_page(self, page_name, content, message="automated edit"):
        page_path = self._page_path(page_name)
        self._write_file(page_path, content)
        git = self.repo.git
        git.add(self._page_rel_path(page_name))
        git.commit(m = message)
        self.origin.push()

if __name__ == '__main__':
    
    gwc = GithubWikiClient()
    page = "test-page"
    content = gwc.read_page(page)
    content += "\nhere we add another line\n"
    gwc.write_page(page, content)
