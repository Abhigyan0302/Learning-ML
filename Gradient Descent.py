import numpy as np
def gradient_descent(x,y):
    n=len(x)
    m_curr=b_curr=0
    learning_rate=0.01
    for i in range(0,10000):
        y_pred=m_curr*x+b_curr
        m_derv=(-2/n)*sum(x*(y-y_pred))
        b_derv=(-2/n)*sum((y-y_pred))
        m_curr=m_curr-learning_rate*m_derv
        b_curr=b_curr-learning_rate*b_derv
        print("m {},b {}".format(m_curr,b_curr))
 
 
x=np.array([1,2,3,4,5])
y=np.array([5,7,9,11,13]) 
gradient_descent(x,y)