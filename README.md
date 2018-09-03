# Pacifica Python Downloader
[![Build Status](https://travis-ci.org/pacifica/pacifica-python-downloader.svg?branch=master)](https://travis-ci.org/pacifica/pacifica-python-downloader)
[![Build Status](https://ci.appveyor.com/api/projects/status/38dmnpbm398cvtu9?svg=true)](https://ci.appveyor.com/project/dmlb2000/pacifica-python-downloader)
[![Test Coverage](https://api.codeclimate.com/v1/badges/e0d5aaf99dd05f3485d6/test_coverage)](https://codeclimate.com/github/pacifica/pacifica-python-downloader/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/e0d5aaf99dd05f3485d6/maintainability)](https://codeclimate.com/github/pacifica/pacifica-python-downloader/maintainability)

Pacifica Python Library for Downloading Data

This repository provides a library so python applications can
download data from Pacifica.

## Downloader API

The entrypoint for this library is the `Downloader` class in 
the `downloader` module. Instances of this class are created
with a download directory and a 
[Pacifica Cartd](https://github.com/pacifica/pacifica-cartd)
endpoint url.

### Downloader Class

The [constructor](pacifica/downloader/downloader.py#16) takes
two arguments `location` and `cart_api_url`. The `location` is
a download directory to be created by a download method. The
`cart_api_url` is the endpoint for creating carts.

The other methods in the `Downloader` class are the supported
download methods. Each method takes appropriate input for that
method and the method will download the data to the location
defined in the constructor.

[CloudEvents](https://github.com/cloudevents/spec) is a
standard for how to send messages between services in cloud
environments. The `cloudevent()` method 
([here](pacifica/downloader/downloader.py#45))
consumes the event emitted by the
[Pacifica Notifications](https://github.com/pacifica/pacifica-notifications)
service and downloads the data.

## Internal Classes and Methods

