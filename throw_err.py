#!/usr/bin/env python

# This script raises an error based on 
# user-supplied command line argument

import sys
import os


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
    sys.exit()

# Check args
if len(sys.argv) != 2:
    print_usage()

error_type = sys.argv[1]

if error_type == "assertion":
    assert 1 > 2		
elif error_type == "io":
    f = open('/not/found/', 'r') 
elif error_type == "import":
    from pickle import doesNotExist 
elif error_type == "index":
    arr = ['a', 'b']
    print arr[10]	 
elif error_type == "key":
    dictionary = { 'a':0 }
    print dictionary['z'] 
elif error_type == "name":
    print arr[0] 
elif error_type == "os":
    for i in range(10):
        print i, os.ttyname(i)
elif error_type == "type":
    a = ['a']
    b = 1 
    add = a[0] + b 
elif error_type == "value":
    print chr(2048) 
elif error_type == "zerodivision":
    print 2/0 
elif error_type =="iter":
    l=[0]
    i=iter(l)

    print i
    print i.next()
    print i.next()
elif error_type =="syntax":
    print eval('five times three')
elif error_type =="custom":
    raise MyCustomError("Custom Error")
elif error_type=="recursion":
    sys.setrecursionlimit(1)
    def func(f):
        (f)
    for i in range(0, 10):
	func(func())
elif error_type=="unbound":
    var = 0 
    def inc():
        var += 1
    inc()
else:
    sys.stderr.write("Sorry, not able to throw a(n) ")
    sys.stderr.write(error_type + " error\n")
    print_usage()


