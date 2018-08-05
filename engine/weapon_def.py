from .damage_type import DamageType
from .dice import Dice
import re
class WeaponDef:
  def __init__(self, name, yaml):
    self.roller = Dice()
    self.name = name
    self.damage = yaml['damage']
    self.damage_type = DamageType[yaml['damage_type']]
    self.weight = int(yaml['weight'])
    props = yaml['properties']
    self.finesse = 'finesse' in props
    self.light = 'light' in props
    self.twoHanded = 'two-handed' in props
    self.heavy = 'heavy' in props
    self.ammunition = False
    self.thrown = False
    for p in props:
      if p.startswith('ammunition'):
        self.ammunition = True
        m = re.search(r"\(range (\d*)\/(\d*)\)", p).groups()
        self.shortRange = int(m[0])
        self.longRange = int(m[1])
      if p.startswith('thrown'):
        self.thrown = True
        m = re.search(r"\(range (\d*)\/(\d*)\)", p).groups()
        self.shortRange = int(m[0])
        self.longRange = int(m[1])
      if p.startswith('versatile'):
        self.versatile = True
        m = re.search(r"versatile \((.*)\)", p).groups()
        self.versatileDamage = m[0]

  def rollDamage(self, modifier = 0, critical = False):
    # need to parse out dice to be able to do critical damage rolls
    return self.roller.rollString(self.damage) + modifier

  def getName(self):
    return self.name

  def getDamage(self):
    return self.damage

  def getDamageType(self):
    return self.damage_type
  
  def getWeight(self):
    return self.weight

  def getShortRange(self):
    return self.shortRange

  def getLongRange(self):
    return self.longRange