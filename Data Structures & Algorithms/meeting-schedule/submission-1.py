"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        meetings = sorted(intervals, key=lambda x: x.start)
        for i in range(len(meetings) - 1):
            if meetings[i].end > meetings[i+1].start:
                return False
        return True