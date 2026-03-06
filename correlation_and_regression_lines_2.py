# x is independent variable
# y is target -> y_pred = m.x + b
x =[int(x) for x in "15  12  8   8   7   7   7   6   5   3".split()]
y =[int(x) for x in "10  25  17  11  13  17  20  13  9   15".split()]

# Initialize slope and intercept 
m, b = 0, 0

# Initilialize learning rate 
n = 0.0001

training = True 

# m += dm 
# b += db
while training:
    dm = 0
    db = 0
    # The error of each data point equals to true value - predicted value
    # Predicted value: y_pred = m.x + b
    for i in range(len(x)):
        dm += (y[i] - (m * x[i] + b)) * x[i]
        db += y[i] - (m * x[i] + b)
        
    # Gradient descent: update b and m
    b += n * db
    m += n * dm
    
    # Stop training when dm and db doesn't change much
    if abs(dm) < 1e-6 and abs(db) < 1e-6:
        training = False
        
print(round(m, 3))