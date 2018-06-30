
from .entity_state import EntityState
# represents an instantiated entity
# TODO:  can I do global scope singletons or something?'
class Entity:
  def __init__(self, entityDef, forceName):
    # entity def is a string, find the correct one from the list
    self.entityDef = entityDef
    self.maxHP = self.entityDef.rollHP()
    self.HP = self.maxHP
    self.forceName = forceName
    self.state = EntityState.normal
    # default the name to the entity defintiion
    self.name = self.getEntityDef().getName()

  def isStillFighting(self):
    return self.state != EntityState.dead and self.state != EntityState.fled

  def getEntityDef(self):
    # returns entity def object
    return self.entityDef
    
  def getEntityDefName(self):
    # returns entity def object
    return self.entityDef.getName()

  def getMaxHP(self):
    return self.maxHP

  def getHP(self):
    return self.HP

  def getInitiative(self):
    return self.initative

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

  def takeTurn(self, enemyForce):
    # a list of tuples, message type and message
    # will be displayed in the battle log
    msgs = list()
    # does this entity have a target that is not dead or fled?
    # if yes continue with this target
    # if not randomly choose another target from the enemy force that is not dead or fled
    return msgs