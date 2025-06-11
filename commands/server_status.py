import aiohttp, hikari, lightbulb

plugin = lightbulb.Plugin('server_status')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.command('server_status', 'Check the minecraft server status')
@lightbulb.implements(lightbulb.SlashCommand)
async def server_status(ctx): 
 server_offline = hikari.Embed(title='Server Status', colour='#FF0000')
 server_offline.add_field(':red_circle: The server is offline.', '‎')
 server_offline.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')

 server_online = hikari.Embed(title='Server Status', colour='#1FFF00')
 server_online.add_field(':green_circle: The server is online.', '‎')
 server_online.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')    

 api = 'https://api.mcstatus.io/v2/status/java/bluntmark.axenthost.me'
 async with aiohttp.ClientSession() as session:
  async with session.get(api) as response:
   if response.status == 200:
    server_status = await response.json()    
    if server_status['online']: 
     await ctx.respond(server_online)
    else:
     await ctx.respond(server_offline) 
   else:
    pass

#Coded by Velocity7