#!/usr/bin/env python
import sys
for line in sys.stdin:
        line = line.strip().split('\t')
        userpair, n_comm, n_total = line
        userpair = list(userpair.split(','))
        print('%s,%s\t%s\t%s' % (userpair[0],userpair[1],n_comm,n_total))
        print('%s,%s\t%s\t%s' % (userpair[1],userpair[0],n_comm,n_total))
print 'FINISHED'
