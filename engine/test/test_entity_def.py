import unittest, json, yaml
from engine.entity_def import EntityDef

class TestEntityDef(unittest.TestCase):

  def setUp(self):
    with open('./engine/test/resources/goblin.yaml', 'rb') as str:
      self.goblin_yaml = yaml.load(str.read())
    
  def test_name(self):
    someMob = EntityDef(self.goblin_yaml)
    self.assertEqual(someMob.getName(), 'goblin')

if __name__ == '__main__':
    unittest.main() 
