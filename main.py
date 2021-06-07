import os
import discord
import requests
import json

client = discord.Client()
my_secret = os.environ['token']#bot token

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  
  if message.content.startswith('!sexo'):
    quote = get_quote()
    await message.channel.send(quote)

  #return kenzy stikers
  if message.content.startswith('!uligrongos'):
    await message.channel.send('😎🌹')


client.run(my_secret)