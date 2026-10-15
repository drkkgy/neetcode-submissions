"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        if not intervals:
            return True

        intervals.sort(key = lambda i:i.start )

        current_booked_time = [intervals[0].start,intervals[0].end]



        for interval in intervals[1:]:

            # First check for overlapp

            if current_booked_time[1] > interval.start:
                return False

            # if current_booked_time[0] < interval.start and current_booked_time[1] > interval.start:
            #     return False
            # if current_booked_time[0] < interval.end and current_booked_time[1] > interval.end:
            #     return False 
            # if current_booked_time[0] == interval.start and current_booked_time[1] == interval.end:
            #     return False 

            # #  Case1 Full overlap
            # if current_booked_time[0] <= interval.start:
            #     if current_booked_time[1] >=interval.end:
            #         return False
            # # Case2 Partial Overlap 
            # if current_booked_time[0] < interval.start:
            #     if current_booked_time[1] < interval.end:
            #         return False

           

            current_booked_time[0] = min(current_booked_time[0],interval.start)
            current_booked_time[1] = max(current_booked_time[1],interval.end)

        return True


