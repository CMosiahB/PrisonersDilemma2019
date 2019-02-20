import random 
def move(my_history, their_history, my_score, their_score):
  team_name = 'I am Grootman'
  team_strategy =  'Merciless until merciful'
  strategy_description = 'If they have more, betray, if they have less, betray, if they loose multiple times, collude. If they betray the last time, betray again. '
  if len(their_history)==0:
    return 'c'
  elif (my_score) < (their_score):
    return 'b'
  elif (my_score) > (their_score):
    return 'c' 
  else:
    return 'b'
