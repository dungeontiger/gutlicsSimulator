import unittest
from engine.util import statMod

class TestUtil(unittest.TestCase):

  def testStatMod0(self):
    self.assertEqual(statMod(10), 0)

  def testStatModPositive(self):
    self.assertEqual(statMod(17), 3)

  def testStatModNegative(self):
    self.assertEqual(statMod(4), -3)

  def testStatMod5(self):
    self.assertEqual(statMod(5), -3)

  def testStatMod6(self):
    self.assertEqual(statMod(6), -2)

  def testStatMod7(self):
    self.assertEqual(statMod(7), -2)

  def testStatMod11(self):
    self.assertEqual(statMod(11), 0)

  def testStatMod18(self):
    self.assertEqual(statMod(18), 4)

  def testStatMod19(self):
    self.assertEqual(statMod(18), 4)

  def testStatMod20(self):
    self.assertEqual(statMod(20), 5)

if __name__ == '__main__':
    unittest.main() 
