class EntityWeaponAttack:
  def __init__(self, weapon, toHit, damage):
    self.weapon = weapon
    self.toHitMod = toHit
    self.damageMod = damage

  def getWeapon(self):
    return self.weapon

  def getToHitMod(self):
    return self.toHitMod

  def getDamageMod(self):
    return self.damageMod

  def isMelee(self):
    return self.weapon.isMelee()

  def rollDamage(self, criticalHit):
    return self.rollDamage(criticalHit) + self.damageMod

  def getDamageType(self):
    return self.weapon.getDamageType()