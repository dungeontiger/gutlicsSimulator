from .alignment import Alignment
from .dice import Dice
from .util import *

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
    self.str = yaml['stats']['str']
    self.dex = yaml['stats']['dex']
    self.con = yaml['stats']['con']
    self.int = yaml['stats']['int']
    self.wis = yaml['stats']['wis']
    self.cha = yaml['stats']['cha']
    # TODO: need to finish alignment
    if yaml['alignment'] == 'neutral evil':
      self.alignment = Alignment.neutral_evil

  def rollHP(self):
    return self.dice.rollString(self.hd)

  def rollInitiative(self):
    return statMod(self.dex) + self.dice.d20()

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