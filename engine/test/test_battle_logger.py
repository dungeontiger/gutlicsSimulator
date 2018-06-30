import unittest
from engine.battle_logger import BattleLogger

class TestBattleLogger(unittest.TestCase):
  
  def testBattleLogger(self):
    bl = BattleLogger('Crimson vs Ebony')
    self.assertIsNotNone(bl)
    bl.close()

  def testWriteMessage(self):
    bl = BattleLogger('Crimson vs Ebony')
    bl.msg('Battle Started')
    # TODO: check file contents
    self.assertIsNotNone(bl)
    bl.close()

  def testFullMessage(self):
    #TODO: check order make sure output matches column headers
    bl = BattleLogger('Crimson vs Ebony')
    bl.msg('Goblin bit the dust', 'death', 1, 15, 'Crimson', 'goblin', 'goblin_12')
    # TODO: check file contents
    self.assertIsNotNone(bl)
    bl.close()
    