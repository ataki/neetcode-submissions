"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

"""
Explore:
[(0,40),(5,10),(15,20)]
* sort by start times
* max_overlap of intervals
* danger in sorting which interval, and invariant

0,40 x 5,10 x 15,20 -> 2

[(0,40),(5,10),(41,50),(42,60),(43,60)]
41,50 x 42,60 x 43,60
3

Invariant:
bc we sort by start time, it's safe to pop from heap of end intervals
when an end interval does not intersect with upcoming interval

Pseudocode:
sort by start intv
start with first interval -> put the end interval in
for each interval after
pop from heap until start time > top of heap
if empty heap, reset count to 1
else update cur_overlap
push end time to heap
set max_overlap to max of 2
return max_overlap

[(0,40),(5,10),(41,50),(42,60),(43,60)]
h = [50,60,60]
max_sofar = 2
count = 3
(43,60)
"""

import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        [(0,40),(5,10),(15,20)]
        q = 40
        cur = 2
        max_sofar = 2
        15,20

        bug: pseudocode is wrong. we shouldn't increment by 1 every time.
        """
        if len(intervals) == 0:
            return 0
        sorted_vals = sorted(intervals, key=lambda x: x.start)
        q = [sorted_vals[0].end]
        cur, max_sofar = 1, 1
        for iv in sorted_vals[1:]:
            while q and iv.start >= q[0]:
                heapq.heappop(q)
            # this statement looks weird
            if not q:
                cur = 1
            else:
                # update this to be the length of heap + 1
                cur = len(q) + 1
            heapq.heappush(q, iv.end)
            max_sofar = max(max_sofar, cur)
        return max_sofar

        
        