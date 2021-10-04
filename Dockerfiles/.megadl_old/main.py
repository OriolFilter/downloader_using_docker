#!/usr/bin/env python3
### File in the docker machine that will download the files
from colored import fore, style
from sh import megadl, ErrorReturnCode
from sys import argv

def clean_line(line):
    if not line:
        return None
    elif str.encode(line).rfind(b'\x1b[0K') != -1:
        return clean_line(bytes.decode(str.encode(line)[str.encode(line).find(b'\x1b[0K')+4:]))
    elif str.encode(line) == str.encode('\r'):
        return None
    elif str.encode(line)[0] == 13:
        return None
    elif str.encode(line) == str.encode('\r\n'):
        return None
    elif str.encode(line)[-1:] == str.encode('\n'):
        return line[:-1]
    else:
        return line


def output(line):
    txt = clean_line(line)
    if txt:
        print(f'{fore.GREEN_3A}[{fore.BLUE}MESSAGE{fore.GREEN_3A}]{style.RESET} {txt}')


def err(line):
    txt = clean_line(line)
    if txt: print(f'{fore.GREEN_3A}[{fore.RED}ERROR{fore.GREEN_3A}]{style.RESET} {txt}')


args_list: list = argv[1:]
if len(args_list) > 0:
    for link in args_list:
        try:
            megadl(link, _err=err, _out=output)
        except ErrorReturnCode:
            pass
else:
    print("No mega links (arguments) given")
