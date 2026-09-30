class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        """
        Input: n = 2, 
        Output: 0

        Explore

        free_rooms []
        busy_rooms [(t=10, 0), (t=10, 1)]
        meetings = [[1,10],[2,10],[3,10],[4,10]]
        t = 0
        t = 1
        [1, 10] -> 0
        t = 2
        [2, 10] -> 1
        t = 3
        [3, 10] *free rooms is empty*
        t = top of busy room's t
        t = 10
        free busy rooms at t=10
        free_rooms = [0,1]
        [3, 10] -> 0
        [4, 10] -> 1

        What about:
        free_rooms [0, 1]
        busy_rooms []
        meetings = [[1,10],[2,10],[13,10],[14,10]
        t = 2
        m = [13, 10]
        t = 13 -> free everything
        [13, 10] -> 0
        [14, 10] -> 1
        
        Concepts
        * sort meetings by start time
        * heap for busy_rooms
        * heap for free_rooms
        * keep track of time t
        * if no free rooms, skip till next free room is avail
        * then book the next meeting room for the next meeting
        * keep counter of room: meetings
        """
        import heapq
        from collections import defaultdict
        cnts: dict[int, int] = defaultdict(int)
        sorted_meetings = sorted(meetings, key=lambda x: x[0]) 
        # room ids
        free_rooms = list(range(n))
        # pairs of (time_freed, room_id)
        busy_rooms = []

        """
        Pseudocode
        sort meetings by start time
        initialize heaps, t=0
        for each meeting m
            if free room
                assign m to free room
                update count
            else
                skip till next free room is avail
                book next room for m
                update count
        put results into heap, get max count
        """

        """
        Note: bug happens at [6,10], but not at [5,10]
        Trace debugging practice
        free_rooms []
        busy_rooms [(10,1),(10,2)]
        meetings = [[1,10],[2,10],[3,10],[4,10],[5,10],[6,10]]
        0:[1,10]
        1:[2,10]
        cur = 2
        t = 10
        [3,10]
        """

        t = sorted_meetings[0][0]
        cur = 0
        while cur < len(sorted_meetings):
            st, et = sorted_meetings[cur]
            # free busy rooms at time t
            while len(busy_rooms) > 0 and busy_rooms[0][0] <= t:
                _, room = heapq.heappop(busy_rooms)
                heapq.heappush(free_rooms, room) 

            # then resume algo
            if len(free_rooms) > 0:
                room = heapq.heappop(free_rooms)
                heapq.heappush(busy_rooms, (t+(et-st), room))
                cnts[room] += 1
                cur += 1
                if cur < len(sorted_meetings):
                    t = max(t, sorted_meetings[cur][0])
            else:
                next_avail = busy_rooms[0][0]
                t = max(next_avail, st)
        
        room, max_sofar = -1, -1
        for k, v in cnts.items():
            # if multiple rooms, return room w lowest number
            if v > max_sofar or (v == max_sofar and k < room):
                max_sofar = v
                room = k
        return room
        

        
        