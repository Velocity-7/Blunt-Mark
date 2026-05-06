import aiohttp, hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class ServerStatus(lightbulb.SlashCommand, name="server_status", description="Check the minecraft server status"):
    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
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
                    status_json = await response.json()    
                    if status_json['online']: 
                        await ctx.respond(server_online)
                    else:
                        await ctx.respond(server_offline) 
                else:
                    await ctx.respond(server_offline)

#Coded by Velocity7