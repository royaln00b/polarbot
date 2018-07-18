import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
import random
from random import sample
import os


bot=commands.Bot(description="Polaris bot. This bot was brought to you by Royalnoob. Built from scratch.",command_prefix=";",pm_help=False)

bot.remove_command('help')


@bot.command(pass_context=True)
async def help(ctx):
	embed=discord.Embed(title="Command List" , description= "1 . ping - Shows latency of the bot\n2. unsub - Unsubscribe from notifications\n3. sub - Subscribe to notifications",colour = 0xEE82EE)
	await bot.send_message(ctx.message.author, embed=embed)

@bot.command(pass_context=True)
async def ping(ctx):
    chars = '0123456789ABCDEF'
    channel = ctx.message.channel
    t1 = time.perf_counter()
    await bot.send_typing(channel)
    t2 = time.perf_counter()
    embed=discord.Embed(title=None, description='Ping: {}ms'.format(round(((t2-t1)*1000)-100)), color = discord.Colour(int('0x'+''.join(sample(chars,6)),16)))
    await bot.say(embed=embed)


	
@bot.command(pass_context=True)
async def suggest(ctx,*,description):
	await bot.add_reaction(message = ctx.message, emoji = "✅")
	await bot.send_message(discord.utils.get(ctx.message.server.members, name='Royalnoob'),ctx.message.author.display_name+" suggested a command to be added:\n\n"+description)

@bot.command(pass_context=True)   
async def avatar(ctx,*, user:discord.Member=None):
   if user == None:
        user = ctx.message.author
   embed = discord.Embed (color=0xff0000)
   embed.set_image(url=user.avatar_url)
   await bot.say(embed=embed)


@bot.command(pass_context=True)
async def unsub(ctx):
	await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str("Members")))
	await bot.say("<@"+str(ctx.message.author.id)+"> you have unsubbed from notifications !")

@bot.command(pass_context=True)
async def sub(ctx):
	await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str("Members")))
	await bot.say("<@"+str(ctx.message.author.id)+"> you have subbed to notifications !")

@bot.command(pass_context=True)
async def start(ctx):
	await bot.move_role(ctx.message.server,discord.utils.get(ctx.message.server.roles,name=str("Manager")),80)

@bot.event
async def on_member_join(member):
	server = member.server
	fmt = '**You can stay here {0.mention} in {1.name} as long as you dont kill anyone**!'
	await bot.send_message(bot.get_channel("467462021412290561"), fmt.format(member, server))

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(type=0, name=';help'))

token = os.getenv('TOKEN')
bot.run(token)
