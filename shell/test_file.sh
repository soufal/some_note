#!/bin/bash
file="1.sh"
if [ -r $file ]
then
echo "File has read access"
else echo "File does not have read access"
fi
