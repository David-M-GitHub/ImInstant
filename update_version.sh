#!/bin/bash
current_version=$(grep "CURRENT_VERSION = " version.py | cut -d '"' -f 2)
echo $current_version > Version.txt
