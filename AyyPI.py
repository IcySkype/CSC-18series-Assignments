import json, requests
from datetime import datetime

apikey = "1E5E2E4F003948C9A36B84FDA4718FA7"
steamid = "76561198089734417"
#player summary
url1 = "http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/"

params1 = dict(
    key = apikey,
    steamids = steamid,
    format = "json"
)

qry1 = requests.get(url=url1, params=params1).json()

def dispsummary():
    name = qry1["response"]["players"][0]["personaname"]
    profurl = qry1["response"]["players"][0]["profileurl"]
    avatar = qry1["response"]["players"][0]["avatar"]
    logoff = int(qry1["response"]["players"][0]["lastlogoff"])
    converttime = datetime.utcfromtimestamp(logoff).strftime('%Y-%m-%d %H:%M:%S')
    print("Steam Name: "+name)
    print("Profile URL: "+profurl)
    print("Avatar :"+avatar)
    print("Last Login: "+converttime)
dispsummary()

#game achievs
url2 = "http://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v0002/"
params2 = dict(
    key = apikey,
    steamid = steamid,
    appid = "218620",
    format = "json"
)

qry2 = requests.get(url=url2, params=params2).json()

def dispachievs():
    print qry2["playerstats"]["gameName"]+" Achievements"
    for achiev in range(0, len(qry2["playerstats"]["achievements"])):
        a_name = qry2["playerstats"]["achievements"][achiev]["name"]
        a_is_achieved = int(qry2["playerstats"]["achievements"][achiev]["achieved"])
        if a_is_achieved == 1:
            achieved = "Achieved"
        else:
            achieved = "Not Achieved"
        print a_name+": "+achieved
dispachievs()

