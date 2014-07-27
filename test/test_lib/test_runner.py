from lib.runner import TaskRunner
from lib.task import Task
import unittest
from mock import patch, Mock, MagicMock

class TestTaskRunner(unittest.TestCase):

	def setUp(self):
		self.runner = TaskRunner()

	def do_nothing(self):
		pass

	def test_build_task_list(self):
		raw_tasks = [{"name": "A","instructions": "1"},{"name": "C","instructions": "3","depends": "B"},{"name": "B","instructions": "2","depends": "A"}]
	
		self.runner.start_tasks = MagicMock(return_value=None)
		self.runner.build_task_list(raw_tasks)

		self.assertEqual(len(self.runner.loaded_tasks), 3)
		self.assertEqual(len(self.runner.task_list), 3)

	def test_fail_build_task_list(self):
		raw_tasks = [{"name": "A","instructions": "1", "depends":"B"}]
		self.runner.start_tasks = MagicMock(return_value=None)
		self.runner.build_task_list(raw_tasks)

		self.assertEqual(len(self.runner.loaded_tasks), 1)
		self.assertEqual(len(self.runner.task_list), 1)


	def test_task_by_name(self):
		raw_task = {"name": "A","instructions": "1", "depends":"B"}
		task = Task(raw_task)
		self.runner.loaded_tasks = [task]

		self.assertEqual(len(self.runner.loaded_tasks), 1)
		self.assertEqual(self.runner.find_task_by_name('A'), task)




