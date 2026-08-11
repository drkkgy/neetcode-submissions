class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        while sandwiches:
            stud = students.pop(0)

            if stud == sandwiches[0]:
                sandwiches.pop(0)
            else:
                students.append(stud)

            if len(set(students)) == 1 and   students[0] != sandwiches[0]:
                return len(sandwiches)

        return 0


        