from lib.runner import TaskRunner
from test import TestBaseLine
from test import TestTaskRunner
import unittest
import sys

def banner():
	''' Display the information banner '''
	print 'Welcome to Taskatron, known commands are as follows:'
	print 'test -- runs all of the unit tests'
	print 'load FILE_NAME -- runs the tasks in the provided file'

args = sys.argv
if len(args) >= 2: 
	command = args[1]

	if command.lower() == 'load':
		if len(args) >=3:
			filename =  args[2]

			if filename:
				task_runner = TaskRunner()
				task_runner.load_tasks_from_file(filename)
		else:
			print 'No filename specified for [load] command'
	else:
		# Start the unit tests
		suite = unittest.TestLoader().loadTestsFromTestCase(TestBaseLine)
		unittest.TextTestRunner(verbosity=2).run(suite)

		suite = unittest.TestLoader().loadTestsFromTestCase(TestTaskRunner)
		unittest.TextTestRunner(verbosity=2).run(suite)
else:
	banner()