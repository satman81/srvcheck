from . import Task 

class TaskChainStuck(Task):
	def __init__(self, notification, system, chain):
		super().__init__('TaskChainStuck', notification, system, chain, self.chain.BLOCK_TIME * 2, 5)
		self.prev = self.chain.getBlockHash()

	def run(self):
		bh = self.chain.getBlockHash()
		if bh == self.prev:
			self.notify('Chain is stuck at block %s' % bh)
		
		self.markChecked()