#!/bin/bash
# This script uses curl to make a request to 0.0.0.0:5000/catch_me and captures the response in a file.
curl -s -L -X PUT 0.0.0.0:5000/catch_me
