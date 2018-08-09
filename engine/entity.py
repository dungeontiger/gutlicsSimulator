from .damage_type import DamageType
from .entity_state import EntityState
from .dice import Dice
from .damage_effect import DamageEffect
from .battle_recorder import BattleRecorder

"""
Represents an instance of an entity def
e.g., Goblin_23 of goblin
"""
class Entity:
  def __init__(self, entityDef, forceName):
    # entity def is a string, find the correct one from the list
    self.entityDef = entityDef
    self.maxHP = entityDef.rollHP()
    self.HP = self.maxHP
    self.AC = entityDef.getAC()

    self.forceName = forceName
    self.state = EntityState.normal
    self.targetEntity = None
    self.dice = Dice()
    # default the name to the entity defintiion
    self.name = self.getEntityDef().getName()
    self.battleRecorder = BattleRecorder()

  """
  Is this entity still fighting
  """
  def isStillFighting(self):
    # TODO: this check should be in the EntityState class I think
    return self.state != EntityState.dead and self.state != EntityState.fled

  """
  Get the entity definition for this entity
  """
  def getEntityDef(self):
    # returns entity def object
    return self.entityDef
  
  """
  Shortcut to get the entity definition name
  """
  def getEntityDefName(self):
    # returns entity def object
    return self.entityDef.getName()

  """
  Get the maximum hp for this entity as rolled when it was created
  """
  def getMaxHP(self):
    return self.maxHP

  """
  Get the current hp for this entity
  """
  def getHP(self):
    return self.HP

  """
  Get the current ac of the entity
  """
  def getAC(self):
    return self.AC

  """
  Get the initative of this entity
  """
  def getInitiative(self):
    return self.initative

  """
  Roll the initiative for this entity
  """
  def rollInitiative(self):
    self.initative = self.entityDef.rollInitiative()
    return self.initative

  def setNameSuffix(self, suffix):
    self.name = self.entityDef.getName() + '_' + suffix
    return self.name

  def getName(self):
    return self.name

  def getForceName(self):
    return self.forceName

  def getState(self):
    return self.state

  """
  This is where the entity takes actions
  It is called once per turn in initative order
  """
  def takeTurn(self, enemyForce):
    # a list of tuples, entity, message type and message
    # will be displayed in the battle log
    msgs = []
    # a list of things that happened to entities that needs to be resolved
    # at the end of the initiative tick
    resolutions = []
    if self.targetEntity == None or not self.targetEntity.isStillFighting():
      self.targetEntity = enemyForce.getRandomAliveEntity()
    if self.targetEntity != None:
      msgs.append((self, 'select target', 'Selecting target ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ')'))
      # the target can still be null if the force has not viable targets left
      # TODO: need to make a weapon or attack choice
      resolutions = self.makeWeaponAttack(self.targetEntity, None, enemyForce, msgs)
    return msgs, resolutions

  """
  Make an attack with a weapon
  """
  def makeWeaponAttack(self, target, weapon, enemyForce, msgs):
    weapon = self.selectWeapon()
    resolutions = []
    d20 = self.dice.d20()
    if d20 == 20:
      # automatic hit, critical hit
      msgs.append((self, 'attack critical hit', 'Hit ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ') with fists'))
      # roll critical hit damage and apply to resolution stack on target
      dmg = weapon.rollDamage(True)
      msgs.append((self, 'dealt damage', 'Dealt ' + str(dmg) + ' to ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ') with fists'))
      self.battleRecorder.criticalHits(self, weapon, dmg, target)
      resolutions.append(DamageEffect(dmg, DamageType.bludgeoning, self.targetEntity))
    elif d20 + weapon.getToHitMod() >= target.getAC():
      # normal hit
      msgs.append((self, 'attack hit', 'Hit ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ') with fists'))
      # roll damage and apply to resolution stack on target
      dmg = weapon.rollDamage(False)
      msgs.append((self, 'dealt damage', 'Dealt ' + str(dmg) + ' to ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ') with fists'))
      self.battleRecorder.hits(self, weapon, dmg, target)
      resolutions.append(DamageEffect(dmg, weapon.getDamageType(), self.targetEntity))
    else:
      # a swing and a miss!
      msgs.append((self, 'attack miss', 'Missed ' + self.targetEntity.getName() + ' (' + enemyForce.getName() + ') with fists'))
      self.battleRecorder.misses(self, weapon, target)
    return resolutions

  def applyDamageEffect(self, effect):
    # TODO: check for resistance and immunity
    msgs = []
    self.HP = self.HP - effect.getAmount()
    self.battleRecorder.takesDamage(self, effect.getAmount())
    msgs.append((self, 'damage taken', str(effect.getAmount())))
    if (self.HP <= 0):
      self.HP = 0
      self.state = EntityState.dead
      self.battleRecorder.dies(self)
      msgs.append((self, 'died', 'This entity is dead.'))
    return msgs

  """
  Choose which weapon to use, for now just use first melee weapon found
  """
  def selectWeapon(self):
    for w in self.entityDef.getWeapons():
      if (w.isMelee() == True):
        return w
    return None
