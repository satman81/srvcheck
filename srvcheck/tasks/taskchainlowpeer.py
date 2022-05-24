from ..notification import Emoji
from . import Task, minutes

MIN_PEERS = 2

class TaskChainLowPeer(Task):
	def __init__(self, confSet, notification, system, chain):
		super().__init__('TaskChainLowPeer', confSet, notification, system, chain, chain.BLOCKTIME * 2, minutes(5))

	def isPluggable(conf):
		return True

	def run(self):
		p = self.chain.getPeerCount()

		if p < MIN_PEERS:
			return self.notify('chain has only %s peers %s' % (p, Emoji.Peers))
		
		return False
		

