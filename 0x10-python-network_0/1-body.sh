#!/bin/bash

# Read the URL from the command line argument
URL=$1

# Send a request to the URL using curl, and get the status code and response body
RESPONSE=$(curl -s -w "\n%{http_code}" $URL)

# Split the response into status code and body
STATUS_CODE=$(echo "$RESPONSE" | tail -n1)
BODY=$(echo "$RESPONSE" | sed '$d')

# Display the body if the status code is 200
if [ "$STATUS_CODE" -eq 200 ]; then
  echo "$BODY"
else
  echo "Status code: $STATUS_CODE"
fi

