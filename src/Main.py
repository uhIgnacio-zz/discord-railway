import nextcord
import os

from nextcord.ext import commands

# Intents
intents = nextcord.Intents.default()

# Bot
bot = commands.Bot(prefix=os.environ.get('PREFIX'), allowed_mentions=None, )

# load cogs
if __name__ == '__main__':
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            bot.load_extension(f"{filename[:-3]}")


@bot.event
async def on_ready():
    print(f"{bot.user} | {bot.user.id}")

bot.run(os.environ('TOKEN'))
