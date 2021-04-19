
from citnet import Address
from citnet.tcp import Host
from citnet import EventType

address = Address("127.0.0.1", 5000)
host = Host(address, # address whre server should bind to
        10 # allow 10 connection / clients
    )

running = True

while running:

    event = host.service(0) # -> wait 1 second for upcoming event

    if event.type == EventType.CITNET_EVENT_CONNECT:
        print("Got connection {}".format(event.peer.data))
        continue
    
    elif event.type == EventType.CITNET_EVENT_RECEIVE:
        print("Received: {}".format(event.packet.data))

    elif event.type == EventType.CITNET_EVENT_DISCONNECT:
        print("Client disconnected")
        continue