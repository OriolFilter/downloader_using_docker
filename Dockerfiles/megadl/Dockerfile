# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/
FROM alpine:3.14.0

## Megatools arguments used to download, untar and install the package
# Megatools package folder file
ARG PKGPATH="https://megatools.megous.com/builds"
# Megatools package file name args
ARG PKGNAME="megatools-1.10.3"
# Megatools package tar file name args
ARG PKGTAR="${PKGNAME}.tar.gz"

# Working folder
ARG WK="/folder"

LABEL version='1.0'
LABEL description="Customized Dockerfile for alpine-3.14.0 with megatools installed"
LABEL org.opencontainers.image.authors='filter.oriol@gmail.com'
#LABEL py_packages_installed="sh colored"
LABEL megatools_version="1.10.0"
LABEL megatools_package="https://megatools.megous.com/builds/"
LABEL megatools_used_package="${PKGPATH}/${PKGTAR}"

RUN apk upgrade --update-cache --available && apk add --no-cache tar asciidoc gcc make g++ zlib-dev glib-dev libressl-dev curl-dev
#RUN apt-get update && apt-get install -y asciidoc && apt-get clean
#    &&

WORKDIR ${WK}
ADD "${PKGPATH}/${PKGTAR}" ${WK}
# Install requirements for python

# Download, untar and install megatools to the system

RUN tar --version
RUN /usr/bin/tar xzvf ${PKGTAR} --transform s/${PKGNAME}/megatools/ && \
    cd megatools && \
    ./configure && make && make install && cd .. && rm -rf megatools && rm -rf ${PKGTAR}

# Change workdir to the download folder
WORKDIR /downloads
ENTRYPOINT ["/usr/local/bin/megadl"]
