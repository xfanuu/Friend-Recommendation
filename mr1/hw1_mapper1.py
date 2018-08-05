#!/usr/bin/env python
 
import sys

input = []
user = {}
friendsofuser = {}
inifriends = {}
for line in sys.stdin:
	input.append(line)
for i in range(len(input)):
    user[i] = input[i].split('\t')[0]
    friendsofuser[i] =  input[i].split('\t')[1]
    friendsofuser[i] = list(friendsofuser[i].split(','))
    friendsofuser[i][-1] = friendsofuser[i][-1].strip()
for i in range(len(input)):
    for j in range(len(friendsofuser[i])):
        print '%s\t%s\t%s' % (friendsofuser[i][j],user[i],friendsofuser[i])
