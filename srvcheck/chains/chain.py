import requests 

def rpcCall(url, method, params=[]):
    d = requests.post(url, json={'jsonrpc': '2.0', 'id': 1, 'method': method, 'params': params}).json()
    return d['result']

class Chain:
    NAME = ""
    BLOCKTIME = 10
    TASKS = []

    def __init__(self, conf):
        self.conf = conf

    ### Abstract methods
    def detect():
        """ Checks if the current server is running this chain """
        raise Exception('Abstract detect()')

    def getLatestVersion(self):
        """ Returns the latest version """
        raise Exception('Abstract getLatestVersion()')

    def getVersion(self):
        """ Returns software version """
        raise Exception('Abstract getVersion()')

    def getHeight(self):
        """ Returns the block height """
        raise Exception('Abstract getHeight()')

    def getBlockHash(self):
        """ Returns the block height """
        raise Exception('Abstract getHeight()')

    def getPeerCount(self):
        """ Returns the number of peers """
        raise Exception('Abstract getPeerCount()')

    def getNetwork(self):
        """ Returns network used """
        raise Exception('Abstract getNetwork()')

    def isStaking(self):
        """ Returns true if the node is staking """
        raise Exception('Abstract isStaking()')