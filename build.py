from os import system
from sh import docker
from dltools.containers import BaseContainersRepo, CustomContainerNames
from getpass import getuser

build_list = [BaseContainersRepo.megadl]
custom_build_list = [CustomContainerNames.megadl]


class USER:
    def __init__(self, uname=None, gname=None, uid=None, gid=None):
        self.uname = uname or self.uname
        self.gname = gname or self.gname
        self.uid = uid or self.uid
        self.gid = gid or self.gid

    uname: str = 'containeruser'
    gname: list = 'containeruser'
    uid: int = 1000
    gid: int = 1000


def eof(OGcontainer: str, USER: USER = USER):
    """
    Returns a EOF input that will be used during docker build command
    :param USER:
    :param OGcontainer:
    :return:
    """

    txt = f"EOF\n" \
          f"FROM {OGcontainer}\n" \
          f"USER root:root\n" \
          f"RUN addgroup --gid {USER.gid} {USER.gname} && adduser -u {USER.uid} -G {USER.gname} -D {USER.uname}\n" \
          f"USER {USER.uname}:{USER.gname}\n" \
          f"EOF"
    return txt


own_user = USER(uname=None, gname=None)

for repo, tag in zip(build_list, custom_build_list):
    system(f"docker build -t {tag} -<< {eof(USER=own_user, OGcontainer=repo)}")
    # It's ugly, didn't managed to pass EOF using sh library
    # docker.build('-t', tag, '-', _in=eof(USER=own_user, OGcontainer=repo))

"""
docker build -t test 
"""

"""
docker build -t test  -<<
FROM nginx:latest
USER test:test"
EOF
"""

"""
docker build -t custom/megadl -<< EOF
FROM {OGcontainer}
RUN groupadd -g ${USER.gid} ${USER.gname} && useradd -u ${USER.uid} -g ${USER.gname}  ${USER.uname}
USER {USER.uname}:{USER.gname}
EOF
"""
