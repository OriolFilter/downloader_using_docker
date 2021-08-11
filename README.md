#### containers.py

- [x] Allow downloading Mega files.
- [ ] Allow downloading Google Drive.
- [ ] Allow downloading Mediafire
- [x] Create classes for each system/downloader used.
    - [x] Mega
    - [ ] Google Drive
    - [ ] Mediafire

- [x] Create a library

[comment]: <> (- [ ] Change its name to find_in_files.py or something like that, and update manager.py to use the library created.)
- [ ] Add error handling for packages not installed
- [ ] Add an Exceptions.py


#### manager.py

- [x] By default uses megadl and no longer uses a python script
- [x] Upload conainer to dockerhub

##### Exceptions.py

- [ ] Errors pass the sh command error so it maintains its content
  
[comment]: <> (- [ ] Allow passing command arguments to modify its behaviour)


#### To Do

- [ ] Comment/Document
- [ ] Dockerfile, useradd custom user (this one should be easy tho)
- [ ] Add support for Google Drive

#### Dockerfiles

- [x] Megadl
- [x] Google Drive
- [ ] Discord bot to download files

##### Automate building custom images