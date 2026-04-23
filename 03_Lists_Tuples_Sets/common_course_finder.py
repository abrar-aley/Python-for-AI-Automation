# task 5 common course finder

csA= {"Discrete Maths", "OOP", "Calculus", "Data Structures"}
csB= {"PF", "OOP", "Calculus", "ICT", "English"}

print('Common Course: ', csA.intersection(csB))
print('Unique courses of A: ',csA.difference(csB))
print('Unique courses of B: ',csB.difference(csA))
print('List of all courses: ',csA.union(csB))

