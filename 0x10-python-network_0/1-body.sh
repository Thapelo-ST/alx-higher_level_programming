#!/bin/bash
# This script sends an HTTP GET request to a URL and displays the response body.
# curl -s "$1"
curl -s -o /dev/null -w "%{http_code}" "$1" | curl -s "$1"
