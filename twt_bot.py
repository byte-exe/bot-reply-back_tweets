import tweepy
import time

print('Starting bot....')
CONSUMER_KEY = "Cqw4pXPk4lz2EEUieSDKjKuQT"
CONSUMER_SECRET = "AhQZvxkBNS2bmXdUOX8tu5SoZi9vYdNimwmTuzkE9ZJJuzTEk5"
ACCES_KEY = "1323551878483865600-LVgJ1466OXyOnZqKNt4H3k0hBBQlmO"
ACCES_SECRET = "yWdPUmakm5Cn4eMURajaZkNkbeaXgLhzvD7msCsB5Ipxw"

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCES_KEY, ACCES_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen.txt'

def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen = int(f_read.read().strip())
    f_read.close()
    return last_seen

def store_last_seen_id(last_seen, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen))
    f_write.close()
    return

def reply_back():
    print('retrieving and reply to tweets....')

last_seen = retrieve_last_seen_id(FILE_NAME)
mentions = api.mentions_timeline(last_seen, tweet_mode = 'extended')

for mention in reversed(mentions):
    print(str(mention.id) + '--' + mention.full_text)
    last_seen = mention.id
    store_last_seen_id(last_seen, FILE_NAME)
    if '#hello' in mention.full_text.lower():
        print('found #hello!')
        print('Responding back...')
        api.update_status('@' + mention.user.screen_name + '#hello back to you!', mention.id)

while True:
    reply_back()
    time.sleep(15)