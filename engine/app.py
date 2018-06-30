""" Singleton object that holds all the info for the simulator """
import os, yaml
from engine.entity_def import EntityDef

# TODO: make a get app method so that it acts like a singleton

class App:
  def __init__(self):
    # TODO: create a normal logger for software activities
    # read the entity definitions
    entityPath = 'engine/resources/entities'
    self.entityDefs = dict()
    for _, _, files in os.walk(entityPath):
      for filename in files:
        if filename.endswith('.yaml'):
          with open(entityPath + '/' + filename, 'rb') as str:
            y = yaml.load(str.read())
            self.entityDefs[y['name']] = EntityDef(y)
    # read the weaspons

  def getEntityDef(self, name):
    return self.entityDefs[name]