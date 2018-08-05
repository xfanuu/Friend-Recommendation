#!/usr/bin/env python
from __future__ import division
import sys
n_total = 0
n_comm = 1
current_userpair = []
userpair_in_progress = []
Jaccard_similarity = 0
for line in sys.stdin:
    line = line.strip().split('\t')
    # If for some reason there are not 3 items,
    # then move on to next line
    if len(line)!=3:
        print('%s,%s\t%s' % (userpair_in_progress[0],userpair_in_progress[1],Jaccard_similarity))
    else:
        userpair, one, total = line
        n_total = int(total)
        current_userpair = list(userpair.split(','))
        if userpair_in_progress == []:
            Jaccard_similarity = n_comm / (n_total-n_comm)
            userpair_in_progress = current_userpair
            n_comm = 1
        else:
            if current_userpair != userpair_in_progress:
                print('%s,%s\t%s' % (userpair_in_progress[0],userpair_in_progress[1],Jaccard_similarity))
                n_comm = 1
                Jaccard_similarity = n_comm / (n_total-n_comm)
                userpair_in_progress = current_userpair
            else:
                n_comm += 1
                Jaccard_similarity = n_comm / (n_total-n_comm)
                userpair_in_progress = current_userpair
                
