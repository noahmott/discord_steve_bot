import discord
from discord import app_commands
from openai import OpenAI
import os
from config import DISCORD_TOKEN, OPENAI_API_KEY

class JokeBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        # Create OpenAI client as a class attribute
        self.openai_client = OpenAI(api_key=OPENAI_API_KEY)

    async def setup_hook(self):
        # This is called when the bot starts
        try:
            await self.tree.sync()
            print("Successfully synced commands")
        except Exception as e:
            print(f"Failed to sync commands: {e}")

client = JokeBot()

@client.tree.command(name="stevejoke", description="Get an AI-generated Steve Pruitt joke")
async def steve_joke(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        response = client.openai_client.chat.completions.create(
            model="gpt-4o",  # Make sure this matches your OpenAI subscription
            messages=[
                {"role": "system", "content": (
                    "You are an AI assistant that provides humorous one-liner jokes about Steve Pruitt, highlighting his bad luck and lack of skills."
                )},
                {"role": "user", "content": (
                    "Generate a short, funny jokes that are the opposite of Chuck Norris jokes and replace Chuck Norris with Steve Pruitt. The joke should be one or two sentences long."
                )}
            ],
            max_tokens=150,
            temperature=0.7
        )
        joke = response.choices[0].message.content.strip()
        await interaction.followup.send(joke)
    except Exception as e:
        await interaction.followup.send("Sorry, I couldn't generate a joke right now. Try again later!")
        print(f"Error generating joke: {str(e)}")

@client.tree.command(name="stevecompliment", description="Get an AI-generated compliment about Steve Pruitt")
async def steve_compliment(interaction: discord.Interaction):
    await interaction.response.defer()
    try:
        response = client.openai_client.chat.completions.create(
            model="gpt-4o",  # Make sure this matches your OpenAI subscription
            messages=[
                {"role": "system", "content": (
                    "You are an AI assistant that provides humorous one-liner compliments about Steve Pruitt, highlighting "
                    "his over-the-top abilities."
                )},
                {"role": "user", "content": (
                    "Generate a short, funny Chuck Norris style joke and replace Chuck Norris with Steve Pruitt. The joke should be one or two sentences long."
                )}
            ],
            max_tokens=150,
            temperature=0.7
        )
        compliment = response.choices[0].message.content.strip()
        await interaction.followup.send(compliment)
    except Exception as e:
        await interaction.followup.send("Sorry, I couldn't generate a compliment right now. Try again later!")
        print(f"Error generating compliment: {str(e)}")

@client.event
async def on_ready():
    print(f'Bot is ready! Logged in as {client.user}')
    print(f'Bot ID: {client.user.id}')
    print('------')

if __name__ == "__main__":
    # Get port from environment variable for Heroku
    port = int(os.environ.get('PORT', 8080))
    
    try:
        client.run(DISCORD_TOKEN)
    except Exception as e:
        print(f"Failed to start bot: {e}")
