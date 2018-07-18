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
	embed=discord.Embed(title="Command List" , description= "1 . ping - Shows latency of the bot\n2. unsub - Unsubscribe from notifications\n3. sub - Subscribe to notifications\n4. channel - Choose your channels!",colour = 0xEE82EE)
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

@bot.event
async def on_member_join(member):
	server = member.server
	fmt = '**You can stay here {0.mention} in {1.name} as long as you dont kill anyone**!'
	await bot.send_message(bot.get_channel("467462021412290561"), fmt.format(member, server))
	await bot.add_roles(member,discord.utils.get(ctx.message.server.roles,name=str("Members")))
#----------------------------------------------------------------------------------------------------------
#                                              AUTO ASSIGN ROLES CODE
channels = ["chat","hangout","memes","toxic","fanstalk","gaming","trading","sports"]
@bot.command(pass_context=True)
async def channel(ctx,action,*,channel):
	failembed=discord.Embed(title="ERROR",description="`"+action+"` or "+"`"+channel+"` Could not be found. Please try again.",colour=0xFF0000)
	addembed=discord.Embed(title="Success!",description="You have been added to the "+channel+" channels! Have fun!",colour=0x00FF00)
	removeembed=discord.Embed(title="Success!",description="You have been removed from the "+channel+" channels! Have fun!",colour=0xBDB76B)
	if action == "remove":
		actions = "removed from"
		if channel in channels:
			await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(channel)))
			await bot.say(embed = removeembed)
		else:
			await bot.say(embed = failembed)
	elif action == "add":
		actions = "added to"
		if channel in channels:
			await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str(channel)))
			await bot.say(embed = addembed)
		else:
			await bot.say(embed = failembed)
	elif action != "remove":
		if action != "add":
			await bot.say(embed = failembed)
	

#----------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------
#                                              ADMIN COMMANDS
adminlist = ["manager"]
any(x in adminlist for [y.name.lower() for y in ctx.message.author.roles])
@bot.command(pass_context=True)
async def purge(ctx,num: int):
	if any(x in adminlist for [y.name.lower() for y in ctx.message.author.roles]):
		await bot.purge_from(ctx.message.channel,limit=num)
	else:
		await bot.say("No")

#----------------------------------------------------------------------------------------------------------



@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(type=0, name=';help'))

token = os.getenv('TOKEN')
bot.run(token)
