from os import getcwd
from typing import Union
from urllib.parse import urlparse

import sh
from sh import docker, ErrorReturnCode, ErrorReturnCode_125

ErrorReturnCode_125: ErrorReturnCode

from colored import fore, style


class UnregisteredDomain(Exception):
    """
    Raises when the domain gives isn't registred.

    In case of having this error, consider contacting the administrator and providing the link that returns error in
    order to update the list and/or add new methods
    """
    pass


class CannotRunTheContainer(Exception):
    """
    For some reason wasn't able to start the docker container, it might be due not being able to access the container
    (maybe due too many requests to DockerHub) or docker service isn't running
    """
    pass


# Pending, probably never happening
# import getpass
# class user():
#     user:str=getpass
#     user:str=getpass


class Credentials:
    """
    Used to log in in services like mega or google drive (not implemented so far)
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    username = None
    password = None


class BaseContainer:
    """
    Base class for all containers
    """

    def __init__(self, url: str, destination: str = getcwd(),
                 credentials: Credentials = Credentials(username=None, password=None), _err=None,
                 _out=None, _bg=False, _done=None) -> None:
        """
        Introduces the default configuration values
        """
        self.credentials = credentials
        self.url = url
        self.destination = destination
        self._err = _err or self._err
        self._out = _out or self._out
        self._bg = _bg
        self.done = False

    def start(self) -> None:
        """
        Start download container process
        """
        # self.job = docker.run('-t', '--volume', f'{self.destination}:/downloads:rw', self.container, self.url,
        #                                   _err=self._err,
        #                                   _out=self._out,
        #                                   # _done=self._done
        #                                   # _bg=self._bg
        #                                   )
        try:
            print(self._container)
            self.job = docker.run('-t', ('', f'--entrypoint {self._entrypoint}'), '--volume',
                                  f'{self.destination}:/downloads:rw',
                                  self._container, self.url,
                                  _err=self._err,
                                  _out=self._out,
                                  _done=self._done,
                                  _bg=self._bg
                                  )
        except ErrorReturnCode_125 as e:
            print("Docker not running or not accessible")
            # raise CannotRunTheContainer("hi")

    def kill(self) -> None:
        """
        KILLS the current process, used in case of running the process in the background
+       """
        self.job.kill()

    def wait(self) -> None:
        """
        Brings the background process to the foreground
        :return:
        """
        self.job.wait()

    def out(self, line):
        self._out(self.clear_line(line))

    def err(self, line):
        self._err(self.clear_line(line))

    def clear_line(self, line):
        if not line:
            return None
        elif str.encode(line).rfind(b'\x1b[0K') != -1:
            return self.clear_line(bytes.decode(str.encode(line)[str.encode(line).find(b'\x1b[0K') + 4:]))
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

    def print_out(self, line) -> None:
        txt = self.clear_line(line)
        if txt:
            print(f'{fore.GREEN_3A}[{fore.BLUE}DOCKER{fore.GREEN_3A}]{style.RESET} {txt}')

    def print_err(self, line) -> None:
        txt = self.clear_line(line)
        if txt:
            print(f'{fore.GREEN_3A}[{fore.RED}ERROR{fore.GREEN_3A}]{style.RESET} {txt}')

    def on_done(self, *args, **kwargs) -> None:
        self.done = True

    _container: str = None  # Docker container name
    _entrypoint: str = None  # Command used as entrypoint for the docker container

    url: str = None
    destination: str = None

    job: docker.run = None  # To store the function job locally

    done: bool = None

    credentials: Credentials = None

    _bg = False
    _err = print_err
    _out = print_out
    _done = on_done

    # Unsure how to implement permissions + user, user could be implemented using the container user thing, but that
    # means I need to add a user to the container.


class Mega(BaseContainer):
    def __init__(self, url: str, destination: str = getcwd(),
                 credentials: Credentials = Credentials(username=None, password=None), _err=None,
                 _out=None, _bg=False, _done=None) -> None:
        super().__init__(url=url, destination=destination, credentials=credentials, _err=_err, _out=_out, _done=_done,
                         _bg=_bg)
        # self._container = "tb"
        self._container = "oriolfilter/megadl:1.0"
        self._entrypoint = "/usr/local/bin/megadl"


def manager(url: str, destination: str = getcwd(),
            credentials: Credentials = Credentials(username=None, password=None), _err=None,
            _out=None, _bg=False, _done=None) -> BaseContainer:
    """
    Returns a container object based in the url given

    If the domain url isn't registered it raises up an Exception
    """
    " ** stuff ** "
    domain_dict: dict = {'mega.nz': Mega}
    domain: str = urlparse(url).netloc
    if domain in domain_dict:
        return domain_dict[domain](url=url, destination=destination, credentials=credentials, _err=_err, _out=_out,
                                   _bg=_bg, _done=_done)
    else:
        raise UnregisteredDomain


if __name__ == "__main__":
    print('Called from main?')
