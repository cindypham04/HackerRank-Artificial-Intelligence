# Enter your code here. Read input from STDIN. Print output to STDOUT

'''
Problem frame: 
Physics: independent variable <- x 
History: <- y

y = w0 + w1.x

result: integer, round to 3 decimal places

Solution:
n: number of data point
xi: each physics data point
x bar: average score of physics - sum of all xi over n 
yi: each history data point
y bar: average score of history - sum of all yi over n

Step by step:
- Obtaining and storing the physics scores and historical score from the user
- Calculate the x bar and y bar. 
- Calculate m, use for loop
'''
# Get data from the user
x = list(map(int, input().split()[2:])) # x = [15, 12, ...]
y = list(map(int, input().split()[2:]))

# The number of students
n = len(x)

# Compute x bar and y bar
x_bar = sum(x) / n
y_bar = sum(y) / n

# Initialize numerator and denominator of m's equation
numerator = 0
denominator = 0

# Calculate m using the formula: m = sum((xi - x_bar) * (yi - y_bar)) / sum((xi - x_bar) ** 2)
for i in range(n):
    numerator += (x[i] - x_bar) * (y[i] - y_bar)
    denominator += (x[i] - x_bar) ** 2
    
m = round(numerator / denominator, 3)

print(m)