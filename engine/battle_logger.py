
from datetime import datetime

"""
Log events in the battle
In theory this could be used to play back a battle
"""
class BattleLogger:

  def __init__(self, name):
    # TODO: create the directory if it does not exist
    # TODO: fix time date format so recognized automatically by excel
    # just put them in the battle logs directory
    # file name will be battle name plus timestamp
    f = './logs/battles/' + name + '_' + str(datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f')) + '.csv'
    self.file = open(f, 'w')
    # write out the headers
    self.file.write('TIME\tROUND\tINITIATIVE_TICK\tFORCE\tENTITY_TYPE\tENTITY\tMESSAGE_TYPE\tMESSAGE\n')

  """
  Log a message
  """
  def msg(self, message, message_type = 'message', round = 0, initiative = 0, force = '', entityType = '', entity = ''):
    self.file.write(str(datetime.now()) + '\t' + str(round) + '\t' + str(initiative) + '\t' + force + '\t' + entityType + '\t' + entity + '\t' + message_type + '\t' + message + '\n')

  """
  Log a message using an entity reference
  """
  def entityMsg(self, message, message_type, entity, round = 0, initiative = 0):
    self.msg(message, message_type, round, initiative, entity.getForceName(), entity.getEntityDef().getName(), entity.getName())

  # seems to be needed for unit testing, but just in case we close it anyway
  """
  Close the log file
  """
  def close(self):
    self.file.close()