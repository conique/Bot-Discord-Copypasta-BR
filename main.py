import discord
import random
import praw

TOKEN = 'digite o token aqui'
CLIENT_ID = 'digite seu client id aqui'
CLIENT_SECRET = 'digite seu client secrete aqui'
USER_AGENT = 'none'

intents = discord.Intents.all()

client = discord.Client(intents=intents)

reddit = praw.Reddit(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    user_agent=USER_AGENT
)

@client.event
async def on_ready():
    print('LIGADO')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!cp') or message.content.startswith('!CP') or message.content.startswith('!cP') or message.content.startswith('!Cp'):
      
        subreddit = reddit.subreddit('copypastabr')
        posts = subreddit.hot(limit=50)

        random_post = random.choice([post for post in posts if not post.stickied])
        post_title = random_post.title[:2000]
        post_text = random_post.selftext[:2000 - len(post_title)]

        await message.channel.send(f' {post_title}\n\n{post_text}')

client.run(TOKEN)