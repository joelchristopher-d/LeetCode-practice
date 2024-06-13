class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        # print(seats,students)
        t=0
        for i in range(len(seats)):
            t+=abs(seats[i]-students[i])
        return t

                
