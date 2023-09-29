#!/bin/bash
# This script sends a JSON POST request to a URL with the contents of a file in the request body.
curl -s -X POST -H "Content-Type: application/json" --data-binary "@$2" "$1"
