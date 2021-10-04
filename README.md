### Installation

#### Library installation
```shell
pip install -r ./dltools/requirements.txt
pip install ./lib/dltools
```
#### Script installation
```
Some of this commands might requeire access to the root user/sudo command 
```
First step is to create a system link or move/copy the script file to the installation folder.

##### Only current user installation

```shell
ln -s manager.py ~/.local/autodown
```

##### All system installation

```shell
sudo mv manager.py /usr/bin/autodown
```

##### Make the script executable

Depending on the path used before, pick one of the both options

```shell
chmod +x ~/.local/autodown
```

or

```shell
sudo chmod +x /usr/bin/autodown
```

#### Usage

#### Library

The basic usage would be setting the url.
By default, if we don't give a destination, will use the current folder we are located.
If we don't pass a user object (which contains the permissions), will get the permissions from the folder we are using as a destination.

Finally, start the download
```python
from dltools.Containers import Manager
obj = Manager(url=linkobj.url,
              destination=linkobj.destination,
              containerUser=ContainerUser(uid=stat(linkobj.destination).st_uid,
                                          gid=stat(linkobj.destination).st_gid)
              )
obj.start()
```

##### Docker

(yet here we are only using the docker container)

docker container run -v ${FOLDER}:/downloads oriolfilter/megadl:1.0 "${URL}"

##### Script

The function of the script, is searching recursively files called "link", 
which are supposed to contain the url for the files to download. 

Once we have installed the script, we can call it with the name we used.
In our case we used "autodown"

```sh
autodown
```

##### Test

- https://mega.nz/folder/GgMH3I4C#nM_NsEidSRurANbNUezo3w

Try to use the next url (first open the link in the url to check it still exists):
###### Example script

First we create a file called "link" somewhere inside our current directory.

Finally we execute the script.

```shell
autodown
```

###### Example bash/docker

```
docker container run -v $(pwd):/downloads oriolfilter/megadl:1.0 'https://mega.nz/folder/GgMH3I4C#nM_NsEidSRurANbNUezo3w'
```

### Known Bugs

- If the folder contains the colon symbol ':' it won't be able to execute the command creating the docker container