import datetime

class Task():
	''' This is the shell for any generic task '''

	def __init__(self, raw_task):
		self.depends = raw_task.get('depends', None)
		self.name = raw_task.get('name', None)
		self.instructions = raw_task.get('instructions', None)
		self.success = None
		self.completion_time = None
		self.start_time = None
		self.running = None

	def start(self):
		''' This will start running the task '''
		self.running = True
		self.start_time = datetime.datetime.now()

		if (self.instructions):
			try:
				print 'Task [%s] output [%s]' % (self.name, eval(self.instructions))
				self.success = True
			except Exception as e:
				print e
				self.success = False

		self.running = False
		self.completion_time = datetime.datetime.now()

		print 'Task [%s] completed in [%d]' % (self.name, (self.completion_time - self.start_time).total_seconds())

	def __str__(self):
		return self.name

	def __repr__(self):
		return self.name