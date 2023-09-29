#!/bin/bash
# Script sends HTTP GET request to a URL and display size of the response body
echo -n curl -s "$1" | wc -c
