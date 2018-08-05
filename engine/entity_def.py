from .alignment import Alignment
from .dice import Dice
from .util import *
from .weapon_library import WeaponLibrary
"""
Represents one type of entity, stats from Monster Manual mostly
"""
class EntityDef:
  """ Encapsulates the definition of an entity """
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
    weaponLib = WeaponLibrary()
    actions = yaml['actions']
    for a in actions:
      # each action itself is a dictionary
      # there will only be one key
      key = list(a.keys())[0]
      wd = weaponLib.getWeapon(key)

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