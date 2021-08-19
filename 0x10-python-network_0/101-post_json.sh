#!/bin/bash
# Script that sends a POST request with some information
curl -H "Content-Type: application/json" -X POST -d @"$2" "$1"
