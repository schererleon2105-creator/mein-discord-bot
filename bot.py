import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f'✅ {bot.user} ist online!')
    
    # Alle Cogs laden (außer __init__.py)
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py") and filename != "__init__.py":
            try:
                await bot.load_extension(f"cogs.{filename[:-3]}")
                print(f"✅ Cog geladen: {filename}")
            except Exception as e:
                print(f"❌ Fehler beim Laden von {filename}: {e}")
    
    # Slash Commands synchronisieren
    try:
        synced = await bot.tree.sync()
        print(f"✅ {len(synced)} Slash Commands synchronisiert!")
    except Exception as e:
        print(f"Sync Fehler: {e}")

    await bot.change_presence(activity=discord.Game(name="XL Service!"))
# Cog neu laden (nur für dich)
@bot.command()
@commands.is_owner()
async def reload(ctx):
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await bot.reload_extension(f"cogs.{filename[:-3]}")
    await ctx.send("✅ Alle Cogs neu geladen!")

if __name__ == "__main__":
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("❌ Token nicht gefunden!")
    else:
        bot.run(token)