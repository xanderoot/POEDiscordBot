import random
import discord

runningOnPi = 1

if runningOnPi == 1:
    x = open("data.env", 'rt')
else:
    x = open("Python/POEDiscordBot/data.env", 'rt')
dotenv = x.readlines(0)
discordToken = dotenv[0]

x.close()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

##################### Declarations

confirmedItems = ['Summon Skeletons']
items = ['Elemental Army','Bone Ring','Calling Wand','+1 Minion Helm','+2 Minion Helm','+3 Minion Helm','Vaal Summon Skeletons','The Dark Mage (Div)','The Brawny Battle Mage (Div)',
        'Necromancer Silks (Normal)','Necromancer Silks (Magic)','Necromancer Silks (Rare)','Feeding Frenzy','Meat Shield','Bone Helmet','Elder Influenced Amulet with +1 Maximum Skeletons.',
        'Added Cold Damage Support','Added Fire Damage Support','Added Lightning Damage Support','Tailoring Orb','Lab Enchanted Minion Helmet Damage 25%','Lab Enchanted Minion Helmet Damage 40%',
        'Faster Casting Support','Spell Echo Support','Cobalt Jewel All Rarities','Chance Orb','Fusing Orb','Ancient Orb','Herald of Ice','Herald of Thunder','Herald of Ash','Minion Resist Flask',
        'Minion Life Flask','Bone Ring with Resists','Queens Decree','Midnight Bargain','Alberons Warpath','Lab Enchanted Minion Helmet Damage 20% Chance to Summon Additional',
        'Lab Enchanted Minion Helmet 40% Chance to Summon Additional','From Dust','To Dust','Earendels Embrace','Femurs of the Saints','The Iron Mass','Trinity Support','Faster Projectiles',
        'Volley Support','Greater Volley Support','Animate Weapon','Animate Guardian']
itemsToOutput = []

##################### Running Code

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$fuckit'):
        itemsToOutput = []
        splitString = message.content.split()
        splitString.append('')
        userChoice = splitString[1].lower()
        if userChoice == '': await message.channel.send('Example: "$fuckit 5" generates 5 items to try.')
        for each in confirmedItems: itemsToOutput.append(each)
        for x in range(int(userChoice)):
            itemsToOutput.append(items[random.randint(0,len(items) - 1)])
        await message.channel.send(itemsToOutput)

#####################

client.run(discordToken)