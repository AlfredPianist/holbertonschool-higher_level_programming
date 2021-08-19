#!/bin/bash
# Script that prints the status code from an URL
curl -so /dev/null -sw "%{http_code}" "$1"
