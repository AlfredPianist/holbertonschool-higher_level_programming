#!/bin/bash
# Script that sends a POST request with some information
curl -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
