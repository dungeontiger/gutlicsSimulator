import unittest
from engine.app import App
from engine.battle import Battle

class TestBattle(unittest.TestCase):

  def setUp(self):
    self.app = App()

  def testForces(self):
    forces = ['./engine/test/resources/forces/crimson.yaml', './engine/test/resources/forces/ebony.yaml']
    battle = Battle(forces, self.app)
    self.assertEqual(len(battle.getForces()), 2)
    battle.end()

  def testBattle(self):
    forces = ['./engine/test/resources/forces/crimson.yaml', './engine/test/resources/forces/ebony.yaml']
    battle = Battle(forces, self.app)
    # TODO: test something here
    battle.start()
    battle.end()

  def testInitiativeMap(self):
    battle = Battle(['./engine/test/resources/forces/crimson.yaml', './engine/test/resources/forces/ebony.yaml'], self.app)
    battle.rollInitiative()
    a, lowest, highest = battle.createInitMap()
    # TODO: Test each creature has one and only one initiative slot
    # TODO: Test lowest and highest correct
    for i in range(1,31):
      if i in a:
        for e in a[i]:
          print(str(i) + ': ' + e.getName())
      else:
        print(str(i) + ': none')
    print(highest)
    print(lowest)
    battle.end()

if __name__ == '__main__':
    unittest.main() 
