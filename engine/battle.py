from .force import Force
from .battle_logger import BattleLogger

""" Manages a battle between forces """
class Battle:
  def __init__(self, forces, app):
    # TODO: Assert only two forces for now
    self.app = app

    # load forces, an array of file names
    self.forces = []
    for f in forces:
      self.forces.append(Force(f, app))

    # create a battle log with the name of the two forces
    battlename = self.forces[0].getName() + ' vs ' + self.forces[1].getName()
    self.battlelogger = BattleLogger(battlename)

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

  def getForces(self):
    return self.forces

  """ Main loop for the battle """
  def start(self):
    # roll initiative for each creature
    # start the rounds, look until one force is defeated
     # create the initiative map
    self.rollInitiative()
    initMap, lowestI, highestI = self.createInitMap()
    round = 0
    while self.continueBattle():
     round = round + 1
     self.battlelogger.msg('Starting new round: ' + round)
     for i in range(highestI + 1, lowestI, -1):
       if i in initMap:
         el = initMap[i]
         for e in el:
           # this entity takes its turn, returns some messages to log
           msgs = e.takeTurn(self.getEnemyForce(e))
           for m in msgs:
             self.battlelogger.msg(m[0], m[1], round, i, e.getForceName(), e.getEntityDef().getName(), e.getName())

  def rollInitiative(self):
    self.battlelogger.msg('Rolling Initiative')
    for f in self.forces:
      for e in f.getEntities():
        i = e.rollInitiative()
        self.battlelogger.msg(str(i), 'initiative', 0, '', f.getName(), e.getEntityDef().getName(), e.getName())

  def getEnemyForce(self, e):
    # TODO: find the oppostive force to the one this entity is in
    return self.forces[0]

  def continueBattle(self):
    for f in self.forces:
      if f.isDefeated():
        return False
        #TODO: prevent infinite loop for now
    return False

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

  def end(self):
    self.battlelogger.close()
   
    # Sizes and how much space they take up
    # T S M L H G
    # T 1/4 (4 per square)
    # S / M same 1 (5' x 5')
    # L 10' x 10'
    # H 15' x 15'
    # G 20' x 20'