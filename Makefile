##
#
#
# @file
# @version 0.1


SHELL = /bin/bash

unittest:
	python -m unittest discover -p 'test*.py' -v
