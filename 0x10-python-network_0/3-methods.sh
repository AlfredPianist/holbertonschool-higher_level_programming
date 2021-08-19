#!/bin/bash
# Script that displays all methods accepted by the web server
curl -sI "$1" | grep Allow | cut -d " " -f 2-
