#!/bin/bash
for f in `cat joget_repos`; do `git clone $f`; done
