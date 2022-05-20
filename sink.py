import zmq

context = zmq.Context() #created context to create socket

# ventilator-sink connection (REQUEST-REPLY PATTERN)
ventilator = context.socket(zmq.REP)  
ventilator.bind('tcp://*:5557')
vent_message= ventilator.recv_pyobj()
ventilator.send(b"")

# worker-sink connection (PARALLEL PIPELINE PATTERN)
receiver = context.socket(zmq.PULL)  
receiver.bind("tcp://*:5556")


# calculating the solution of a mathematical expression
result = 0
for k in range(vent_message+1):
    worker_message=receiver.recv_pyobj()
    result += worker_message
print(result) 


