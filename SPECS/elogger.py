#!/home/builderdev/venv-with-mechanize/bin/python

import sys
import os
import mechanize
import ConfigParser


"""
Script to create an elog messages describing various events connected with 
JAP development.
"""

class Elogger(object):


    def __init__(self, config_file):
        self.config = self.get_config(config_file)
        self.browser = mechanize.Browser()


    def select_item(self, prefix, name):
        """
        Select (first) item with specified name amongst controls 
        beginning with prefix
        """
        controls = self.get_controls(prefix)
        item = self.get_item(controls, name)
        item.selected = True


    def get_item(self, controls, name):
        "Get (first) item with specified name in list of controls"
        for control in controls:
            for item in control.items:
                if item.name == name:
                    return item
        raise ValueError


    def get_controls(self, prefix):
        """
        Get list of controls with names that start with prefix
        """
        return [control for control in self.browser.controls 
                if hasattr(control, 'name')
                and isinstance(control.name, unicode) 
                and control.name.startswith(prefix)]


    def fill_text(self, prefix, value):
        """
        Fill (the only) text box whose name starts with prefix
        """
        control, = self.get_controls(prefix)
        control.value = value


    def elog(self, 
             subject, text, machine,
             category='Software',
             criticality='Normal',
             team='CEDAAdminsTeam',
             suppress=False,
             ):
        """
        Create an elog message (generic)
        """

        url = self.config.get('elog', 'url') + '?cmd=New'
        username = self.config.get('elog', 'username')
        password = self.config.get('elog', 'password')
        
        self.browser.open(url)

        self.browser.select_form(name='form1')
        self.browser.form['uname'] = username
        self.browser.form['upassword'] = password

        self.browser.submit()
        self.browser.select_form(name='form1')

        self.select_item('Team', team)
        self.select_item('Category', category)
        self.select_item('Criticality', criticality)

        self.fill_text('Affected_service', machine)
        self.fill_text('Subject', subject)
        self.fill_text('Text', text)

        if suppress:
            self.select_item('suppress', '1')

        print "-------- MESSAGE TO BE ELOGGED --------"
        print 'subject:', subject
        print 'text:', text
        print "---------------------------------------"

        if raw_input("really submit elog? ").lower().startswith("y"):
            self.browser.submit()
            print "submitted"
        else:
            print "aborted"


    def get_config(self, config_file):

        config = ConfigParser.ConfigParser()
        config.read(config_file)
        return config


    def elog_install(self, machine, rpm_list, uninstall=False):
        """
        Create an elog message with list of RPMs
        """
        comma_sep = ', '.join(rpm_list)
        enter_sep = '\n'.join(rpm_list)
        op = 'uninstalled' if uninstall else 'installed'

        subject = '{}: {} locally {}'.format(machine, comma_sep, op)

        text = """
The following package(s) were locally {} on {}.
{}

This is part of JAP development and testing.
""".format(op, machine, enter_sep)
        
        self.elog(subject, text, machine)


    def elog_update_repo(self, machine):
        """
        Create an elog message saying that the repo was updated.
        """
        subject = '{}: yum repo updated'.format(machine)
        text = """
RPMs were added to the yum repository on {} and the createrepo script was run to update the repo metadata.

This is part of JAP publication.
""".format(machine)
        self.elog(subject, text, machine)
        

def main():

    args = sys.argv[1:]
    conf_file = os.path.join(os.getenv('HOME'), '.elog_conf')
    elogger = Elogger(conf_file)

    if args[0] == '-i':
        machine = args[1]
        packages = args[2:]
        elogger.elog_install(machine, packages)

    elif args[0] == '-u':
        machine = args[1]
        packages = args[2:]
        elogger.elog_install(machine, packages, uninstall=True)

    elif args[0] == '-r':
        machine, = args[1:]
        elogger.elog_update_repo(machine)

    else:
        print "check usage"


if __name__ == '__main__':
    main()
