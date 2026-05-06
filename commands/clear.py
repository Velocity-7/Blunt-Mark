import hikari, lightbulb

loader = lightbulb.Loader()

@loader.command
class Clear(lightbulb.SlashCommand, name="clear", description="Clear messages"):
    lines = lightbulb.integer("lines", "Number of lines you want to delete")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        import __main__
        if ctx.guild_id:
            guild = ctx.client.app.cache.get_guild(ctx.guild_id)
            if guild and ctx.user.id != guild.owner_id:
                raise __main__.NotOwner()
        else:
            await ctx.respond("This command can only be used in a server.", flags=hikari.MessageFlag.EPHEMERAL)
            return

        import datetime
        
        lines = int(self.lines)
        fourteen_days_ago = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=14)
        raw_msgs = await ctx.client.app.rest.fetch_messages(ctx.channel_id).limit(lines)
        msgs = [m for m in raw_msgs if m.created_at >= fourteen_days_ago]
        
        if len(msgs) == 1:
            await ctx.client.app.rest.delete_message(ctx.channel_id, msgs[0])
        elif len(msgs) > 1:
            await ctx.client.app.rest.delete_messages(ctx.channel_id, msgs)
            
        await ctx.respond(f'Deleted {len(msgs)} lines.', flags=hikari.MessageFlag.EPHEMERAL)

#Coded by Velocity7