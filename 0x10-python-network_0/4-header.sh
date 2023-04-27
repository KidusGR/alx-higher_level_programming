#!/bin/bash
# a script that passes a variable in the header of the request
curl -sH "X-HolbertonSchool-User-Id: 98" "$1"
