#!/bin/bash

# Get the URL from the command line argument
url="$1"

# Send a request to the URL using curl and save the response body to a file
response=$(curl -sSL -w "%{size_download}" -o /dev/null "$url")

# Display the size of the response body in bytes
echo "$response"

