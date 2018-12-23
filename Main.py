import pandas as pd
import numpy as np

from urllib.request import urlopen
from bs4 import BeautifulSoup
path = 'C:\\Users\\hovdei\\Desktop\\BovadaLines'
odds = pd.read_csv(path)
#odds = pd.read_csv('SBR_NBA_Lines.csv')
#print(odds)
oddsheaders = list(odds.columns.values)
#print(oddsheaders)

#b,c,d,e = pd.read_html('https://www.basketball-reference.com/leagues/NBA_2019.html')
stat = pd.read_html('http://www.espn.com/nba/statistics/team/_/stat/offense-per-game')
tcomp = pd.read_html('http://www.espn.com/nba/statistics/team/_/stat/team-comparison-per-game')
rebound = pd.read_html('http://www.espn.com/nba/statistics/team/_/stat/rebounds-per-game')
defense = pd.read_html('http://www.espn.com/nba/statistics/team/_/stat/defense-per-game')
misc = pd.read_html('http://www.espn.com/nba/statistics/team/_/stat/miscellaneous-per-game')
nbastuffer = pd.read_html('https://www.nbastuffer.com/2018-2019-nba-team-stats/')#0 for season, 1 for 5, 2 for road, 3 for home
#print(nbastuffer[2].iloc[0]['GP'])

headers = list(nbastuffer[0].columns.values)
#print(headers)
headers2 = list(nbastuffer[1].columns.values)
#print(headers2)
#print(stat)
#test = (stat[0].iloc[21][1])
sched= pd.read_html('http://www.espn.com/nba/schedule')
a = 0
#search = 'New Orleans'
#print(stat[0][1].where(stat[0][1] == search))
#testsearch = (stat[0][stat[0][1] == search])
#print(testsearch)
#print(testsearch[3])
#r = float(testsearch[3])
#rfloat = float(r)
#print(r/2)

print('Scores:')
#ALL CODE WILL BE IN FOR LOOP WHICH WILL CYCLE THROUGH EACH GAME
for i in range(10):
    tempaway = sched[0].iloc[a]['matchup']
    temphome = sched[0].iloc[a]['Unnamed: 1']
    away = tempaway[:-4]
    if away == 'LA':
        away = 'LA Clippers'
    if away == 'Los Angeles':
        away = 'LA Lakers'
    if away == 'Utah ':
        away = 'Utah'
    if away == 'New Orlean':
        away = 'New Orleans'
    if away == 'San Antoni':
        away = 'San Antonio'
    home = temphome[:-4]
    if home == 'LA':
        home = 'LA Clippers'
    if home == 'Los Angeles':
        home = 'LA Lakers'
    if home == 'New Yor':
        home = 'New York'
    if home == 'San Antoni':
        home = 'San Antonio'
    if home == 'Golden Stat':
        home = 'Golden State'
    if home == 'Utah ':
        home = 'Utah'
    #ESPN STATS http://www.espn.com/nba/statistics/team/_/stat/offense-per-game
    osa = (stat[0][stat[0][1] == away]) #asa = offense search away
    osh = (stat[0][stat[0][1] == home]) #osh = offense search home
    tca = (tcomp[0][tcomp[0][1] == away]) #tca = teamp comparison away
    tch = (tcomp[0][tcomp[0][1] == home]) #tca = teamp comparison home
    ra = (rebound[0][rebound[0][1] == away]) #rebound away
    rh = (rebound[0][rebound[0][1] == home])  # rebound home
    da = (defense[0][defense[0][1] == away]) #defense away
    dh = (defense[0][defense[0][1] == home])  # defense home
    ma = (misc[0][misc[0][1] == away])
    mh = (misc[0][misc[0][1] == home])
    #NBA STUFFER STATS https://www.nbastuffer.com/2018-2019-nba-team-stats/
    nbassa = (nbastuffer[0][nbastuffer[0]['TEAM'] == away]) #nba stuffer season away
    nbassh = (nbastuffer[0][nbastuffer[0]['TEAM'] == home]) #nba stuffer season home
    nbasl5a = (nbastuffer[1][nbastuffer[1]['TEAM'] == away]) #nba stuffer last 5 away
    nbasl5h = (nbastuffer[1][nbastuffer[1]['TEAM'] == home]) #nba stuffer last 5 home
    nbasra = (nbastuffer[2][nbastuffer[2]['TEAM'] == away]) #nba stuffer away
    nbashh = (nbastuffer[3][nbastuffer[3]['TEAM'] == home]) #nba stuffer home

    hrebound = float(rh[4])
    arebound = float(ra[4])
