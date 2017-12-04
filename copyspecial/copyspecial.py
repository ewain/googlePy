#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands
import subprocess


"""Copy Special exercise
"""

# +++your code here+++
# Write functions and modify main() to call them
listPath = []
dictPath ={}
def get_special_paths(todir):
  print '---------get_special_paths-----------: ', todir
  for fileName in os.listdir(todir):
    iteratore = re.finditer(r'__\w*__', fileName)
    for mat in iteratore:
      trovato = mat.group()
      print os.path.abspath(trovato)
      listPath.append(os.path.abspath(trovato))
  #print 'listPathIn:', listPath 
  return listPath


def copy_to(paths, to_dir):
  print '---------copy_to-----------: ', to_dir
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for fileNames in os.listdir('.'):
    iteratore = re.finditer(r'__\w*__', fileNames)
    print 'fileNames:', fileNames
    for mat in iteratore:
      trovato = mat.group()
      os_path = os.path.abspath(to_dir)    
      shutil.copy2(fileNames,os_path)
  #print 'listPathIn:', listPath 
  print '---------FINE copyTo---------'
#---------------------------------
  if not os.path.exists(to_dir):
    os.mkdir(to_dir)
  for path in paths:
    fname = os.path.basename(path)
    print 'basename: ',fname
    print'join: ',os.path.join(to_dir, fname)
    print 'path:', path
    #shutil.copy(path, os.path.join(to_dir, fname))
  
  return
def zip_to(path, tozip):
  print 'toziop: ',tozip
  subprocess.Popen('notepad.exe c:\aaa.txt')    
  return
  
def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)
  
  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)
  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    print 'todir: ', todir
    copy_to('.', todir)
    
    #del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    print 'tozip: ', tozip
    zip_to('.',tozip)
    #del args[0:2]

  # +++your code here+++
  # Call your functions
  dir=''
  if len(args) == 1:
    dir=args[0]
    print "un solo parametro: ", dir
    get_special_paths(dir)
    #del args[0]


  
if __name__ == "__main__":
  main()
