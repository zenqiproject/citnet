
from citnet import Address
from citnet.tcp import Host


address = Address("127.0.0.1", 5000)
client  = Host(None, 2)
peer    = client.connect(address)
