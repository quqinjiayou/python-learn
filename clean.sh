#!/bin/bash

set -e -x

find ./  -name "*~" -exec rm -rf {} \;

find ./  -name "._.DS_Store" -exec rm -rf {} \;
find ./  -name ".DS_Store" -exec rm -rf {} \;
