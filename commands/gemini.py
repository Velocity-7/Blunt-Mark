import hikari, lightbulb, google.generativeai

google.generativeai.configure(api_key='API_KEY')
model = google.generativeai.GenerativeModel('gemini-1.5-flash')
plugin = lightbulb.Plugin('gemini')

def load(bot):
 bot.add_plugin(plugin)

@plugin.command
@lightbulb.add_checks(lightbulb.owner_only)
@lightbulb.option('prompt', 'Enter a prompt')
@lightbulb.command('gemini', 'Interact with Gemini')
@lightbulb.implements(lightbulb.SlashCommand)
async def clear(ctx):
 prompt = str(ctx.options.prompt)
 response = model.generate_content(f'{prompt}')
 await ctx.respond(response.text,  flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7