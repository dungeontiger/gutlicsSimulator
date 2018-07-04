import yaml, re
from .entity import Entity

""" 
Represents one side in a battle 
"""
class Force:
  def __init__(self, file, app):
    # read the yaml file
      with open(file, 'rb') as str:
        y = yaml.load(str.read())
        self.name = y['name']
        self.description = y['description']
        self.entities = list()
        # read in and process all the entities
        for e in y['entities']:
          # check for a number first, if there is create that many entities
          # by default there is only one (if not number provided)
          # TODO: what is num is < 1?
          # TODO: could be more robust with regex but could not get it to work for some reason
          num = 1
          ent = e
          m = e.split(' ')
          if len(m) > 1:
            num = int(m[0])
            ent = m[1]
          for _ in range(0, num):
            self.entities.append(Entity(app.getEntityDef(ent), self.name))

  def isDefeated(self):
    # if any one entity is still fighting this force is not defeated
    for e in self.entities:
      if e.isStillFighting():
        return False
    return True

  def getName(self):
    return self.name

  def getDescription(self):
    return self.description

  def getNumberOfEntities(self):
    return len(self.entities)

  def getEntities(self):
    return self.entities

  #TODO: get total hit points
  #TODO: get total EXP
  