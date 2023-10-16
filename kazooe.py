import warcraftAPI
import datetime
import pandas as pd
import numpy as np

#745 - 757
auth_token = warcraftAPI.get_new_token()
total_damage = 0
count = 0
playerName = "jabes"
"""
for boss_id in range(745, 758):

    log = warcraftAPI.getPlayerDmgOnOneBoss(playerName, auth_token, boss_id)
    all_fights = log['data']['characterData']['character']['encounterRankings']['ranks']
    for fight in all_fights:
        amount = fight['amount']
        duration = fight['duration'] / 1000
        damage = amount * duration
        total_damage = total_damage + damage

for boss_id in [629, 633, 641, 645]:

    log = warcraftAPI.getPlayerDmgOnOneBoss(playerName, auth_token, boss_id)
    all_fights = log['data']['characterData']['character']['encounterRankings']['ranks']
    for fight in all_fights:
        amount = fight['amount']
        duration = fight['duration'] / 1000
        damage = amount * duration
        dt = datetime.datetime.fromtimestamp(fight['startTime'] / 1000, tz=datetime.timezone.utc)
        print(dt.day)
        total_damage = total_damage + damage
        count += 1
        """
boss_id = 1118
log = warcraftAPI.getPlayerDmgOnOneBoss(playerName, auth_token, boss_id)
all_fights = log['data']['characterData']['character']['encounterRankings']['ranks']
for fight in all_fights:
    amount = fight['amount']
    duration = fight['duration'] / 1000
    damage = amount * duration
    dt = datetime.datetime.fromtimestamp(fight['startTime'] / 1000, tz=datetime.timezone.utc)
    print(dt)
    total_damage = total_damage + damage
    count += 1


a =23


print(total_damage)
print(count)