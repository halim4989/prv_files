from instabot import Bot
bot = Bot(
    comments_file="../comments.txt",
    comment_delay=15,
    max_comments_per_day=3000
)
bot.login(username="real_girl_live", password="Qwerty@2199@riFJ")

flwing = bot.get_user_following("real_girl_live")
# bot.comment_users(flwing, 2)

print('\n\ntype ', type(flwing),'\nlen ', len(flwing))