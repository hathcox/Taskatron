from lib.task import Task
from lib.runner import TaskRunner
import unittest


class TestBaseLine(unittest.TestCase):

    def setUp(self):
        self.runner = TaskRunner()
        
    def test_simple_json(self):
    	self.runner.load_tasks_from_file('examples/single_task.json')

