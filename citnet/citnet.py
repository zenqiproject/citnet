#         Copyright (c) 2021, Zenqi. All rights reserved.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import socket
import sys

lass CitNet:
    """
    Main socket handler for both TCP and UDP.

    ATTRIBUTE
        socketFamily: socket.AddressFamily   = Address Family of socket. usually AF_INET
        socketType:   socket.SocketKind      = Socket Type of socket. SOCK_STREAM (TCP) SOCK_DGRAM (UDP)
        
    """
    
    addressFamily:  socket.AddressFamily  = None # default is AF_INET
    socketType:     socket.SocketKind     = None # SOCK_STREAM (TCP) SOCK_DGRAM (UDP)
    socketProto:    int                   = None # IPPROTO_*


    def __init__(self):
        pass

    def initialize(self):
        if self.socketType == socket.SOCK_STREAM:
            self.socketProto = socket.IPPROTO_TCP

        elif self.socketType == socket.SOCK_DGRAM:
            self.socketProto = socket.IPPROTO_UDP
    
        if self.addressFamily == None:
            self.socketFamily = socket.AF_INET
    
        if self.socketType != None:
            self.citnet = socket.socket(self.addressFamily, self.socketType, self.socketProto)
            self.citnet.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        else:
            raise TypeError("socketType and socketProto is required.")

        return self.citnet


    def deinitialize(self):
        if self.citnet:
            self.citnet.shutdown(1)
        else:
            sys.exit()

        return
