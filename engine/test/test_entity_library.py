import unittest
from engine.entity_library import EntityLibrary

class TestEntityLibrary(unittest.TestCase):

  def testGetInstance(self):
    el = EntityLibrary()
    self.assertIsNotNone(el)

  def testSingleton(self):
    el1 = EntityLibrary().getEntities()
    el2 = EntityLibrary().getEntities()
    # the wrapping objects are different but the underlying impls are the same
    self.assertTrue(el1 is el2)

  def testGnoll(self):
    gnoll = EntityLibrary().getEntity('gnoll')
    self.assertIsNotNone(gnoll)
    self.assertTrue(gnoll.getHD() == '5d8')

if __name__ == '__main__':
    unittest.main() 
