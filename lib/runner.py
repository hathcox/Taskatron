import json
from pprint import pprint
from lib.task import Task

class TaskRunner():
	''' This is the singleton class that launches all of your tasks '''

	def __init__(self):
		self.loaded_tasks = []
		self.task_list = []
		

	def load_tasks_from_file(self, filename):
		json_data=open(filename)

		raw_tasks = json.load(json_data)
		json_data.close()

		print 'Loaded [%d] tasks from [%s]' % (len(raw_tasks), filename)
		self.build_task_list(raw_tasks)


	def start_tasks(self):
		''' This will actually kick of all of the tasks, 
		assumes that loaded_tasks is populated '''

		for task in self.task_list:
			self.run_task(task)

	def find_task_by_name(self, name):
		''' Right now this assumes the task will exist '''
		return next((task for task in self.loaded_tasks if task.name == name), None)

	def find_dependencies(self, task):
	    if task in self.task_list:
	        return

	    if task.depends:
	    	dependency_task = self.find_task_by_name(task.depends)
	    	if (dependency_task):
	    		self.find_dependencies(dependency_task)
	    	else:
	    		print 'Couldn\'t find dependency task [%s]' % (task.depends)

	    self.task_list.append(task)


	def build_task_list(self, raw_tasks):
		''' This will actually construct the correct 
			task list from the tasks loaded '''

		#load all of the tasks into memory
		for raw_task in raw_tasks:
			task = Task(raw_task)
			self.loaded_tasks.append(task)
		

		#build the dependency graph
		for task in self.loaded_tasks:
			self.find_dependencies(task)

		print 'Dependency tree is :'
		print self.task_list

		self.start_tasks()


	def run_task(self, task):
		try:
			task.start()
		except Exception as e:
			print 'Error running task [%s] ' % task.name
			print e

			