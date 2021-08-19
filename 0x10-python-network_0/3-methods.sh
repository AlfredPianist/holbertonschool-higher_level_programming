#!/bin/bash
# Script that displays all methods accepted by the sweb server
curl -sI "$1" | grep Allow | cut -d " " -f 2-
