# Gre-Words-Twitter-Bot
This is a simple twitter bot which tweets GRE words. If you're one of the people who are studying for GRE, you could subscribe to the twitter bot I've made [@LogophileInsaan](https://twitter.com/logophileinsaan), or create a bot of your own. 


## How to run the bot?
First of all, you need to create a twitter account for your bot and create an application to use that twitter account. You can look up [this link](http://www.instructables.com/id/Raspberry-Pi-Twitterbot/) which will give you a good idea of what I'm talking about.
Once you're done setting up your twitter account, you'll need 4 credentials : 
1. API Key
2. Api Secret
3. Access Token
4. Access Token Secret

Once you have these, just create a file named `config_auth.properties` in this directory and put these details there. Use the same format as provided in `config_auth.properties.example`

Just how you need to obtain Twitter API credentials, you need to obtain Wordnik API credentials as well, and put them in the file as well. 

## Requirements
- Python v2.7  (Why? Because this is actually an old project that I'm just publishing now. Back then I was on Py 2.7, although it can quite easily be ported to v3. **Pull Requests, Anyone?**)
- configparser (`pip install configparser`)
- twython (`pip install twython`)
- wordnik (`pip install wordnik`)

## How to run?
It's as simple as it can get.
`python AwesomeGreBot.py`

This would send out a new tweet with a random word from the words.txt or princeton words list. 

**To regularly tweet a new word out, you could add this to cron**
Step 1. Open crontab for editing

`crontab -e`

Step 2. Add an entry for executing this bot. If we had to tweet out a word every 20 minutes (Say, 10th, 30th and 50th minute of every hour from 9am to 10pm) 

`10,30,50 9-22 * * *     /usr/bin/python /home/pi/GRE-BOT-Project/AwesomeGreBot.py`

Of course, don't forget to change the path. :-) 
