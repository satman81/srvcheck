from . import Task, minutes

MIN_PEERS = 2

class TaskChainLowPeer(Task):
	def __init__(self, conf, notification, system, chain):
		super().__init__('TaskChainLowPeer', conf, notification, system, chain, chain.BLOCKTIME * 2, minutes(5))

	def isPluggable(conf):
		return True

	def run(self):
		p = self.chain.getPeerNumber()

		if int(p) < MIN_PEERS:
			return self.notify('Chain has only %s peers %s' % (p, self.notification.PEERS_EMOJI))
		
		return False
		

