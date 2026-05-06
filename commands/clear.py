import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Clear(lightbulb.SlashCommand, name="clear", description="Clear messages"):
    lines = lightbulb.integer("lines", "Number of lines you want to delete")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        lines = int(self.lines)
        channel = str(ctx.channel_id)
        msgs = await ctx.app.rest.fetch_messages(channel).limit(lines)
        await ctx.app.rest.delete_messages(channel, msgs)
        await ctx.respond(f'Deleted {lines} lines.', flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7