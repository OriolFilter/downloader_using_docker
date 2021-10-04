#!/usr/bin/env python3
from validators import url as vurl
from os.path import dirname
from os import getcwd, stat
from getpass import getuser
from glob import glob
from dltools.Containers import Manager, ContainerUser
from dltools.Exceptions import ErrorDuringContainerExecution, CannotRunTheContainer


class LINKOBJ:
    """ Stores url and destination from each mega link"""

    def __init__(self, url:str, destination:str):
        self.url = url
        self.destination = destination

    url: str = None
    destination: str = None


keyword = "link"
link_list: list = []

# Will search the files with the word "file" in the current directory (and recursive), then proceed to call the docker
# downloader and maybe (only maybe, uncompress it afterwards)

# Finds all files named ${keyword}
file_list: list = glob(f'{getcwd()}/**/{keyword}', recursive=True)

for file in file_list:
    # For each element in @file_list will start a docker container
    with open(file, 'r') as f:
        line: str
        for line in f.read().split(
                '\n'):  # Each line represents to have a url, if doesn't pass the validation process it's discarded
            if vurl(line):
                link_list.append(LINKOBJ(url=line, destination=dirname(file)))

if len(link_list) > 0:
    for linkobj in link_list:
        linkobj: LINKOBJ
        try:
            """ Calls the manager and passes the arguments """
            download = Manager(url=linkobj.url, containerUser=ContainerUser(uid=stat(linkobj.destination).st_uid,
                                                                            gid=stat(linkobj.destination).st_gid),
                               destination=linkobj.destination,
                               _bg=False)
            download.start()

        except Exception as e:
            print(f'Error downloading url: {linkobj.url}')
            if len(str(e)) > 0:
                print(f'Error: {e}')
else:
    print("No files and or links found inside the files")
