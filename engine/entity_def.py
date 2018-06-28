from .alignment import Alignment
from .dice import Dice
class EntityDef:
  """ Encapsulates the definition of an enity """
  def __init__(self, yaml):
    self.dice = Dice()
    self.name = yaml['name']
    # TODO: size
    self.type = yaml['type']
    self.subtype = yaml['subtype']
    self.speed = yaml['speed']
    self.hd = yaml['hd']
    self.ac = yaml['ac']
    # TODO: need to finish alignment
    if yaml['alignment'] == 'neutral evil':
      self.alignment = Alignment.neutral_evil

  def rollHP(self):
    return self.dice.rollString(self.hd)

  def getName(self):
    return self.name

  def getType(self):
    return self.type

  def getSubtype(self):
    return self.subtype

  def getSpeed(self):
    return self.speed

  def getAC(self):
    return self.ac

  def getHD(self):
    return self.hd