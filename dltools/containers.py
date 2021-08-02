from os import getcwd
from typing import Union
from urllib.parse import urlparse


# Pending, probably never happening
# import getpass
# class user():
#     user:str=getpass
#     user:str=getpass

class Credentials:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    username = None
    password = None


class BaseContainer:
    """
    Base class for all containers
    """

    def __init__(self, credentials: Credentials = Credentials(username=None, password=None), url: str = None,
                 destination: str = getcwd()) -> None:
        """
        Introduces the default configuration values
        """
        pass

    def start(self) -> None:
        """
        Start download function
        """
        pass

    def kill(self) -> None:
        """
        KILLS the current process
        how? don't know yet
+       """
        pass

    def wait(self) -> None:
        """
        Waits the work to end.
        :return:
        """
        pass

    _container: str = None

    url: str = None
    destination: str = None

    job = None  # To store the function job locally

    container: str = None  # Container used to download the files

    credentials: Credentials = None
    # Unsure how to implement permissions + user, user could be implemented using the container user thing, but that
    # means I need to add a user to the container.


class Megadl(BaseContainer):
    def __init__(self, credentials: Credentials = Credentials(username=None, password=None), url: str = None,
                 destination: str = getcwd()) -> None:
        super().__init__(credentials, url, destination)
        self.container = "oriolfilter/megadl:1.0"


def manager(credentials: Credentials, url: str = None, destination: str = getcwd()) -> BaseContainer or bool:
    """
    Returns a container object based in the url given
    """
    " ** stuff ** "
    domain_Dict: dict = {'mega.nz': Megadl}
    domain: str = urlparse(url).netloc
    container = domain_Dict[domain]
    if container:
        return container(credentials, url, destination)
    print("Couldn't find any container for your URL given, in that case submit a petition for the administrator of "
          "the package")
    return False




if __name__ == "__main__":
    print('Called from main?')
