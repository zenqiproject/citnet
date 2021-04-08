
import socket
import random

class Address:

    """
    Main class for creating and handling addresses for CitNet.

    ATTRIBUTE:
        
        host:   str     = None -> A host for a server to bind to. If none, return local hostname
        port:   int     = None -> A port for a server to bind to. If none, return random port from range 1024 -> 49151
    
    """

    def __init__(self, host: str=None, port: int=None):
        self.host       = host
        self.port       = port

        if self.host == "" or self.host == None:
            self.host = socket.gethostbyname(socket.gethostname())

        elif self.port == None:
            self.port = random.randint(1024, 49151) # if the port is lower than 1024, it requires administrative previledges

