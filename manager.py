#!/usr/bin/env python3
## File that will call the downloader

# https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/

from validators import url as vurl
from os.path import dirname
from os import getcwd
from glob import glob
from dltools.containers import manager, ErrorDuringContainerExecution, CannotRunTheContainer


class LINKOBJ:
    def __init__(self, url, destination):
        self.url = url
        self.destination = destination

    url: str = None
    destination: str = None


keyword = "link"
# file_list: list[str] = []
# link_list: list[LINKOBJ] = []
link_list: list = []

# Will search the files with the word "file" in the current directory (and recursive), then proceed to call the docker
# downloader and maybe (only maybe, uncompress it afterwards)

file_list: list[str] = glob(f'{getcwd()}/**/{keyword}', recursive=True)

for file in file_list:
    with open(file, 'r') as f:
        line: str
        for line in f.read().split('\n'):  # Each line represents to have a url, if doesn't pass the validation process it's discarded
            if vurl(line):
                link_list.append(LINKOBJ(url=line, destination=dirname(file)))

if len(link_list) > 0:
    for linkobj in link_list:
        linkobj: LINKOBJ
        try:

            download = manager(url=linkobj.url,
                               destination=linkobj.destination,
                               _bg=False)
            download.start()

        except Exception as e:
            print(f'Error downloading url: {linkobj.url}')
            print(f'Error: {e}')
            # Logs the error appropriately.
else:
    print("No files and or links found inside the files")