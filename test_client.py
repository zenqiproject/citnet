
from citnet import Address, Packet
from citnet.tcp import Host
import time

address = Address("127.0.0.1", 5000)
client  = Host(None, 2)
peer    = client.connect(address)

time.sleep(5)
packet = Packet("hello world")
peer.send(packet.create())