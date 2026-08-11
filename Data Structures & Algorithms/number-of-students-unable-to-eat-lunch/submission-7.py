from collections import Counter
from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)
        unable_to_eat = len(students)

        for sandwich in sandwiches:
            if count[sandwich] == 0:
                break

            count[sandwich] -= 1
            unable_to_eat -= 1

        return unable_to_eat