import json
import csv
from tapioca_twitter import Twitter

def generator_files():
    with open('secrets.json') as secret_file:
        secret = json.load(secret_file)

    api = Twitter(
        api_key=secret['API_KEY'], 
        api_secret=secret['API_SECRET'], 
        access_token=secret['ACCESS_TOKEN'], 
        access_token_secret=secret['ACCESS_TOKEN_SECRET']
    )

    channels = {
        'fashions': ('theblondesalad', 'aimeesong', 'Kayture', 'GalMeetsGlam', 'wendynguyen'),
        'fitness': ('greatist', 'dailyburn', 'FitBottomedGirl', '@bornfitness', 'TheRock')
    }

    for type_channel, values in channels.items():
        for channel in values:
            tweets = api.search_tweets().get(params={'q': 'from:{channel}', 'count': 20, 'result_type': 'recent'})
            data = tweets().data
            with open("/tmp/files/tweets_{channel}.csv".format(channel=channel), 'w') as csvfile:
                fieldnames = ['id', 'text', 'user_name', 'user_id']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for item in data['statuses']:
                    writer.writerow({'id': item['id'], 'text': item['text'], 'user_name': item['user']['name'], 'user_id': item['user']['id']})