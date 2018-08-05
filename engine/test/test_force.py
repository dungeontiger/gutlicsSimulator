import unittest, os
from engine.force import Force

class TestForce(unittest.TestCase):
  
  def testName(self):
    force = Force('./engine/test/resources/forces/crimson.yaml')
    self.assertEqual(force.getName(), 'Crimson')

  def testDescription(self):
    force = Force('./engine/test/resources/forces/crimson.yaml')
    self.assertEqual(force.getDescription(), 'Collection of lowly goblins')
    
  def testNumberOfCreatures(self):
    force = Force('./engine/test/resources/forces/crimson.yaml')
    self.assertEqual(force.getNumberOfEntities(), 4)

if __name__ == '__main__':
    unittest.main() 
