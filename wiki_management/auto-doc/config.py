# top-level package(s) from which we follow dependencies, auto-documenting
top_level_packages = ["jasmin-sci-vm"]

# directory(/-ies) that may contain RPMs that we auto-document
package_dirs = ["/datacentre/opshome/dist/htdocs/yumrepo/RPMS/"]

# list of packages from which we document dependencies outside
# this repository (without further recursion)
show_nonlocal_deps_for = ["jasmin-sci-vm", "jasmin-common-vm"]

# cache directory for RPMs from external repositories
cache_dir = "/home/jap/auto-doc/cache"

# how to run the yumdownloader
# needs to be run as root to access RHN repo.  Options are to use sudo,
# possibly ssh root@localhost, or just to run the top-level script as root
# and then not need anything special
yumdownloader_command = "sudo yumdownloader"

# whether to attempt download every time (though may still not download if
# yumdownloader says that correct file already exists) - if False then won't
# even attempt download if file exists with expected filename (from running
# yumdownloader --urls)
try_download_every_time = False

# wiki editing stuff
wiki_top_url = "http://proj.badc.rl.ac.uk/cedaservices/"
wiki_page = "JASMIN/AnalysisPlatform/Packages"
wiki_creds_file = "/home/jap/.wiki_auth"
wiki_token_1 = "__start_of_automated_list__"
wiki_token_2 = "__end_of_automated_list__"
