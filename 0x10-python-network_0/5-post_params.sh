#!/bin/bash
# This script sends an HTTP POST request to a URL with specified variables and displays the response body.
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
