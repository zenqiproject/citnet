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

import struct
import enum


class Packet:
    """
    Create a new packet object that can be sent or receive.

    ATTRIBUTE:
        data:   bytes   =   a byte object that act as a main data for packet that can be packed or unpack
    """

    receivedPacket = None
    dataLength: int     = 0
    version: int        = 1

    def __init__(self, _data: str=None):
    
        if _data != None:
            self._data = bytes(_data, "utf-8")
            self.dataLength = len(self._data)

    
    def create(self):
        return self._data

    @property
    def data(self): # property for received data
        return self.receivedPacket

    @data.setter
    def data(self, receve_data=None):
        if receve_data != None:
            self.receivedPacket = receve_data
        
        else:
            raise DataError("Specify data. Expected -> receive_data got -> NoneType")

        return self.receivedPacket

