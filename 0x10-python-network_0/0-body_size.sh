#!/bin/bash

# Read the URL from the command line argument
URL=$1

# Send a request to the URL using curl, and get the size of the response body in bytes
SIZE=$(curl -s -w "%{size_download}" $URL -o /dev/null)

# Display the size of the response body in bytes
echo "$SIZE"
