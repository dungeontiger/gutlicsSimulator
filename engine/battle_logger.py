
from datetime import datetime

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

  #TODO: Can I put this back to clean it up?
  def msg(self, message, message_type = 'message', round = 0, initiative = 0, force = '', entityType = '', entity = ''):
    self.file.write(str(datetime.now()) + '\t' + str(round) + '\t' + str(initiative) + '\t' + force + '\t' + entityType + '\t' + entity + '\t' + message_type + '\t' + message + '\n')

  def close(self):
    self.file.close()