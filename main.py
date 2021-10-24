import wikipedia
import discord
import os
from discord.utils import get
import requests
import random
import pickle  #https://wiki.python.org/moin/UsingPickle
client = discord.Client()

global uvotes
global dvotes
global keywords
global keyword2
global bot
global channels
global author


uvotes = 0
dvotes = 0
keywords = {
    "talk_#1": 540606138190921747,
    "talk_#2": 812772146615025674,
    "talk_#3": 788526723905486884,
    "talk_#4": 788526749931667508,
    "kerker": 540606273901690900,
    "talk_#5": 540606199066787873,
    "talk_#6": 540606231061069824,
    "cooler-talk": 820039528978841631,
    "geringverdiener": 826791511361716265,
    "großgeldverdiener": 824679002866188328
  }
bot = ["Move Bot#3376"]
channels = [
    "text", 
    "the-cooler-text", 
    "bot-commands", 
    "rankings", 
    "lord-chat", 
    "admin"
  ]
opfer = [
  
  ]
cancer_emote = ["Der Diamantkönig#4154"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    wikipedia.set_lang("de")


@client.event
async def on_message(message):
    global keywords
    global keyword2
    global bot
    global channels
    global author
    global response
    global category
    global joke
    global healthvalue
    global standard_value

    if str(message.channel) in channels:
        if message.content.startswith('?hello'):
            await message.channel.send('Hello!')
            return
        elif message.content.startswith("?MC_Menü"):
            await message.channel.send("https://www.mcdonalds.com/de/de-de/produkte/alle-produkte.html")
            return
        elif message.content.startswith("?stats"):
            await message.channel.send("https://statbot.net/dashboard/539102925402931230")
            return        
        elif message.content.startswith("?wiki"):
            subkey = message.content.split(".",1)
            keyword = subkey[1].split(" ")
            if keyword[0] == "rand":
              page = wikipedia.random(pages=1)
              embedVar = discord.Embed(title="Random Wiki Article", description="", color=0x00ff00, url="https://de.wikipedia.org/wiki/" + str(page).title().replace(" ", "_"))
              embedVar.add_field(name=page, value=wikipedia.summary(title=page, chars=240, auto_suggest=True, redirect=True))
              await message.channel.send(embed=embedVar)
              return

            elif keyword[0] == "search":           
              page = wikipedia.search(keyword[1], results=1, suggestion=True)
              embedVar = discord.Embed(title="Wiki Artikel", description="", color=0x00ff00, url="https://de.wikipedia.org/wiki/" + str(page[1]).title().replace(" ", "_"))
              embedVar.add_field(name=page[1].title(), value=wikipedia.summary(title=page[0], chars=240, auto_suggest=True, redirect=True))
              await message.channel.send(embed=embedVar)
              await message.channel.send(page[1].title())
              await message.channel.send(str(page[1]))
              return
            return

        #if str(message.author) in cancer_emote:
         # await message.add_reaction('<:Krebs:899299521966784595>')     
        if message.content.startswith("?health_status"):
          healthvalue = random.random()
          standard_value = 0.8
          print(healthvalue)
          if healthvalue >= standard_value:
            await message.channel.send('<:Krebs:899299521966784595>') 
          else:
            await message.channel.send('<:Gesund:899299804281188415>')
          return
          

    
        if not message.content.startswith("?"):
            if str(message.author) in opfer:
                await message.channel.purge(limit=1)
                await message.channel.send(
                    f"""{message.author.name} shut the fck up!""")
                return
            else:
                return
        if message.content.startswith("?joke"):
          category = message.content.split(".")[1]
          if category == "dark":
            response = requests.get("https://v2.jokeapi.dev/joke/Dark")
          if category == "programming":
            response = requests.get("https://v2.jokeapi.dev/joke/Programming")
          if category == "pun":
            response = requests.get("https://v2.jokeapi.dev/joke/Pun")
          if category == "spooky":
            response = requests.get("https://v2.jokeapi.dev/joke/Spooky")  
          else:
            response = requests.get("https://v2.jokeapi.dev/joke/Any")
          joke = response.json()
          if joke["type"] == "single" :
            await message.channel.send(joke["joke"])
          else:  
            await message.channel.send(joke["setup"])
            await message.channel.send(joke["delivery"])
            return
        
        if message.content == "?help":
          embedVar = discord.Embed(title="Hilfe", description="", color=0x00ff00)
          embedVar.add_field(name="Mögliche Befehle:", value="?hello = Bot sagt Hallo\n?moven (Channel) = Moveanfrage für Channel (Channel muss angegeben werden)\n?MC_Menü = Anzeige des Aktuellen MCDonald Menüs\n?joke.'category' = Bot gibt Witz aus bestimmter Kategorie aus\n  Mögliche Kategorien: any, dark, spooky, pun, programming\n  ?wiki.rand =Random Wikipedia Artikel\n  ?wiki.search 'seach' = sucht passenden Wikipedia Artikel\n?health_status = Find out if you have cancer")
          await message.channel.send(embed=embedVar)
          return

        if message.content.startswith('?move'):
            keyword = message.content.split(" ")[1]
            print(keyword)
            keyword2 = keyword.lower()
            print(keyword2)

            if str(keyword2) in keywords:

                print('Keyword found')
                channel = client.get_channel(830881516825083955)  #anfragen channel id
                message_id = message.id
                print(message_id)
                await message.channel.purge(limit=1)
                print("Nachricht gelöscht")
                await channel.send("* " + (message.author.name) + " möchte gemoved werden in " + (keyword))
                print(keywords[keyword2])
                author = message.author
            else:
              await message.channel.send('Zielangabe fehlt')

    if str(message.author) in bot:
        if message.content.startswith("*"):
            await message.add_reaction('👎')
            await message.add_reaction('👍')

    print('\n')

    if message.content.startswith('?thumb'):
        await message.channel.send('Send me that 👍 reaction, mate')
        await message.add_reaction('👍')

        def check(reaction, user):
            return user == message.author and str(reaction.emoji) == '👍'

@client.event
async def on_raw_reaction_add(payload):
    global uvotes
    global dvotes

    #voice_channel = client.get_channel(829047891850821693)  #allgemein talk

    if payload.channel_id == 830881516825083955:  #emote im kanal move-anfragen
        #usercount = voice_channel.voice_states.keys()
        #length = len(usercount)  #anzahl leute im talk

        channel = client.get_channel(830881516825083955)
        message = await channel.fetch_message(payload.message_id)
        reaction = get(message.reactions, emoji=payload.emoji.name)

        if payload.emoji.name == "👍":
            uvotes = reaction.count
            print('uvote')

        elif payload.emoji.name == "👎":
            dvotes = reaction.count
            print('dvote')
        else:
            print('wrong emoji')
    else:
        print('wrong channel id')

    print("up/down:" + str(uvotes - dvotes))

    #hallo machts spaß?
    
    if uvotes - dvotes >= 1:
      global keyword2
      global author
      print('move to channel new')
      channel_id = keywords[keyword2]
      print("ChannelId:" + str(channel_id))
      move_channel = client.get_channel(channel_id)
      print(move_channel)
      print('move to channel')
      print("author: " + str(message.author))
      await author.move_to(move_channel)
      print('\n')
      return
    else:
        print('no movement')
        print("\n")


@client.event
async def on_raw_reaction_remove(payload):
  global uvotes
  global dvotes

  if payload.channel_id == (829419366763331615):  
    channel = client.get_channel(830881516825083955)
    message = await channel.fetch_message(payload.message_id)
    reaction = get(message.reactions, emoji=payload.emoji.name)

    if payload.emoji.name == "👍":
      uvotes = reaction.count
      print('uvote removed')

    elif payload.emoji.name == "👎":
      dvotes = reaction.count
      print('dvote removed')
    else:
      print('wrong emoji removed')  
  else:
    print('wrong channel id removed')

  print("up/down:" + str(uvotes - dvotes))
  print("\n")

  if uvotes - dvotes >= 1:
    global keyword2
    global author
    print('move to channel new')
    channel_id = keywords[keyword2]
    print("ChannelId:" + str(channel_id))
    move_channel = client.get_channel(channel_id)
    print(move_channel)
    print('move to channel')
    print("author: " + str(message.author))
    await author.move_to(move_channel)
    print('\n')
  else:
    print('no movement')
    print("\n")
client.run(os.getenv('TOKEN'))

#test2: https://replit.com/join/ezhjyupe-thrillerninja

#https://www.mediawiki.org/wiki/API:Main_page
#https://wikipedia.readthedocs.io/en/latest/code.html

