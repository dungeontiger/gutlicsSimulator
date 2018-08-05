import unittest
from engine.weapon_library import WeaponLibrary

class TestWeaponLibrary(unittest.TestCase):

  def testGetInstance(self):
    wl = WeaponLibrary()
    self.assertIsNotNone(wl)

  def testSingleton(self):
    wl1 = WeaponLibrary().getWeapons()
    wl2 = WeaponLibrary().getWeapons()
    # the wrapping objects are different but the underlying impls are the same
    self.assertTrue(wl1 is wl2)

  def testSpear(self):
    spear = WeaponLibrary().getWeapon('spear')
    self.assertIsNotNone(spear)
    self.assertTrue(spear.getDamage() == '1d6')

if __name__ == '__main__':
    unittest.main() 
