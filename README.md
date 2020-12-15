# What is this? 
    You can get a pretty good idea about what people are interested in based on the information they post on social media. This program is supposed to supposed to be part of a bot that can crawl around the internet find users interested in a product and then tweet something related to their interest that will entice them to click on the link. The function of the program is download info about a tweet then create tweets that they might click on 

##How to start
- Clone file install library in requirement.txt - using pip3
- run using Python 3 (Tested in Python 3.8.6)
- Run the main program and you should a bunch of .tweets file in the Output/tweets directory
- If you want to run the full program you have to download the two dataset and move in the resource folder

##Results
For example if we want to run our program on @elonmusk(Elon Musk)
We could uncomment the comment code in main.py and input name=elonmusk

Here are some of the better tweets I got back from the bot
- @elonmusk Short vid of 1st Dragon flight was a sponge. Simpler times they were. https://t.co/bqa5pIAOnk
- @elonmusk Loading the Mars fleet into Earth tones & convolutions https://t.co/bqa5pIAOnk
- @elonmusk It is all about journey 🤔 https://t.co/bqa5pIAOnk
- @elonmusk Falcon on LZ-1 at Cape Canaveral to California... https://t.co/bqa5pIAOnk
- @elonmusk games coming in v hot & fast, so not surprising. https://t.co/bqa5pIAOnk
- @elonmusk why did you manage to get rid of the two Starship build site today https://t.co/bqa5pIAOnk

The URL is supposed to represent a malicious link - However, this is just a link to random article I found on Elon's timeline 


##Importance
Phishing attacks accounted for 80% of security incidents. And the pandemic has increased the number of cyber attacks. So, it is imperative that we study different social attacks. There is a more potent type of phishing called “spear-phishing”, where an attacker gathers information about a user and uses that to craft a more persuasive message. This technique has a much higher click through rate than average phishing attacks. Fortunately, this method is time-consuming and so the attacker cannot target as many people. However, we believe that you can use machine learning to automate this process. If this process becomes widespread, it would have disastrous consequences.

Our project will be to create this automated spear-phishing tool. We will then use our tool to analyze them to determine the effectiveness of various algorithms and the vulnerability on different platforms. We also hope to show the potency of this attack. So, we will compare it to normal phishing attacks and compare the results. We hope the results from our study will help future developers and cybersecurity researchers to create more effective safeguards against social attacks.

Most malware comes from email. However, there is a rising trend for phishing attacks conducted on social media. This is because social media contains a plethora of personal information which makes it possible to launch this type of automated spear-phishing attack.

Rather than creating a defensive tool like a phishing detector using machine learning, we have created an offensive tool. This is because when people are trying to break things, they look for the easiest ways to get the job done. The principle of easiest penetration states that a security system is as strong as its weakest link. So by thinking like an attacker, we can become better defenders.

Furthermore, we wanted to show how easy it is to scale our attack by using libraries like PySpark. This because for each user we only need a limited amount of tweets to generate believable tweets. However the challenge comes from having to deal with millions of users, since most users won't fall for the phishing attack. However, we can easily parallelize the training of our model by creating one worker per user. 

##Improvements
 - use Text-blob to spell correct
 - strip out hash-tags
 - don't take replies when training model
 - use hugging face and implement GPT-2 and potentially GPT-3 on release  and fine tune
 - create model in all tweet about presidential election 