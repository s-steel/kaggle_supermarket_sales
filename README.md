# Supermarket Sales

<!--
[![Build Status](https://travis-ci.com/travis-ci/travis-web.svg?branch=main)](https://travis-ci.com/github/2008-Untangled/Music-Service-API)
-->

  <h3 align="center">Supermarket Sales</h3>

  <p align="center">
    WIP - details to be added
  </p>
</p>

### Table of Contents

1. [About This Project](#about-this-project)
1. [Virtual Environment setup](#virtual-environment-setup)
1. [Testing](#testing)
1. [Contributing](#contributing)

## About This Project
Visit [Untangled](https://github.com/2008-Untangled) to view all the repositories associated with this application.

This microservice allows you to query a song name and receive a response that includes the song name, artist name, album name, album release date, and a url for that song on spotify.  It takes in the song name query, then consumes the [Spotify API](https://developer.spotify.com/documentation/web-api/) to get information about that song.  The relevant information for that song is then extracted and compiled, and then returned in the microservice response.   

## Virtual Environment setup

```bash
# build a virtual environment to install your Python packages
python3 -m venv ./venv

# 'activate' the virtual environment for your project
# do this every time you start a new terminal and enter your project folder
source venv/bin/activate

# install your Python packages
pip3 install -r requirements.txt
```

To shut off your virtual environment, run `deactivate` at a terminal where you
have an active virtual environment.