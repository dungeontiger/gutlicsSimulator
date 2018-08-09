from datetime import datetime

"""
Singleton to record a battle that can be played back or visualized
"""
class BattleRecorder:
  __instance = None

  # constructor
  def __init__(self):
    # create the singleton object on first access
    if BattleRecorder.__instance is None:
      BattleRecorder.__instance = BattleRecorder.__impl()
    self.__dict__['_Singleton__instance'] = BattleRecorder.__instance

  def __getattr__(self, attr):
    """ Delegate access to implementation """
    return getattr(self.__instance, attr)

  def __setattr__(self, attr, value):
      """ Delegate access to implementation """
      return setattr(self.__instance, attr, value)

  # implementation class for the singleton
  class __impl:
    def setRound(self, r):
      self.round = r

    def setInitTick(self, i):
      self.initiative = i

    # starts a battle
    def startBattle(self, name):
      self.round = 0
      self.initiative = 0
      # create the file
      f = './logs/battles/' + name + '_recorded_' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3] + '.csv'
      self.file = open(f, 'w')
      # write out the headers
      self.file.write('TIME\tROUND\tINITIATIVE_TICK\tFORCE\tENTITY_TYPE\tENTITY\tEVENT\tAMOUNT\tWITH\tFORCE2\tENTITY_TYPE2\tENTITY2\n')
      self._write(None, 'Start Battle', 0, '', None)

    # ends a battle
    def endBattle(self, forces):
      for f in forces:
        e = f.getRandomAliveEntity()
        if e is not None:
          self._write(e, 'Wins Battle', 0, '', None)
      self.file.close()

    # spawns an entity
    def spawn(self, entity):
      self._write(entity, 'Spawns', entity.getHP(), '', None)

    def criticalHits(self, entity, weapon, damage, target):
      self._write(entity, 'Critical Hits', damage, weapon.getName(), target)

    def hits(self, entity, weapon, damage, target):
      self._write(entity, 'Hits', damage, weapon.getName(), target)

    def misses(self, entity, weapon, target):
      self._write(entity, 'Misses', 0, weapon.getName(), target)

    def dies(self, entity):
      self._write(entity, 'Dies', 0, '', None)

    def takesDamage(self, entity, damage):
      self._write(entity, 'Takes Damage', damage, '', None)

    def _write(self, entity, event, amount, _with, entity2):
      t = datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3]
      force = ''
      entity_type = ''
      entity_name = ''
      force2 = ''
      entity_type2 = ''
      entity_name2 = ''
      if (entity is not None):
        force = entity.getForceName()
        entity_type = entity.getEntityDefName()
        entity_name = entity.getName()
      if (entity2 is not None):
        force2 = entity2.getForceName()
        entity_type2 = entity2.getEntityDefName()
        entity_name2 = entity2.getName()
      line = t + '\t' + str(self.round) + '\t' + str(self.initiative) + '\t' + force + '\t' + entity_type + '\t' + entity_name
      line = line + '\t' + event + '\t' + str(amount) + '\t' + _with + '\t' + force2 + '\t' + entity_type2 + '\t' + entity_name2 + '\n'
      self.file.write(line)