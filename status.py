#!/usr/bin/env python
# TBR Services Knocker
# Copyright 2015 Simon Sickle <simon@simonsickle.com>
# Licensed under GNUv3
# You may obtain a copy of this license online

# Import modules to make life easier
import socket
import requests

# Get HTTP status code
def getHttpStatus(host):
    try:
        r = requests.head(host)
        return(r.status_code)
    except requests.ConnectionError:
        return 0

# Get UDP Port Status
def getUdpStatus(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    result = sock.connect_ex((host,port))
    if (result == 0):
        return 1
    return 0

# Get TCP Port Status
def getTcpStatus(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host,port))
    if (result == 0):
        return 1
    return 0


# Print out JSON
print '{'
print '"webserver": { "ssh": "%s", "http": "%s" },' % (getUdpStatus("server2.teamblueridge.org",22),
                                                     getHttpStatus("https://teamblueridge.org"))
print '"gerrit": { "ssh": "%s", "http": "%s" },' % (getUdpStatus("review.teamblueridge.org",29418),
                                                   getHttpStatus("https://review.teamblueridge.org"))
print '"buildbox": { "ssh": "%s" },' % getUdpStatus("server1.teamblueridge.org",22)
print '"jenkins": { "http": "%s" },' % getHttpStatus("https://jenkins.teamblueridge.org")
print '"jira": { "http": "%s" },' % getHttpStatus("https://jira.teamblueridge.org")
print '"stash": { "http": "%s" },' % getHttpStatus("https://stash.teamblueridge.org")
print '"status": { "http": "%s" },' % getHttpStatus("https://status.teamblueridge.org")
print '"paste": { "http": "%s" }' % getHttpStatus("https://paste.teamblueridge.org")
print '}'
