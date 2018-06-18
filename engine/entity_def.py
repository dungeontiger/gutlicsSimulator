from .alignment import Alignment
class EntityDef:
  """ Encapsulates the definition of an enity """
  def __init__(self, yaml):
    self.name = yaml['name']
    if yaml['alignment'] == 'neutral evil':
      self.alignment = Alignment.neutral_evil

  def getName(self):
    return self.name