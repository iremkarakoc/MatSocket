import zmq

context = zmq.Context() #created context to create socket

#ventilator connection
ventilator = context.socket(zmq.REP) #created socket --- socket type:req-rep
ventilator.bind('tcp://*:5557')
vent_message= ventilator.recv_pyobj()
ventilator.send(b"")

receiver = context.socket(zmq.PULL) #created socket --- socket type:push pull
receiver.bind("tcp://*:5556")



result = 0
for k in range(vent_message+1):
    worker_message=receiver.recv_pyobj()
    result += worker_message
print(result) 


