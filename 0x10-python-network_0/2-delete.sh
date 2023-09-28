#!/bin/bash
# This script sends an HTTP DELETE request to a URL and displays the response body.

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Get the URL from the command line argument
url="$1"

# Send an HTTP DELETE request to the URL using curl and display the response body
response=$(curl -s -X DELETE "$url")

# Display the response body
echo "$response"
