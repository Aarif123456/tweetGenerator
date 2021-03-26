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


def generateTweet(username: str, url: str, genFile="Output/tweets",
                    corpusFile="Resources/tweets",numTweets=10):
    corpusFile += "/" + username + ".corpus"
    genFile += "/" + username + ".tweets"
    reply = "@" + username + " "
    url = " " + url
    if os.path.exists(corpusFile):
        # Get raw text as string.
        with open(corpusFile) as f:
            text = f.read()
        maxTweetLength = max(0, 279 - len(url) - len(reply))
        # Build the model.
        text_model = TweetText(text)
        with open(genFile, "w") as myfile:
            # Print three randomly-generated sentences of no more than 280 characters
            for i in range(numTweets):
                gen = text_model.make_short_sentence(maxTweetLength)
                if gen == None:
                    warn("WARNING: unable to create " + str(numTweets) + "tweets for user " + username)
                    break
                out = reply + gen + url
                print(out)
                myfile.write(out + "\n")