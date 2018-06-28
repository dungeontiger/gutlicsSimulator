import unittest
from engine.app import App

class TestApp(unittest.TestCase):

  def testApp(self):
    app = App()
    self.assertIsNotNone(app)

  def testGoblinDef(self):
    app = App()
    goblin = app.getEntityDef('goblin')
    self.assertTrue(goblin.getName() == 'goblin')

if __name__ == '__main__':
    unittest.main() 
