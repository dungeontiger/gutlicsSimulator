class EntityWeaponAttack:
  def __init__(self, weapon, toHit, damage):
    self.weapon = weapon
    self.toHitMod = toHit
    self.damageMod = damage

  def getName(self):
    return self.weapon.getName()

  def getWeapon(self):
    return self.weapon

  def getToHitMod(self):
    return self.toHitMod

  def getDamageMod(self):
    return self.damageMod

  def isMelee(self):
    return self.weapon.isMelee()

  def rollDamage(self, criticalHit):
    return self.weapon.rollDamage(self.damageMod, criticalHit)

  def getDamageType(self):
    return self.weapon.getDamageType()