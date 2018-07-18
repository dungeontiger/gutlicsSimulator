# TODO: need a test for this class
class DamageEffect:
  def __init__(self, amount, type, target):
    self.amount = amount
    self.type = type
    self.target = target

  def getAmount(self):
    return self.amount

  def getType(self):
    return self.type

  def getTarget(self):
    return self.target

  def resolve(self):
    return self.target.applyDamageEffect(self)