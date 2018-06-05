import discord
import asyncio
from discord.ext.commands import Bot
from discord.ext import commands
import time
import random
from random import sample


bot=commands.Bot(description="Polaris bot. This bot was brought to you by Royalnoob. Built from scratch.",command_prefix=";",pm_help=False)

bot.remove_command('help')


@bot.command(pass_context=True)
async def help(ctx):
	embed=discord.Embed(title="Command List" , description= "1 . ping - Shows latency of the bot\n2 . hello - If you are lonely\n3 . iamlist - Shows what roles you can assign\n4 . iam - To add yourself to a role in the list\n5 . iamnot - Remove a role from yourself from the list\n6. unsub - Unsubscribe from notifications\n\n Admin only :\n1 . kick - Kick a member\n2 . ban - Ban a member\n3 . paint - Force a member to be a color\n4 . unpaint - Force a member out of a color",colour = 0xEE82EE)
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
	await bot.send_message(discord.utils.get(ctx.message.server.members, name='Sesmic'),ctx.message.author.display_name+" suggested a command to be added:\n\n"+description)

@bot.command(pass_context=True)   
async def avatar(ctx,*, user:discord.Member=None):
   if user == None:
        user = ctx.message.author
   embed = discord.Embed (color=0xff0000)
   embed.set_image(url=user.avatar_url)
   await bot.say(embed=embed)

@bot.command()
async def hello():
	await bot.say("Hello")

@bot.command()
async def iamlist():
	await bot.say("The current available roles are : \n - red \n - blue \n - yellow \n - Rainbow")

@commands.has_role("Mod")
@bot.command()
async def kick(member:discord.Member):
    await bot.kick(member)
    
@commands.has_role("Admin")
@bot.command(pass_context=True)
async def ban(ctx,member:discord.Member):
    await bot.say('<@{}>, you have been banned'.format(member.id))
    await asyncio.sleep(1)
    await bot.ban(member)
    
@bot.command(pass_context=True)
async def iam(ctx,*,role):
	if role == "blue":
		await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Added "+role+"!")
	elif role == "yellow":
		await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Added "+role+"!")
	elif role == "red":
		await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Added "+role+"!")
	elif role == "Rainbow":
		await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Added "+role+"!")
		server = ctx.message.server
		chars = '0123456789ABCDEF'
		key = 'q'
		while key == 'q':
			await bot.edit_role(server,discord.utils.get(server.roles, name='Rainbow'), colour = discord.Colour(int('0x'+''.join(sample(chars,6)),16)))
			await asyncio.sleep (1)

	else:
		await bot.say("I could not find this role or you not have permissions to be this role")


@bot.command(pass_context=True)
async def unsub(ctx):
	await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str("EVERYONE")))
	await bot.say("<@"+str(ctx.message.author.id)+"> you have unsubbed from notifications !")

@bot.command(pass_context=True)
async def sub(ctx):
	await bot.add_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles,name=str("EVERYONE")))
	await bot.say("<@"+str(ctx.message.author.id)+"> you have subbed to notifications !")

@bot.command(pass_context=True)
async def iamnot(ctx,*,role):
	if role == "blue":
		await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Removed "+role+"!")
	elif role == "yellow":
		await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Removed "+role+"!")
	elif role == "red":
		await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Removed "+role+"!")
	elif role == "Rainbow":
		await bot.remove_roles(ctx.message.author,discord.utils.get(ctx.message.server.roles, name=str(role)))
		await bot.say("Removed "+role+"!")
	else:
		await bot.say("I could not find this role.")

@commands.has_role("Admin")
@bot.command(pass_context=True)
async def paint(ctx,member:discord.Member,*,role):
	if role == "blue":
		await bot.add_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "yellow":
		await bot.add_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "red":
		await bot.add_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "Rainbow":
		await bot.add_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
		server = ctx.message.server
		chars = '0123456789ABCDEF'
		key = 'q'
		while key == 'q':
			await bot.edit_role(server,discord.utils.get(server.roles, name='Rainbow'), colour = discord.Colour(int('0x'+''.join(sample(chars,6)),16)))
			await asyncio.sleep (1)

	else:
		await bot.say("I could not find this role")



@commands.has_role("Admin")
@bot.command(pass_context=True)
async def unpaint(ctx,member:discord.Member,*,role):
	if role == "blue":
		await bot.remove_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "yellow":
		await bot.remove_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "red":
		await bot.remove_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	elif role == "Rainbow":
		await bot.remove_roles(member,discord.utils.get(ctx.message.server.roles, name=str(role)))
	else:
		await bot.say("I could not find this role.")

@bot.event
async def on_member_join(member):
	server = member.server
	fmt = '**You can stay here {0.mention} in {1.name} as long as you dont kill anyone**!'
	await bot.send_message(bot.get_channel("428279776181092356"), fmt.format(member, server))

@bot.event
async def on_ready():
	await bot.change_presence(game=discord.Game(type=0, name=';help'))


bot.run("NDMzMzczNjQyMzUzNjcyMTky.Da66OQ.TMe9vn3DMraKmWsXGOeqlEiYbnU")
