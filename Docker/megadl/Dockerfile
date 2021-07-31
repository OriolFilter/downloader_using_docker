# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM python:3.9.6-buster

## Megatools arguments used to download, untar and install the package
# Megatools package folder file
ARG PKGFOLDER="https://megatools.megous.com/builds"
# Megatools package file name args
ARG PKGNAME="megatools-1.10.3"
# Megatools package tar file name args
ARG PKGTAR="${PKGNAME}.tar.gz"

# Working folder
ARG WK="/folder"

LABEL version='1.0'
LABEL description="Customized Dockerfile for python-3.9.6 buster"
LABEL org.opencontainers.image.authors='filter.oriol@gmail.com'
LABEL py_packages_installed="sh colored"
LABEL megatools_version="1.10.0"
LABEL megatools_package="https://megatools.megous.com/builds/"
LABEL megatools_used_package="${PKGFOLDER}/${PKGTAR}"

RUN apt-get update && apt-get install -y asciidoc && apt-get clean
#    &&

WORKDIR ${WK}
ADD main.py ${WK}
ADD requirements.txt ${WK}
ADD "${PKGFOLDER}/${PKGTAR}" ${WK}
# Install requirements for python
RUN pip install -r requirements.txt

# Download, untar and install megatools to the system

RUN /bin/tar xzvf ${PKGTAR} --transform s/${PKGNAME}/megatools/ && \
    cd megatools && \
    ./configure && make && make install && cd .. && rm -rf megatools && chmod +x main.py && ln -s ${WK}/main.py /usr/bin/dlmanager

USER 1000:1000
# Change workdir to the download folder
WORKDIR /downloads
ENTRYPOINT ["/usr/bin/dlmanager"]
