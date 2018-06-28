
# represents an instantiated entity
class Entity:
  def __init__(self, entityDef):
    # entity def is a string, find the correct one from the list
    self.entityDef = entityDef
    self.maxHP = self.entityDef.rollHP()
    self.HP = self.maxHP

  def getEntityDef(self):
    # returns entity def object
    return self.entityDef
    
  def getMaxHP(self):
    return self.maxHP

  def getHP(self):
    return self.HP