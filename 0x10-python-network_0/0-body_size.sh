#!/bin/bash
# Script that sends a request to a URL and displays the size of the response
curl -sI "$1" | grep Content-Length | cut -d " " -f 2
