# Read csv in spark

import twint
from pprint import pprint
from warnings import warn
from os import path


def createCorpusForUser(username, filePath="Resources/tweets", tweetLimit=5000):
    filePath += "/"+username + ".corpus"
    if not path.exists(filePath):
        print("Getting tweet for user:" + username)
        try:
            c = twint.Config()
            # c.Store_csv= True
            c.Username = username
            c.Custom["tweet"] = "<|startoftext|>{tweet}<|endoftext|>"
            c.Limit = str(tweetLimit)
            c.Format = "<|startoftext|>{tweet}<|endoftext|>"
            c.Hide_output = True
            c.Output = filePath
            # c.Store_object  = True
            twint.run.Search(c)
        except ValueError:
            warn(username + " has been deleted ")
    else:
        warn(filePath + " exist already")
