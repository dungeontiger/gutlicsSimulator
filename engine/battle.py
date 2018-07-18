from datetime import datetime

from .force import Force
from .battle_logger import BattleLogger

""" 
Manages a battle between forces 
Currently forces are limited to two
In the future more than two forces will be allowed
"""
class Battle:
  def __init__(self, forces, app):
    # TODO: Assert only two forces for now
    self.app = app

    # load forces, an array of file names
    self.forces = []
    for f in forces:
      self.forces.append(Force(f, app))

    # create a battle log with the name of the two forces
    self.battlename = self.forces[0].getName() + ' vs ' + self.forces[1].getName()
    self.battlelogger = BattleLogger(self.battlename)

    # set the names of each entity
    for f in self.forces:
      i = 0
      for e in f.getEntities():
        i = i + 1
        e.setNameSuffix(str(i))

    # write out hp of all entities to log
    for f in self.forces:
      for e in f.getEntities():
        self.battlelogger.msg(str(e.getHP()), 'hp', 0, '', f.getName(), e.getEntityDef().getName(), e.getName())

  """
  Returns the array of forces
  """
  def getForces(self):
    return self.forces

  """ 
  Main loop for the battle 
  """
  def start(self):
    # roll initiative for each creature
    # start the rounds, look until one force is defeated
    # create the initiative map
    self.rollInitiative()
    initMap, lowestI, highestI = self.createInitMap()
    round = 0
    while self.continueBattle():
      round = round + 1
      # TODO: to prevent infinite loop go for 100 rounds
      if (round > 100):
        break
      self.battlelogger.msg('Starting new round: ' + str(round))
      for i in range(highestI + 1, lowestI, -1):
        if i in initMap:
          self.battlelogger.msg('Initiative tick: ' + str(i))
          el = initMap[i]
          resolutions = list()
          for e in el:
            if e.isStillFighting():
              # this entity takes its turn, returns some messages to log
              msgs, rs = e.takeTurn(self.getEnemyForce(e))
              resolutions = resolutions + rs
              for m in msgs:
                self.battlelogger.entityMsg(m[2], m[1], m[0], round, i)
          # all entities in this initiative tick had a chance, resolve the effects
          resMsg = []
          for r in resolutions:
            resMsg = r.resolve()
            for m in resMsg:
              self.battlelogger.entityMsg(m[2], m[1], m[0], round, i)

  """
  Tell each entity to roll its initative
  """
  def rollInitiative(self):
    self.battlelogger.msg('Rolling Initiative')
    for f in self.forces:
      for e in f.getEntities():
        i = e.rollInitiative()
        self.battlelogger.entityMsg(str(i), 'initiative', e, 0, '')

  """
  Get the opposing force of an entity
  """
  def getEnemyForce(self, e):
    # return the force that does not match the one this entity is in
    for f in self.forces:
      if f.getName() != e.getForceName():
        return f
    # TODO: This needs to be an exception
    return self.forces[0]

  """
  Determine if the battle is over or not
  """
  def continueBattle(self):
    for f in self.forces:
      if f.isDefeated():
        return False
    return True

  """
  Creates a map to manage initiative order
  Key is the initative number
  """
  def createInitMap(self):
    # make a map where the key  is the initiative number
    # each value is a list of entities that have this initiative and resolve simaltaneously
    lowest = 100
    highest = -100
    a = dict()
    for f in self.forces:
      for e in f.getEntities():
        i = e.getInitiative()
        if i > highest:
          highest = i
        if i < lowest:
          lowest = i
        if i not in a:
          a[i] = list()
        a[i].append(e)
    return a, lowest, highest

  """
  End the battle
  """
  def end(self):
    self.battlelogger.close()
    # write out a battle summary
    # TODO do configuration, should this place write out summary or should be other class?
    with open('./logs/battles/' + self.battlename + '_summary_' + datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')[:-3] + '.csv', 'w') as f:
      f.write('FORCE\tENTITY\tSTATE\tHP\t\n')
      for force in self.forces:
        for e in force.getEntities():
          f.write(force.getName() + '\t' + e.getName() + '\t' + e.getState().name + '\t' + str(e.getHP()) + '\n')
      
    # Sizes and how much space they take up
    # T S M L H G
    # T 1/4 (4 per square)
    # S / M same 1 (5' x 5')
    # L 10' x 10'
    # H 15' x 15'
    # G 20' x 20'