import zmq

# ventilator-worker connection (PARALLEL PIPELINE PATTERN)
context = zmq.Context()
receiver = context.socket(zmq.PULL) 
receiver.connect("tcp://127.0.0.1:7000") 

# worker-sink connection (PARALLEL PIPELINE PATTERN)
sender = context.socket(zmq.PUSH) #socketin tipi PULL
sender.connect("tcp://localhost:5556") # 5556 portunda yeni bir bağlam yarattı 

print("Connected to server.")

# to processthe information and sending it to the sink
while True:
    term = receiver.recv_pyobj()
    term_result = term[0]*(term[1]**term[2])
    print("term number that workers running on it %d: result : %d " %(term[3], term_result))
    sender.send_pyobj(term_result)
    print("Finished!")

