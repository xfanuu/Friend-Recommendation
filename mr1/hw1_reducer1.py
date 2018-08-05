#!/usr/bin/env python
import sys
current_friend = ''
current_user = ''
friendsofuser = {}
current_friendsofuser = {}
friend_in_progress = ''
nuser = 0
userlist = []
userpair = []
for line in sys.stdin:
    line = line.strip().split('\t')
    if len(line)!=3:
        continue
    current_friend, current_user, current_friendsofuser =  line
    if current_friend != friend_in_progress:
        friendsofuser = {}
        userlist = []
        nuser = 0
    nfriend_j = len(current_friendsofuser.split(','))
    friendsofuser[nuser] = current_friendsofuser
    current_friendsofuser = {}
    userlist.append(current_user)
    userpair = []
    nuser += 1
    friend_in_progress = current_friend
    if nuser <=1:
        continue
    for i in range(nuser-1):
        userpair.append(current_user)
        nfriend_i = len(friendsofuser[i].split(','))
        if current_user in friendsofuser[i]:
            userpair = []
            continue
        userpair.append(userlist[i])
        print('%s,%s\t%s\t%s' % (userpair[0],userpair[1],1,nfriend_j + nfriend_i))
        userpair = []
