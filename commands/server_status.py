import aiohttp, hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class ServerStatus(lightbulb.SlashCommand, name="server_status", description="Check the minecraft server status"):
    server_ip = lightbulb.string("server_ip", "The IP address of the Minecraft server")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        ip = str(self.server_ip)
        api = f'https://api.mcstatus.io/v2/status/java/{ip}'
        
        async with aiohttp.ClientSession() as session:
            async with session.get(api) as response:
                if response.status == 200:
                    status_json = await response.json()    
                    if status_json.get('online'):
                        version = status_json.get('version', {}).get('name_clean', 'Unknown')
                        players_online = status_json.get('players', {}).get('online', 0)
                        players_max = status_json.get('players', {}).get('max', 0)
                        motd = status_json.get('motd', {}).get('clean', 'A Minecraft Server')
                        
                        server_online = hikari.Embed(title=f'Server Status: {ip}', colour='#1FFF00')
                        server_online.add_field(':green_circle: The server is online', '‎')
                        server_online.add_field('Version', version, inline=True)
                        server_online.add_field('Players', f"{players_online}/{players_max}", inline=True)
                        server_online.add_field('MOTD', motd, inline=False)
                        server_online.set_thumbnail(f'https://api.mcstatus.io/v2/icon/{ip}')    
                        
                        await ctx.respond(server_online)
                    else:
                        server_offline = hikari.Embed(title=f'Server Status: {ip}', colour='#FF0000')
                        server_offline.add_field(':red_circle: The server is offline', '‎')
                        server_offline.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
                        await ctx.respond(server_offline) 
                else:
                    server_offline = hikari.Embed(title=f'Server Status: {ip}', colour='#FF0000')
                    server_offline.add_field(':red_circle: The server is offline or API returned an error.', '‎')
                    server_offline.set_thumbnail('https://cdn.discordapp.com/attachments/971651606204522506/1129751247776387152/Blunt_Mark-1_1.png')
                    await ctx.respond(server_offline)

#Coded by Velocity7