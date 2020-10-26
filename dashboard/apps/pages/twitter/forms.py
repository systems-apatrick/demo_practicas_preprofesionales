from django import forms
from django.conf import settings
import tweepy

class TwitterForm(forms.Form):

    def __str__(self):
        auth = tweepy.OAuthHandler(settings.TWITTER_CONSUMER_KEY, settings.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(settings.TWITTER_ACCESS_TOKEN, settings.TWITTER_ACCESS_TOKEN_SECRET)
        api  = tweepy.API(auth)
        query = ['textil']

    def search(self):
        # result = {}
        # word = self.cleaned_data['word']
        # endpoint = 'https://od-api.oxforddictionaries.com/api/v1/entries/{source_lang}/{word_id}'
        # url = endpoint.format(source_lang='en', word_id=word)
        # headers = {'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY}
        # response = requests.get(url, headers=headers)
        # if response.status_code == 200:  # SUCCESS
        #     result = response.json()
        #     result['success'] = True
        # else:
        #     result['success'] = False   
        #     if response.status_code == 404:  # NOT FOUND
        #         result['message'] = 'No entry found for "%s"' % word
        #     else:
        #         result['message'] = 'The Oxford API is not available at the moment. Please try again later.'
        # return result