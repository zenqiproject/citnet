#            Copyright (C) 2021, Zenqi. All Rights Reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


import socket
import struct
import time
import sys
from .errors import *
from .citnet import CitNet
from .address import Address
from .event_type import EventType
from .packet import Packet


class CitNet_TCP(CitNet):
    """
    Main CitNet object for TCP connection
    """

    def __init__(self):
        super().__init__()
        self.addressFamily  = socket.AF_INET
        self.socketType     = socket.SOCK_STREAM # SOCK_STREAM listen to protocol (TCP)
        self.socketProto    = socket.IPPROTO_UDP 


class Peer:
    """
    Main class for handling peer
    """
    _data: None
    def __init__(self, citnet: CitNet_TCP):
        self.citnet = citnet

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data=None):
        # peer data including Peer host and port.
        if data != None:
            self._data = data
        else:
            raise DataError("Specify data. Expected -> data got -> NoneType")

        return self.data

class Event:

    eventType: EventType.CITNET_EVENT_NONE

    def __init__(self):
        self._packet = None

    @property
    def type(self):
        if self.eventType:
            return self.eventType
        else:
            return EventType.CITNET_EVENT_NONE

    @type.setter
    def type(self, eventType: EventType):
        if eventType:
            self.eventType = eventType
        else:
            self.eventType = EventType.CITNET_EVENT_NONE

        return self.eventType

    @property
    def peer(self):
        return self._peer

    @peer.setter
    def peer(self, peer: Peer):
        if peer != None:
            self._peer = peer
        
        return self._peer

    @property
    def packet(self):
        return self._packet
    
    @packet.setter
    def packet(self, packet: Packet):
        if packet:
            self._packet = packet
        
        else:
            raise DataError("Specify data. Expected -> Packet got -> NoneType")

        return self._packet

class Host:
    """
    Host(Address: address, int: peer_count)

    ATTRIBUTES

        Address: address            Address of the host
        int:     peer_count         all peer or client to be connected  
    """

    def __init__(self, address: Address=None, peer_count: int=0):
        self.address        = address
        self.peer_count     = peer_count

        try:

            citnet_obj = CitNet_TCP()
            self.citnet = citnet_obj.initialize()

        except socket.error as e:
            citnet_obj.deinitialize()
            raise e

        if self.address != None:
            try:
                self.citnet.bind((self.address.host, self.address.port))
    
            except socket.error as e:
                #print(e)
                if "an attempt was made to access a socket" in e:
                    print("It looks like port: {} is currently used by another process? try using different port")
                else:
                    print("cannot bind to socket with error: {}".format(e))
                
                self.citnet.close()
                sys.exit()

            self.citnet.listen(self.peer_count) # listen for (peer_count: int) possible connections.
            
        
    def connect(self, address: Address):
        if self.address != None:
            raise AddressError("Address has a value. Expected -> None.")

        if self.citnet != None:
            self.citnet.connect((address.host, address.port))

        return self.citnet

    def check_events(self):

        con, a = self.citnet.accept()
        receive = con.recv(2048)
        event = Event()
        peer  = Peer(self.citnet)

        if a:
            event.type = EventType.CITNET_EVENT_CONNECT
            peer.data = a
            event.peer = peer

        if receive:
            event.type = EventType.CITNET_EVENT_RECEIVE
            pack = Packet()
            pack.data = receive
            event.packet = pack

        return event

    def service(self, timeout: int = 0):

        if self.citnet != None:
            events = self.check_events()

        else:
            raise CitNetError("CitNet is not defined")

        time.sleep(timeout)

        return events
    
