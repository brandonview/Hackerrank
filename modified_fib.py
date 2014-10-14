# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

argString = sys.stdin.readline()
args = argString.split()
  
n1 = args[0]
n2 = args[1]
nth = args[2]

n1 = int(float(n1))
n2 = int(float(n2))
nth = int(float(nth))

solutions = []
solutions.append(n1)
solutions.append(n2)



for i in range(2, nth):
    tempSolution = solutions[i-1] * solutions[i-1] + solutions[i-2]
    solutions.append(tempSolution)
    
finalSolution = solutions[len(solutions)-1]
    

    
print(finalSolution)
