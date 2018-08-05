import yaml
from .weapon_def import WeaponDef
"""
Singleton class to contain the list of weapons
"""
class WeaponLibrary:
  # the singleton instance
  __instance = None

  # constructor
  def __init__(self):
    # create the singleton object on first access
    if WeaponLibrary.__instance is None:
      WeaponLibrary.__instance = WeaponLibrary.__impl()

    # Store instance reference as the only member in the handle
    # TODO: what does this do?
    self.__dict__['_Singleton__instance'] = WeaponLibrary.__instance

  def __getattr__(self, attr):
    """ Delegate access to implementation """
    return getattr(self.__instance, attr)

  def __setattr__(self, attr, value):
      """ Delegate access to implementation """
      return setattr(self.__instance, attr, value)

  # implementation class for the singleton
  class __impl:
    # constructor
    def __init__(self):
      # read the weapons
      self.weapons = {}
      with open('engine/resources/weapons.yaml') as w:
        y = yaml.load(w.read())
        for key in y:
          self.weapons[key] = WeaponDef(key, y[key])

    def getWeapons(self):
      return self.weapons

    def getWeapon(self, name):
      return self.weapons[name]
