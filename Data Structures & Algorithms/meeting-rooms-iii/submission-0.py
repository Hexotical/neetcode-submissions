class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        #return number of the room that held the most meetings
        #If tie return lowest number
        #Values of start time are unique
        #Meeting takes place in unused room lowest num
        #No available rooms, meeting will be delayed
        #Room becomes unused, earlier start will be given room
        #there are n rooms
        
        #Keep a heap tracking free rooms
        #2 heaps, free rooms and rooms becoming free
        #3 heaps? nah just a pointer towards meetings
        
        meetings.sort(key= lambda x:(x[0],x[1]))
        print(meetings)
        rooms = list(range(n))
        heapq.heapify(rooms)
        in_use = []
        heapq.heapify(in_use)
        cur_time = meetings[0][0]
        cur_meeting = 0
        most_used = defaultdict(int)
        while cur_meeting < len(meetings):
            if cur_time < meetings[cur_meeting][0]:
                cur_time = meetings[cur_meeting][0]
            while in_use and cur_time >= in_use[0][0]:
                time, room = heapq.heappop(in_use)
                heapq.heappush(rooms, room)
            while not rooms:
                time, room = heapq.heappop(in_use)
                cur_time = time
                heapq.heappush(rooms, room)

            to_use = heapq.heappop(rooms)
            most_used[to_use] += 1
            
            heapq.heappush(in_use, (cur_time + meetings[cur_meeting][1] - meetings[cur_meeting][0], to_use))
            cur_meeting += 1

        to_ret = 0
        for r in most_used:
            if most_used[to_ret] < most_used[r]:
                to_ret = r
            elif most_used[to_ret] == most_used[r]:
                to_ret = min(to_ret, r)
        return to_ret