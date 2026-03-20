import numpy as np
import matplotlib.pyplot as plt
#size of house in sq feet
size = np.array([1000,1500,2000,2740,4250,5000])
#price of the house in lakhs
price=np.array([2,3,4,5.5,8.4,10])

def predict(size,a,x):
    return a*size+x

def error(size,price,a,x):
    total=0
    n=len(size)
    for i in range(n):
        p=a*size[i]+x
        errors=p-price[i]
        total=total+(errors*errors)
    cost = total/n
    return cost

def gradient_descent(size,price,a,x,alpha):
    n=len(size)
    change_a=0
    change_x=0
    for i in range(n):
        predictvalue=a*size[i]+x
        errors= predictvalue-price[i]
        change_a=change_a+errors*size[i]
        change_x=change_x+errors
    
    change_a=(change_a)*2/n
    change_x=(change_x)*2/n
    a=a-alpha*change_a
    x=x-alpha*change_x
    return a,x

a=0
x=0
cost_arr=[]
alpha = 0.0000001
for i in range(1000):
    a,x=gradient_descent(size,price,a,x,alpha)
    cost_arr.append(error(size,price,a,x))
    if i%100==0:
        print("Iteration : ",i)
        print("Cost : ",error(size,price,a,x))

print("Final Slope : ",a)
print("Final intercept : ",x)

plt.plot(cost_arr)
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()
