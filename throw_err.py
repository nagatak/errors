#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("err", help="display name error")


# Custom error class
class MyCustomError(Exception):
    pass

class CustomError(Exception):
    def __init__(self, arg):
        self.msg = arg


def print_usage():
    """Print usage and exit"""
    sys.stderr.write("usage: python raise_err.py <error type>\n")
    sys.stderr.write("available errors: \n")
    sys.stderr.write("\tassertion, io, import, index\n")
    sys.stderr.write("\tkey, name, os, type, value,\n")
    sys.stderr.write("\tzerodivision\n")
    sys.stderr.write("\tNew Errors:\n")
    sys.stderr.write("\titer, syntax, recursion, unbound\n")
    sys.stderr.write("\tcustom class:\n")
    sys.stderr.write("\tcustom\n")
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

if parser.parse_args().err == "assertion":
    assert 1 > 2		
elif parser.parse_args().err == "io":
    f = open('/not/found/', 'r') 
elif parser.parse_args().err == "import":
    from pickle import doesNotExist 
elif parser.parse_args().err == "index":
    arr = ['a', 'b']
    print arr[10]	 
elif parser.parse_args().err == "key":
    dictionary = { 'a':0 }
    print dictionary['z'] 
elif parser.parse_args().err == "name":
    print arr[0] 
elif parser.parse_args().err == "os":
    for i in range(10):
        print i, os.ttyname(i)
elif parser.parse_args().err == "type":
    a = ['a']
    b = 1 
    add = a[0] + b 
elif parser.parse_args().err == "value":
    print chr(2048) 
elif parser.parse_args().err == "zerodivision":
    print 2/0 
elif parser.parse_args().err =="iter":
    l=[0]
    i=iter(l)

    print i
    print i.next()
    print i.next()
elif parser.parse_args().err =="syntax":
    print eval('five times three')
elif parser.parse_args().err =="custom":
    raise MyCustomError("Custom Error")
elif parser.parse_args().err == "recursion":
    sys.setrecursionlimit(1)
    def func(f):
        (f)
    for i in range(0, 10):
	func(func())
elif parser.parse_args().err == "unbound":
    var = 0 
    def inc():
        var += 1
    inc()
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()


