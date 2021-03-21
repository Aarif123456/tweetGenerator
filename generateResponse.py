# Read in tweet from target user and then generate Text
import os
import markovify
import re
from warnings import warn


class TweetText(markovify.Text):
    def sentence_split(self, text):
        return re.split(
            r"(?:\s*<\|endoftext\|>\s*)|(?:@[^\s]*\s)|(?:\s*<\|startoftext\|>\s*)|(?:http[s]?://[^\s]*\s)|(?:www\.[^\s]*\s)",
            text)


def generateTweet(username: str, url: str, num_tweets=10):
    corpus_file = "Resources/tweets/" + username + ".corpus"
    gen_file = "Output/tweets/" + username + ".tweets"
    reply = "@" + username + " "
    url = " " + url
    if os.path.exists(corpus_file):
        # Get raw text as string.
        with open(corpus_file) as f:
            text = f.read()
        max_tweet_length = max(0, 279 - len(url) - len(reply))
        # Build the model.
        text_model = TweetText(text)
        with open(gen_file, "w") as myfile:
            # Print three randomly-generated sentences of no more than 280 characters
            for i in range(num_tweets):
                gen = text_model.make_short_sentence(max_tweet_length)
                if gen == None:
                    warn("WARNING: unable to create " + str(num_tweets) + "tweets for user " + username)
                    break
                out = reply + gen + url
                print(out)
                myfile.write(out + "\n")
