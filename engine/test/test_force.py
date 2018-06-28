import unittest, os
from engine.force import Force
from engine.app import App

class TestForce(unittest.TestCase):
  
  def setUp(self):
    self.app = App()

  def testName(self):
    force = Force('./engine/test/resources/forces/crimson.yaml', self.app)
    self.assertEqual(force.getName(), 'Crimson')

  def testDescription(self):
    force = Force('./engine/test/resources/forces/crimson.yaml', self.app)
    self.assertEqual(force.getDescription(), 'Collection of lowly goblins')
    
  def testNumberOfCreatures(self):
    force = Force('./engine/test/resources/forces/crimson.yaml', self.app)
    self.assertEqual(force.getNumberOfEntities(), 4)
