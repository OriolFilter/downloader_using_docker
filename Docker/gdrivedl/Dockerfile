# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM python:3.9.6-buster

## ***
#
# Working folder
ARG WK="/folder"

LABEL version='1.0'
LABEL description="Customized Dockerfile for python-3.9.6 buster with gdrive library installed"
LABEL org.opencontainers.image.authors='filter.oriol@gmail.com'
LABEL py_packages_installed=""

WORKDIR ${WK}
ADD main.py ${WK}
ADD requirements.txt ${WK}
ADD "${PKGFOLDER}/${PKGTAR}" ${WK}
# Install requirements for python
RUN pip install -r requirements.txt

RUN chmod +x main.py
# Download, untar and install megatools to the system

#USER 1000:1000
# Change workdir to the download folder
WORKDIR /downloads
ENTRYPOINT ["{WK}/main.py"]
