#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
from __future__ import print_function
from fileinput import filename
from re import match

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""
import cardinality
import sys
from operator import itemgetter, attrgetter
import re

# +++your code here+++

def count_words(filename):
    #print '-----------FILE----------'
    # Echo the contents of a file
    #print "faccio tutto: ", seleziona
    dict_foo = {}
    f = open('foo.txt', 'rU')
    file_list = f.readlines()
    for riga in file_list:
        #print '---', riga,
        a = riga.split()
        #print 'parola1 ',a.pop(0),'\n'        
        for parola in a:
            p = parola.lower()
            #print 'parola+ ', parola,
            if p in dict_foo:
                dict_foo[p]+=1
            else:
                dict_foo[p]=1
 
    f.close()
    #-----prova re----
    f = open('foo.txt', 'rU')
    file_list = f.read()
    result = re.finditer(r'\nC', file_list,)
    b = re.finditer(r'\nC', file_list,)
    #print("cardi: ",cardinality.count(result))
    print ('result: ' , result)
    for match in result :
        print ('ris: ', match.group(0))
        print ('posizioni: ',match.span())
        
    for match in b :
        print ('ris2: ', match.group(0))
        print ('posizioni2: ',match.span())
    f.close()
    print ('test iterable')
    iterable = [1, 2] 
    iterator = iter(iterable)
    print(iterator.next())
    print(iterator.next())
    #se eseguo un altro nex mi da errore perché è finito l'iteratore
    #print(iterator.next())   
    print ('test iterable')
    
    #print 'dizionario: '
    #for key in sorted(dict_foo.keys(), key=dict_foo.__getitem__, reverse=True):
    #    print "K:", key, " - ", dict_foo[key] 
    #for keys in dict_foo:
    #    print "K:", keys, " - ", dict_foo[keys]
    #print dict_foo
    #sys.exit(0)
    return dict_foo
    
    #print '-----------EOF :)--------'
    return


def print_words(filename):
    a = count_words(filename)
    print ('-----PAROLE IN ORDINE ALFABETICO------ ')
    #for k in sorted(a):
    #    print k,': ',a[k]
    
    
    for key in sorted(a.iterkeys()):
        print (key,':',a[key],sep='')
 
    #print sorted(a, key=a.__getitem__, reverse=True)[:10]
    #print a
    #print 'DIZ',a
    #for k in b:
    #    print 'coppieAll: ', k, b[k]
    #    print k 
    #print 'sono in words'
    return

def print_top(filename):
    a = count_words(filename)
    #print 'tutti: ', a['tutti']
    conta=1
    print ('---TOP 10 WORD---')
    #for k in sorted(a,key=a.__getitem__, reverse=True)[:9]:
    #for k in sorted(a,key=a.__getitem__, reverse=True)[:9]:        
        #print conta,':',k,a[k]    #a = count_words(filename, 'top')
        #conta+=1
    for key, value in sorted(a.iteritems(), key=lambda (k,v): (v,k), reverse=True)[:10]:
        print (key,':',value,sep='')
        conta+=1
    #for k in a:
        #print 'coppieTop: ', k, a[k]
    #    print k
    return    
    

# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.
###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    '''  
    print "------DICT-------"
    dict = {}
    dict['a'] = 'alpha'
    dict['g'] = 'gamma'
    dict['o'] = 'omega'
    
    print dict
    print"a in dict? ", 'a' in dict #True
    print"dict[a]? ", dict['a']  #alpha
    #print"print z", dict['z']  #ERRORE!!!! KeyError --> chiave non trovata nel dizionario
    print dict.get('z') #SENZA ERRORE None -->chiave non trovata nel dizionario
    print dict.get('g') #gamma
    print 'chiavi/keys(): ',dict.keys()
    print 'valori/values: ',dict.values()
    print 'items: keys+values di tutto il dict: \n', dict.items()#diverso da 'print dict'...
    ## By default, iterating over a dict iterates over its keys.
    ## Note that the keys are in a random order.
    for key in dict: print 'chiave: ',key
    ## Exactly the same as above
    for key in dict.keys(): print key
    ## Common case -- loop over the keys in sorted order,
    ## accessing each key/value
    for key in sorted(dict.keys()):
        print 'coppia chiave valore:',key, dict[key]
    ## .items() is the dict expressed as (key, value) tuples
    print dict.items()  ##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]    
    hash = {}
    hash['word'] = 'garfield'
    hash['count'] = 42
    s = 'I want %(count)d copies of %(word)s' % hash  # %d for int, %s for string
    print s
    
    print '------------DEL------------'
    var = 6
    del var  # var no more!
    
    list = ['a', 'b', 'c', 'd']
    del list[0]     ## Delete first element
    del list[-2:]   ## Delete last two elements
    print list      ## ['b']
    
    dict = {'a':1, 'b':2, 'c':3}
    print dict
    del dict['b']   ## Delete 'b' entry
    print dict      ## {'a':1, 'c':3}
    
    print '------fine dict----------'
    #The f.readlines() method reads the whole file into memory and returns its contents as a list of its lines.
    #The f.read() method reads the whole file into a single string, which
    #can be a handy way to deal with the text all at once, such as with regular expressions we'll see later.
    
    print '-----------FILE----------'
    # Echo the contents of a file
    f = open('foo.txt', 'rU')
    for line in f:   ## iterates over the lines of the file
        print line,    ## trailing , so print does not add an end-of-line char
                     ## since 'line' already includes the end-of line.
    f.close()
    #sys.exit(0)
    
    print '-----------EOF :)--------'
    '''
    if len(sys.argv) != 3:
        print ('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
    
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print ('unknown option: ' + option)
        sys.exit(1)
    
if __name__ == '__main__':
    main()
