# Doctor-Hospital Matching With Hungarian Algorithm

Efficient allocation of resources is an important objective in healthcare. This also applies to matching doctors to desired hospitals. The algorithm implemented matches N doctors with K hospitals. The doctors provide a list of their preferences and the hospitals declare a capacity. A fair, optimized list of assignments of the doctors to hospitals is returned. 

Hungarian algorithm is a combinational optimization algorithm that solves the assignment linear programming problem is polynomial time. It finds the minimum cost when assigning people to jobs and provides an optimized solution. It is generally implemented on a square n x n matrix and each person is assigned to one job with a time complexity of O(n^3). When the number of the doctor's preference is smaller, it means that the doctor is more satisfied with the hospital. So, when the total of all doctors' preference is the lowest, that is the state in which doctors are most satisfied overall. This is the same as finding the minimum cost for a job, so the matching problem of doctors and hospitals can be solved using the Hungarian algorithm. 

We have implemented an algorithm where the capacity of the hospital (maximum capacity is more than doctors) and unequal number of doctors is taken into consideration. We have used the method of adding dummy lines to allow the Hungarian algorithm to be implemented in non-square matrices (ie, when the hospital capacity is greater than the number of doctors). 

In this case, the individual capacity of hospitals cannot differ and the preferences of the hospital is not considered. 

References:
https://www.hungarianalgorithm.com/hungarianalgorithm.php
https://en.wikipedia.org/wiki/Hungarian_algorithm
