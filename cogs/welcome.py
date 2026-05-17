import discord
from discord.ext import commands
from datetime import datetime

class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Willkommens-Nachricht
    @commands.Cog.listener()
    async def on_member_join(self, member):
        # Sucht nach einem Channel namens "willkommen", "welcome" oder nutzt den System-Channel
        channel = discord.utils.get(member.guild.text_channels, name="willkommen") or \
                   discord.utils.get(member.guild.text_channels, name="welcome") or \
                   member.guild.system_channel
        
        if channel:
            embed = discord.Embed(
                title="👋 Willkommen auf dem Server!",
                description=f"{member.mention} ist gerade beigetreten!",
                color=0x00ff00,
                timestamp=datetime.now()
            )
            embed.set_thumbnail(url=member.display_avatar.url)
            embed.add_field(name="User ID", value=member.id, inline=True)
            embed.add_field(name="Account erstellt", value=member.created_at.strftime("%d.%m.%Y"), inline=True)
            embed.set_footer(text=f"Willkommen {member.name}!")
            
            await channel.send(embed=embed)

    # Leave-Nachricht
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="willkommen") or \
                   discord.utils.get(member.guild.text_channels, name="welcome") or \
                   member.guild.system_channel
        
        if channel:
            embed = discord.Embed(
                title="😢 Verlassen",
                description=f"{member.name} hat den Server verlassen.",
                color=0xff0000,
                timestamp=datetime.now()
            )
            await channel.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Welcome(bot))