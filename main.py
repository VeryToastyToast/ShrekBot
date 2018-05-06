import discord
from discord.ext import commands
import random
import os

bot = commands.Bot(command_prefix='/')
bot.remove_command('help')

@bot.event
async def on_ready():
	print('HerobrineBot 0.1dev')
	print('')
	print('Logged in as:')
	print(bot.user.name)
	print('')
	print('Client User ID:')
	print(bot.user.id)
	print('')
	await bot.change_presence(game=discord.Game(name='I Am Bread'))

@bot.command()
async def help():
	await bot.say('__**ToastBot 1.3dev Commands:**__\n\n```css\n/help : Helps you out!\n/eat  : Eats\n/idk  : Gives Helpful Advice\n/choose  : Chooses\n/noob  : Call Out The Noobs\n/kill  : Kill Annoying People\n/resurrect  : Brings Your Friends Back To Life\n/kick  : Gets rid of dumb butts\n/echo  : Repeats whatever you say\n/toast : The most important thing you need to know\n```\n```\nJoin my Discord!\nhttps://discord.gg/NsPCv4A\n```')

@bot.command()
async def idk():
        await bot.say('Please Contact VeryToastyToast, MildlyWarmBread or SlightlyBurntToast With Any Questions. Thank You.')

@bot.command()
async def noob(*, mentioned = 'you'):
        await bot.say('Hey ' + (mentioned) + ' Your A NOOOOOOOOOOOOOOOOOOOOOOOB')

@bot.command()
async def kill(*, mentioned = 'You'):
	await bot.say((mentioned) + ' Ate Some Poisened Toast')

@bot.command()
async def toast():
	await bot.say('Sub To Team Toast Its ToastBot Approved')

@bot.command()
async def echo(*, message: str):
	await bot.say(message)
	
@bot.command()
async def choose(*, mentioned = 'You'):
        await bot.say('Go ' + (mentioned) + ' I Choose You')
        
@bot.command()
async def resurrect(*, mentioned = 'You'):
        await bot.say((mentioned) + ' Subscribed To Team Toast And Came Back To Life')

@bot.command()
async def eat():
        await bot.say('Om Nom Nom. Om.\nNom')

@bot.command(pass_context = True)
async def kick(ctx, userName: discord.User):
	try:
		if ctx.message.author.server_permissions.kick_members:
			await bot.kick(userName)
			await bot.say('Noob Just Betrayed Us')
		else:
			await bot.say('NO You Havent Eaten Enough Toast')
	except:
			await bot.say('Sorry, But I Cant Do That. Please Make Sure I Have Permission To Kick.')

bot.run(os.environ['TOKEN_DISCORD'])