#    print(hrebound)

    shomepace = float(nbassh['PACEPaceEstimate of Possessions Per 48 Minutes'])
    sawaypace = float(nbassa['PACEPaceEstimate of Possessions Per 48 Minutes'])
    l5homepace = float(nbasl5h['PACEPaceEstimate of Possessions Per 48 Minutes'])
    l5awaypace = float(nbasl5a['PACEPaceEstimate of Possessions Per 48 Minutes'])
    pace = (l5homepace * 2 + l5awaypace *2 + shomepace + sawaypace)/6

    shomeoeff = float(nbassh['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    l5homeoeff = float(nbasl5h['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    hhomeoeff = float(nbashh['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    homeoeff = (shomeoeff + l5homeoeff * 2 + hhomeoeff)/4

    sawayoeff = float(nbassa['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    l5awayoeff = float(nbasl5a['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    aawayoeff = float(nbasra['OEFFOffensive EfficiencyPoints scored per 100 possessions.'])/100
    awayoeff = (sawayoeff + l5awayoeff * 2 + aawayoeff)/4

    shomedeff = float(nbassh['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    l5homedeff = float(nbasl5h['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    hhomedeff = float(nbashh['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    homedeff = (shomedeff + l5homedeff * 2 + hhomedeff) / 4

    sawaydeff = float(nbassa['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    l5awaydeff = float(nbasl5a['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    aawaydeff = float(nbasra['DEFFDefensive EfficiencyPoints allowed per 100 possessions.']) / 100
    awaydeff = (sawaydeff + l5awaydeff * 2 + aawaydeff) / 4

    homeavg = (homeoeff + awaydeff)/2
    awayavg = (awayoeff + homedeff)/2

    sa4fh = float(nbassh['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    l5a4fh = float(nbasl5h['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    hha4fh = float(nbashh['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    a4fh = 1 + (sa4fh + l5a4fh * 2 + hha4fh)/4

    sa4fa = float(nbassa['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    l5a4fa = float(nbasl5a['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    hha4fa = float(nbasra['A4FAdjusted Four FactorsCalculated by applying weights to the differentials of offensive and defensive four factors. A4F explains the specified proportion of variability in wins.'])
    a4fa = 1 + (sa4fa + l5a4fa * 2 + hha4fa)/4


    homescore = int(homeavg * pace * a4fh)
    awayscore = int(awayavg * pace * a4fa)

    home1 = home
    away1 = away

    #COMPARE TO LINES
    if home1 == 'LA Lakers':
        home1 = 'L.A. Lakers'
    if home1 == 'LA Clippers':
        home1 = 'L.A. Clippers'
    if away1 == 'LA Clippers':
        away1 = 'L.A. Clippers'
    hodds = (odds[odds['team'] == home1])
    aodds = (odds[odds['team'] == away1])
#    print(hodds)
    aspread = float(aodds['rl_BVD_line'])
    hspread = float(hodds['rl_BVD_line'])
    hodd = float(hodds['rl_BVD_odds'])
    aodd = float(aodds['rl_BVD_odds'])
    boverunder = float(hodds['tot_BVD_line'])
    hml = float(hodds['ml_BVD'])
    aml = float(aodds['ml_BVD'])
    if homescore > awayscore:
        hmlpyth = (homescore**16.5)/(homescore**16.5 + awayscore**16.5)*100
        if hodd < 0:
            hmlbovada = (-(hml) / ((-(hml)) + 100)) * 100
            if (hmlpyth - hmlbovada > 3):
                w = 3
#                print("ml value")
#                print(hmlpyth)
#                print(hmlbovada)

    if boverunder > (homescore + awayscore):
        ou = 2
    elif boverunder < (homescore + awayscore):
        ou = 1
    else:
        ou = 3

    if (homescore + hspread) > awayscore:
       homescore2 = homescore + hspread
       hpyth = (homescore2**16.5)/(homescore2**16.5 + awayscore**16.5)*100
       if hodd < 0:
          hbovada = (-(hodd)/((-(hodd))+100))*100
          if (abs(hpyth - hbovada) > 0):
#              print(hpyth,hbovada)
              pick = 1
#             print(home1,hspread,'----',away,awayscore,"at",home,homescore)
#           print('bet home')
    elif (awayscore + aspread) > homescore:
        awayscore2 = awayscore + aspread
        apyth = (awayscore2 ** 16.5) / (homescore ** 16.5 + awayscore2 ** 16.5) * 100
        if aodd < 0:
            abovada = (-(aodd) / ((-(aodd)) + 100)) * 100
            if (abs(apyth-abovada) > 0):
#                print(apyth,abovada)
                pick = 2
#                print(away1,aspread,'----',away,awayscore,"at",home,homescore)
    else:
        pick = 3
#        print("Push, no pick",'----',away,awayscore,"at",home,homescore)
#    print(hspread)
#    print(away,awayscore,"at",home,homescore)
    if (ou == 1) and (pick ==1):
        print(home1,hspread,'----','Over',boverunder,'----',away,awayscore,"at",home,homescore)
    elif (ou == 2) and (pick == 1):
        print(home1, hspread, '----', 'Under', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 3 and pick == 1:
        print(home1, hspread, '----', 'Push, no pick for', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 1 and pick == 2:
        print(away1, aspread, '----', 'Over', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 2 and pick == 2:
        print(away1, aspread, '----', 'Under', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 3 and pick == 2:
        print(away1, aspread, '----', 'Push, no pick for', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 1 and pick == 3:
        print('Push', '----', 'Over', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 2 and pick == 3:
        print('Push', '----', 'Under', boverunder, '----',away, awayscore, "at", home, homescore)
    elif ou == 3 and pick == 3:
        print('Push', '----', 'Push, no pick for', boverunder, '----',away, awayscore, "at", home, homescore)
    else:
        print("mistake")
    a = a+1
