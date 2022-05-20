import zmq

CoefArr = []
print("Please enter the degree of polynomial: ")
degree_num = int (input())
while(degree_num<0):
    if(degree_num<0):
        print("Please enter number bigger than zero!")
        degree_num = int (input())
print("Please enter the coefficients of the polynomial: ")
for x in range(degree_num+1):
    coeff_num = int (input())
    CoefArr.append(coeff_num)

print(CoefArr)
print("Please enter the root to find the solution: ")
root =int( input())


context = zmq.Context() #created the context to create socket
# sink connection --- request-reply  pattern used
sink = context.socket(zmq.REQ)
sink.connect('tcp://127.0.0.1:5557')
sink.send_pyobj(degree_num)
s = sink.recv()

#worker connection -- parallel pipeline pattern used
sender = context.socket(zmq.PUSH)
sender.bind("tcp://127.0.0.1:7000")   # Server is ready listening on port 7000"
print("Press any key to start to send message to the workers!")
_ = input()



inputs = []
curr_term = 1
print("ready to send coefficients to the workers")
for i in CoefArr:    
    while (degree_num>=0):
        inputs.append(i)
        inputs.append(root)
        inputs.append(degree_num)
        inputs.append(curr_term)
        print(inputs)
        break
    degree_num -= 1
    curr_term += 1
    sender.send_pyobj(inputs)
    inputs.clear()
