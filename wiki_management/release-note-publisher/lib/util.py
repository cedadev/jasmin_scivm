import sys

def call_verbose(description, verbose, function, *args, **kwargs):
    if verbose:
        print ("%s... " % description),
        sys.stdout.flush()
    retval = function(*args, **kwargs)
    if verbose:
        print "done"
        sys.stdout.flush()
    return retval
