import warcraftAPI
import datetime
import pandas as pd
import numpy as np

df = pd.DataFrame()

#   2KMBwR79kP6fWZqC
dates = []
auth_token = warcraftAPI.get_new_token()
total_kills = 0
playerRankingLogs = warcraftAPI.getPlayerDmgOnOneBoss("Greezie", auth_token, 755)
all_kills = playerRankingLogs['data']['characterData']['character']['encounterRankings']['ranks']
for kill in all_kills:

    total_kills +=1
    peeps = {}
    attempts = 0
    report_code = kill['report']['code']
    startTime = kill['report']['startTime']
    startTime = datetime.datetime.fromtimestamp(startTime / 1000, tz=datetime.timezone.utc)
    print(startTime)
    log_of_fights = warcraftAPI.getFightIDs(report_code, auth_token)
    fights = log_of_fights['data']['reportData']['report']['fights']
    prevDate = 0
    for fight in fights:
        attempts+=1
        fight_id = fight['id']

        # get player IDS for this report
        playerNames = [0] * 1000
        shadowCrashHits = [0] * 1000
        playerInfo = warcraftAPI.getPlayerInfo(report_code, auth_token, fight_id)
        players = playerInfo['data']['reportData']['report']['playerDetails']['data']['playerDetails']
        healers = players['healers']
        for player in healers:
            playerNames[player['id']] = player['name']
            if not player['name'] in peeps:
                peeps[player['name']] = 0
        dps = players['dps']
        for player in dps:
            playerNames[player['id']] = player['name']
            if player['name'] == "Kazootie":
                print("KAZOOTIEEEEEEE")
            if not player['name'] in peeps:
                peeps[player['name']] = 0
        shadowCrashLog = warcraftAPI.getShadowCrash(report_code, auth_token, fight_id)
        crashes = shadowCrashLog['data']['reportData']['report']['events']['data']
        for crash in crashes:
            shadowCrashHits[crash['targetID']] += 1

        index = 0
        for hit in shadowCrashHits:
            if playerNames[index] != 0:
                peeps[playerNames[index]] += hit
            index+=1

    #print(peeps)
    date = startTime.date()
    dates.append(date)
    #date = str(date.month) + "/" + str(date.day) + '/' + str(date.year)
    for peep in peeps:
        df.loc[peep, date] = peeps[peep]
    #df2 = pd.DataFrame.from_dict(peeps)
    #print(df2)
    #print(attempts)


df.sort_index(axis=1, inplace=True)
dates.sort()
df_total = pd.DataFrame(columns=dates)
print(df_total)
print(df)
df.to_csv("shadowCrash.csv")
print(total_kills)
