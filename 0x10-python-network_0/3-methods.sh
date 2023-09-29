#!/bin/bash
# This script sends an HTTP HEAD request to a URL and displays the allowed HTTP methods.
curl -sI "$1" | grep -i 'Allow' | cut -d ' ' -f 2-
