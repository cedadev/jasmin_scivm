"""
Test ipython features.

"""

from unittest import TestCase

import subprocess as S


class TestInvokeIpython(TestCase):
    def setUp(self):
        #!TODO: should probably create an isolated profile
        pass

    def testNotebook(self):
        #!TODO: fully test starting the notebook
        pass
    testNotebook.__test__ = False

    def testNotebookAppImport(self):
        try:
            import IPython.html.notebookapp
        except ImportError:
            self.fail('Importing notebookapp fails')
