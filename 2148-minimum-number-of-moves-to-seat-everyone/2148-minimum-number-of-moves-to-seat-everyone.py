class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        move = 0
        students.sort()
        seats.sort()
        x = len(seats)
        for i in range(x):
            move = move + abs((seats[i]- students[i]))
        
        return move