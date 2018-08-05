import yaml, os
from .entity_def import EntityDef
"""
Singleton class to contain the list of weapons
"""
class EntityLibrary:
  # the singleton instance
  __instance = None

  # constructor
  def __init__(self):
    # create the singleton object on first access
    if EntityLibrary.__instance is None:
      EntityLibrary.__instance = EntityLibrary.__impl()

    # Store instance reference as the only member in the handle
    # TODO: what does this do?
    self.__dict__['_Singleton__instance'] = EntityLibrary.__instance

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
      entityPath = 'engine/resources/entities'
      self.entities = {}
      for _, _, files in os.walk(entityPath):
        for filename in files:
          if filename.endswith('.yaml'):
            with open(entityPath + '/' + filename, 'rb') as str:
              y = yaml.load(str.read())
              self.entities[y['name']] = EntityDef(y)

    def getEntities(self):
      return self.entities

    def getEntity(self, name):
      return self.entities[name]