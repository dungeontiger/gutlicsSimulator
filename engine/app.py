import os, yaml
from engine.entity_def import EntityDef
from engine.weapon_def import WeaponDef

# TODO: make a get app method so that it acts like a singleton

""" 
Singleton object that holds all the info for the simulator 
"""
class App:
  def __init__(self):
    # TODO: create a normal logger for software activities
    # read the entity definitions
    entityPath = 'engine/resources/entities'
    self.entityDefs = dict()
    self.weaponDefs = dict()
    for _, _, files in os.walk(entityPath):
      for filename in files:
        if filename.endswith('.yaml'):
          with open(entityPath + '/' + filename, 'rb') as str:
            y = yaml.load(str.read())
            self.entityDefs[y['name']] = EntityDef(y)
    # read the weapons
    with open('engine/resources/weapons.yaml') as w:
      y = yaml.load(w.read())
      for key in y:
        self.weaponDefs[key] = WeaponDef(key, y[key])

  """
  Get a particular entity definition
  """
  def getEntityDef(self, name):
    return self.entityDefs[name]

  def getWeaponDef(self, name):
    return self.weaponDefs[name]