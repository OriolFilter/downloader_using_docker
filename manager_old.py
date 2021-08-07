#!/usr/bin/env python3
## File that will call the downloader

# https://www.codespeedy.com/check-if-a-string-is-a-valid-url-or-not-in-python/

from validators import url as vurl
from os.path import dirname
from sh import docker, ErrorReturnCode
from os import getcwd
from glob import glob
from colored import fore, style


def clean_line(line):
    if not line:
        return None
    elif str.encode(line).rfind(b'\x1b[0K') != -1:
        return clean_line(bytes.decode(str.encode(line)[str.encode(line).find(b'\x1b[0K')+4:]))
    elif str.encode(line) == str.encode('\r'):
        return None
    elif str.encode(line)[0] == 13:  # \r
        return None
    elif str.encode(line) == str.encode('\r\n'):
        return None
    elif str.encode(line)[-1:] == str.encode('\n'):
        return line[:-1]
    else:
        return line

def output(line):
    # print(f'>> {str.encode(line)}')
    txt = clean_line(line)
    if txt:
        print(f'{fore.GREEN_3A}[{fore.BLUE}DOCKER{fore.GREEN_3A}]{style.RESET} {txt}')


def err(line):
    txt = clean_line(line)
    if txt: print(f'{fore.GREEN_3A}[{fore.RED}ERROR{fore.GREEN_3A}]{style.RESET} {txt}')


class LINKOBJ:
    def __init__(self, url, destination):
        self.url = url
        self.destination = destination

    url: str = None
    destination: str = None


keyword = "link"
# file_list: list[str] = []
link_list: list[LINKOBJ] = []

# Will search the files with the word "file" in the current directory (and recursive), then proceed to call the docker
# downloader and maybe (only maybe, uncompress it afterwards)
file_list: list[str] = glob(f'{getcwd()}/**/{keyword}', recursive=True)

for file in file_list:
    with open(file, 'r') as f:
        line: str
        for line in f.read().split(
                '\n'):  # Each line represents to have a url, if doesn't pass the validation process it's discarded
            if vurl(line):
                link_list.append(LINKOBJ(url=line, destination=dirname(file)))
# for url in link_list:
#     print(f'>> {url}')

if len(link_list) > 0:
    for linkobj in link_list:
        linkobj: LINKOBJ
        try:
            docker.run('-t', '--volume', f'{linkobj.destination}:/downloads:rw', 'megadl', linkobj.url, _err=err,
                       _out=output, _bg=True)
        except ErrorReturnCode as e: pass
else:
    print("No files and or links found inside the files")
