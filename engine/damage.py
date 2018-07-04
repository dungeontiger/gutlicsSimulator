class Damage:
  def __init__(self, entity, damage, type):
    self.entity = entity
    self.damage = damage
    self.type = type

  def getEntity(self):
    return self.entity

  def getDamage(self):
    return self.damage

  def getType(self):
    return self.type