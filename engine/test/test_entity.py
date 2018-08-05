import unittest
from engine.entity import Entity
from engine.entity_library import EntityLibrary

class TestEntity(unittest.TestCase):
  
  def testCreateGoblin(self):
    e = Entity(EntityLibrary().getEntity('goblin'), 'The Force')
    self.assertTrue(e.getMaxHP() >= 2 and e.getMaxHP() <= 12)

if __name__ == '__main__':
    unittest.main() 
