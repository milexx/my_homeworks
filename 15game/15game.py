# -*- coding: utf-8 -*-

import os
import random

__author__ = 'milex'

EMPTY_MARK = '  '
u = (0, 1, 2, 3)
d = (12, 13, 14, 15)
r = (3, 7, 11, 15)
l = (0, 4, 8, 12)
blocks0 = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', EMPTY_MARK]
blocks = [' 1', ' 2', ' 3', ' 4', ' 5', ' 6', ' 7', ' 8', ' 9', '10', '11', '12', '13', '14', '15', EMPTY_MARK]
random.shuffle(blocks)
#e = blocks.index(EMPTY_MARK)
st = 1
err = ' '

def print_blocks(s):
    print('15-puzzle       Step ' + str(st))
    print('------------------------')
    print (blocks[0:4])
    print (blocks[4:8])
    print (blocks[8:12])
    print (blocks[12:16])
    print('------------------------')
    if s not in u: print('press w to move up')
    if s not in d: print('press z to move down')
    if s not in l: print('press a to move left')
    if s not in r: print('press s to move right')
    print('press e to exit')
    print('------------------------')
    print(err)

def w(n,blocks):
    if n not in u:
        k = blocks.pop(n-4)
        blocks.remove(EMPTY_MARK)
        blocks.insert(n-4,EMPTY_MARK)
        blocks.insert(n,k)
        return blocks

def z(n,blocks):
    if n not in d:
        k = blocks.pop(n+4)
        blocks.remove(EMPTY_MARK)
        blocks.insert(n,k)
        blocks.insert(n+4,EMPTY_MARK)
        return blocks

def a(n,blocks):
    if n not in l:
        k = blocks.pop(n-1)
        blocks.remove(EMPTY_MARK)
        blocks.insert(n-1,EMPTY_MARK)
        blocks.insert(n,k)
        return blocks

def s(n,blocks):
    if n not in r:
        k = blocks.pop(n+1)
        blocks.remove(EMPTY_MARK)
        blocks.insert(n,k)
        blocks.insert(n+1,EMPTY_MARK)
        return blocks

while blocks != blocks0 :
   os.system('cls')
   e = blocks.index(EMPTY_MARK)
   print_blocks(e)
   err = ' '
   p = raw_input('Make your move:')

   if (p.lower() == 'w' and e not in u):
        st = st + 1
        blocks = w(e,blocks)
   elif (p.lower() == 'a' and e not in l):
        st = st + 1
        blocks = a(e,blocks)
   elif (p.lower() == 'z' and e not in d):
        st = st + 1
        blocks = z(e,blocks)
   elif (p.lower() == 's' and e not in r):
        st = st + 1
        blocks = s(e,blocks)
   elif (p.lower() == 'e'):
        blocks = blocks0
   else:
        err = 'Bad key!'
   continue
