#imports packages that i need half of this code is stolen btw
import os
import discord
import random
import requests
import aiohttp
import time
import asyncio
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands
from quips import QUIPS
from dotenv import load_dotenv
random.seed(time.time())

# sets aliases loads stuf you know all that crap already
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix = "!", intents=intents)
TOKEN = os.getenv('TOKEN')

# notifies in the terminal when the bot is running also prints an image of 02
@client.event
async def on_ready():
    print("Bot's up and running")
    await client.tree.sync()
    print(f"Synced command(s)")
    print("--------------------")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⢰⠆⠀⠀⠀⠀⠈⠻⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⠁⡆⠀⠀⡘⠀⠀⠀⠀⠀⠀⡄⠈⠉⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⠘⠁⠀⠀⡇⠀⠀⠀⠀⡆⢀⣆⠀⠀⠀⢂⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⡟⢰⠀⠀⠀⡄⠀⠀⠀⢰⠇⢸⠛⡄⠀⠀⠘⡄⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⢸⣆⠀⢸⡇⠀⠀⠀⡿⠀⣼⠀⠱⡀⠀⠀⢳⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⡄⢸⡇⣀⠀⢰⣷⠀⣇⣀⠀⠱⡀⠀⠈⢧⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣾⣇⣿⠀⢸⢿⡀⠀⠈⠉⠙⠳⡀⠀⠈⢧⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠗⠒⢢⡄⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣽⡛⠀⠆⠸⢬⣷⣦⣍⣀⣀⠀⠱⣄⠀⠈⢧⣸⠀⠀⠀⠀⠀⠀⠀⠀⢠⡖⠛⠿⣧⠀⠀⠀⠀⠀⠀⠀⢠")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⢀⠀⠀⠀⠀⠀⠈⠙⠒⠓⠒⠛⠉⠀⠑⢄⣸⠀⠀⠀⢸⠁⠀⠀⠀⣼⡧⠃⢀⠟⠀⠀⠀⠀⠀⠀⠀⡀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠀⡇⠀⠀⠀⠀⠏⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠁")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀⠀⢸⠃⠀⠀⠀⢠⣤⣾⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⡟⠀⠀⠀⠀⢸⡇⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡗⠦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⢰⠃⠀⠀⠀⠀⡏⢇⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣄⠉⠒⠒⠒⠒⠂⠀⠀⠀⠀⠀⠀⠀⢰⠀⢀⡏⠀⠀⠀⠀⢸⣿⢻⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢘⢦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣸⠀⡼⠀⠀⠀⠀⢀⡿⣿⠸⡇⠀⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠠⠈⣆⠀⠀⠀⠀⣀⣀⣤⣴⠒⠛⢯⡇⣸⠁⠀⠀⠀⠀⡼⠀⣿⠐⢳⠀⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠈⠙⠉⠉⠉⣿⣿⣿⣿⣆⠀⣿⣱⠃⠀⠀⠀⠀⣴⣷⠎⢹⡀⠘⡄⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢷⠀⠀⡤⠀⢸⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢀⣼⡿⠃⠀⢸⡇⠀⢇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⢸⠀⢠⡇⠀⣿⣿⣿⣿⣿⣿⣿⠋⠀⠀⠀⣠⡾⠋⠀⠀⠀⠸⣇⠀⠸⣸⡇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠘⡆⣸⠁⢠⣿⣿⣿⣿⣿⠟⠁⠀⣀⠤⠚⠁⠀⠀⠀⠀⠀⠈⣿⠀⠀⢿⡇⠀⠀⠀⠀⠀⠀⠀⠀")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⣵⡟⠀⢸⣿⣿⣿⡟⠁⠔⠊⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡇⠀⠘⣇⠀⠀⠀⠀⠀⠀⠀⠀")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name= 'the voices'), status=discord.Status.do_not_disturb)
# force sync commands
@client.command(name='sync')
async def sync(ctx):
    if ctx.author.id == 340271265707327488:
        await client.tree.sync()
        await ctx.send('command tree synced')
    else:
        await ctx.send('You arent the owner')
        return
# checks if the bots awake
@client.command()
async def botcheck(ctx):
    await ctx.send("i'm here")
# Rolls Dice from a d4 to d100!
@client.tree.command(name="ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}")

@client.tree.command(name="d20", description="rolls a 20 sided die")
async def d20(interaction: discord.Interaction):
    number = random.randint(1,20)
    if number == (1):
        await interaction.response.send_message(f'{interaction.user.mention} **NAT 1**')
    elif number == (20):
        await interaction.response.send_message(f'{interaction.user.mention} ** NAT 20 GYATT**')
    else:
        await interaction.response.send_message(f'{interaction.user.mention} rolled a **d20** and got a **{number}**')

@client.tree.command(name="d12", description="rolls a 12 sided die")
async def d12(interaction: discord.Interaction):
    number = random.randint(1,12)
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d12** and got a **{number}**')

@client.tree.command(name="d10", description="rolls a 10 sided die")
async def d10(interaction: discord.Interaction):
    number = random.randint(1,10)
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d10** and got a **{number}**')

@client.tree.command(name="d8", description="rolls a 8 sided die")
async def d8(interaction: discord.Interaction):
    number = random.randint(1,8)
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d8** and got a **{number}**')

@client.tree.command(name="d6", description="rolls a 6 sided die")
async def d6(interaction: discord.Interaction):
    number = random.randint(1,6)
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d6** and got a **{number}**')

@client.tree.command(name="d4", description="rolls a 4 sided die")
async def d4(interaction: discord.Interaction):
    number = random.randint(1,4)
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d4** and got a **{number}**')

@client.tree.command(name="d100", description="rolls a 100 sided die")
async def d100(interaction: discord.Interaction):
    number = random.randint(1,100) 
    await interaction.response.send_message(f'{interaction.user.mention} rolled a **d100** and got a **{number}**')

@client.command(name = "ban")
async def ban(ctx, member: discord.Member):
    if ctx.author.id == 340271265707327488 or ctx.author.id == 649296073042427904:
        await ctx.send(f'banning {member.mention} in 30 seconds')
        await asyncio.sleep(10)
        await ctx.send(f'banning {member.mention} in 20 seconds')
        await asyncio.sleep(10)
        await ctx.send(f'banning {member.mention} in 10 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 9 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 8 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 7 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 6 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 5 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 4 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 3 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 2 seconds')
        await asyncio.sleep(1)
        await ctx.send(f'banning {member.mention} in 1 seconds')
        await asyncio.sleep(1)
        await ctx.send(f"Get that ass banned, {member.mention}!")
        await asyncio.sleep(3)
        await member.ban(reason=f"Banned by {ctx.author}")
    else:
        await ctx.send("You are not authorized to use this command.")
# runs the script using the specified token from another file 
client.run(TOKEN)