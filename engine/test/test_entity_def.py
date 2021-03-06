import unittest, json, yaml
from engine.entity_def import EntityDef

class TestEntityDef(unittest.TestCase):

  def setUp(self):
    with open('./engine/resources/entities/goblin.yaml', 'rb') as str:
      goblin_yaml = yaml.load(str.read())
      self.goblin = EntityDef(goblin_yaml)

  # TODO: test roll initiaitve

  #TODO: test stats

  def test_name(self):
    self.assertEqual(self.goblin.getName(), 'goblin')

  def testRollHP(self):
    hp = self.goblin.rollHP()
    self.assertTrue(hp >= 2 and hp <= 12)

  def testInitative(self):
    i = self.goblin.rollInitiative()
    self.assertTrue(i > 0)

if __name__ == '__main__':
    unittest.main() 
