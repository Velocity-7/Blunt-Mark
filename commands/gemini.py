import hikari, lightbulb, os
from google import genai

client = genai.Client(api_key=os.environ.get('GEMINI_API_KEY'))
loader = lightbulb.Loader()

@loader.command
class Gemini(lightbulb.SlashCommand, name="gemini", description="Interact with Gemini"):
    prompt = lightbulb.string("prompt", "Enter a prompt")

    @lightbulb.invoke
    async def invoke(self, ctx: lightbulb.Context) -> None:
        await ctx.defer(ephemeral=True)
        prompt_str = str(self.prompt)
        try:
            response = await client.aio.models.generate_content(
                model='gemini-3.6-flash',
                contents=f'Strictly without using any bullet points or other formatting options answer this keep it under 150 words: {prompt_str}'
            )
            text = response.text
            if text and len(text) > 2000:
                text = text[:1997] + "..."
            await ctx.respond(text)
        except Exception as e:
            await ctx.respond(f"An error occurred: {str(e)[:1900]}")

#Coded by Velocity7