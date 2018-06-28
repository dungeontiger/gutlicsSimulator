import unittest
from engine.entity import Entity
from engine.app import App

class TestEntity(unittest.TestCase):
  
  def setUp(self):
    self.app = App()

  def testCreateGoblin(self):
    e = Entity(self.app.getEntityDef('goblin'))
    self.assertTrue(e.getMaxHP() >= 2 and e.getMaxHP() <= 12)