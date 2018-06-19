import unittest
from engine.dice import Dice

class TestDice (unittest.TestCase):
  """Test a single D20 roll """
  def testSimpleRoll(self):
    roller = Dice()
    value = roller.roll(1, 20, 0)
    self.assertTrue(value <= 20 and value >= 1, 'Value was {}'.format(value))

  """Test a roll of multiple dice """
  def testMultipleDice(self):
    roller = Dice()
    value = roller.roll(3,6,0)
    self.assertTrue(value <= 18 and value >= 3)

  """Test with a modifier """
  def testWithModifer(self):
    roller = Dice()
    value = roller.roll(1, 10, 5)
    self.assertTrue(value <= 15 and value >= 6)

  """Roll 100 times and ensure that the min and max are rolled, its possible to fail but unlikely """
  def testRoll100Times(self):
    roller = Dice()
    found1 = False
    found15 = False
    for _ in range (0, 100):
      value = roller.roll(2,8,-1)
      self.assertTrue(value <= 15 and value >= 1)
      if value == 1:
        found1 = True
      if value == 15:
        found15 = True
    self.assertTrue(found1, 'Did not roll a 1')
    self.assertTrue(found15, 'Did not roll a 15')

  """Test d20 roll"""
  def testD20(self):
    roller = Dice()
    value = roller.d20()
    self.assertTrue(value >= 1 and value <= 20)

  """Test d20 advantage roll"""
  def testD20Advantage(self):
    roller = Dice()
    value = roller.d20Advantage()
    self.assertTrue(value >= 1 and value <= 20)

  """Test d20 disadvantage roll"""
  def testD20Disadvantage(self):
    roller = Dice()
    value = roller.d20Disadvantage()
    self.assertTrue(value >= 1 and value <= 20)

  """Test rolling by string"""
  def testRollByString(self):
    roller = Dice()
    value = roller.rollString('3d6')
    self.assertTrue(value >= 3 and value <= 18)

  """Test rolling by string with a modifer """
  def testRollByStringMod(self):
    roller = Dice()
    value = roller.rollString('2d8-1')
    self.assertTrue(value >= 1 and value <= 15)

if __name__ == '__main__':
    unittest.main() 
