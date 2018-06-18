import unittest
from engine.dice import Dice
class TestDice (unittest.TestCase):
  def testSimpleRoll(self):
    roller = Dice()
    value = roller.roll(1, 20, 0)
    self.assertTrue(value <= 20 and value >= 1, 'Value was {}'.format(value))

if __name__ == '__main__':
    unittest.main() 
