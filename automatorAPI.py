from lcu_driver import Connector

connector = Connector()

toBan = []
toPick = []

@connector.ready
async def connect(connection):
    print('LCU API is ready to be used.')
    summoner = await connection.request('get', '/lol-summoner/v1/current-summoner')
    print(await summoner.json())

@connector.close
async def disconnect(connection):
    print('Finished task')
    await connector.stop()    

@connector.ws.register('/lol-matchmaking/v1/ready-check', event_types = ('UPDATE',))
async def readyCheck(connection, event):
    if event.data['state'] == 'InProgress' and event.data['playerResponse'] == 'None':
        await connection.request('post', '/lol-matchmaking/v1/ready-check/accept')

@connector.ws.register('/lol-champ-select/v1/session', event_types = ('UPDATE',))
async def readyCheck(connection, event):
    teamIntent = []
    for teammate in event.data['myTeam']:
        teamIntent.append(teammate.data['championPickIntent'])

connector.start()