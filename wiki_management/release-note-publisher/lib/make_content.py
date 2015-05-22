import string

import config

"""
misc routines to generate content of email and the wiki page
"""

def markup_release_notes(releases):
    """
    return a string with concatenated marked-up release notes for the 
    supplied list of releases
    """
    return string.join(map(lambda release: markup_release_note(release),
                           releases),
                       "\n")


def markup_release_note(release,
                        heading_markup = config.wiki_heading_markup):
    return (heading_markup % ("Version %s (install date %s)" % 
                              (release.version, release.install_date)) 
            + "\n\n" + release.contents)


def compose_email(future_releases,
                  template_file = config.email_contents_file):
    """
    returns a string containing full text (headers and body) of email 
    to be sent
    """
    # probably there will only be one future release, but if there is more 
    # than one, then list them chronologically, and the version and 
    future_releases.sort()
    next_release = future_releases[0]
    next_version = next_release.version
    next_date = next_release.install_date.strftime("%A %d %B, %Y")
    release_notes = markup_release_notes(future_releases)
    email_template = ""
    f = open(template_file)
    for line in f.xreadlines():
        if not line.startswith("%#"):
            email_template += line
    f.close()
    email_content = (email_template
                     .replace("%V", next_version)
                     .replace("%D", next_date)
                     .replace("%N", release_notes))
    return email_content
