
from citnet import Address
from citnet.tcp import Host

address = Address("127.0.0.1", 5000)
host = Host(address, # address whre server should bind to
        10 # allow 10 connection / clients
    )

running = True

while running:

    event = host.service(1) # -> wait 1 second for upcoming event
    
     