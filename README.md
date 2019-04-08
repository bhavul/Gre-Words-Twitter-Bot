# Gre-Words-Twitter-Bot
This is a simple twitter bot which tweets GRE words. If you're one of the people who are studying for GRE, you could subscribe to the twitter bot I've made [@LogophileInsaan](https://twitter.com/logophileinsaan), or create a bot of your own. 

This would send out a new tweet with a random word from the words.txt or princeton words list. You could have your own word list as well.

## How to run the bot?

**This is a Heroku-Deployable branch,** meaning you will able to link a clone of this repofor your use-case and heroku will understand how it has to deploy it. Some files have been added just for this purpose, so heroku knows how to deploy this app, i.e., namely the `Procfile`, `clock.py`, `requirements.txt` and `runtime.txt`.   

But before you deploy, you'll need to create a twitter account for your bot and create an application to use that twitter account. You can look up [this link](http://www.instructables.com/id/Raspberry-Pi-Twitterbot/) which will give you a good idea of what I'm talking about.  
Once you're done setting up your twitter account, you'll need 4 credentials : 
1. API Key
2. Api Secret
3. Access Token
4. Access Token Secret

Just how you need to obtain Twitter API credentials, you need to obtain Wordnik API credentials as well, and put them as well in Config Vars of Heroku. 


Once you have these, you need to know that these have to be given as following environment variables of [Config Vars](https://devcenter.heroku.com/articles/config-vars) to Heroku :  
1. `TWITTER_APIKEY`  
2. `TWITTER_APISECRET`  
3. `TWITTER_ACCESSTOKEN`  
4. `TWITTER_ACCESSTOKENSECRET`  
5. `WORDNIK_APIKEY`


### Helpful Heroku Reference URLs

- https://github.com/heroku/heroku-buildpack-python
- https://devcenter.heroku.com/articles/config-vars
- https://devcenter.heroku.com/articles/clock-processes-python
- https://apscheduler.readthedocs.io/en/v3.6.0/modules/triggers/cron.html#module-apscheduler.triggers.cron

## Requirements
- Python v2.7  (Why? Because this is actually an old project that I'm just publishing now. Back then I was on Py 2.7, although it can quite easily be ported to v3. **Pull Requests, Anyone?**)


- configparser (`pip install configparser`)
- twython (`pip install twython`)
- wordnik (`pip install wordnik`)
- apscheduler (`pip install apscheduler`)

Or, you could just run one command to do them all : 

`pip install -r requirements.txt`

Know that Heroku automatically knows to run this command when we've put a `requirements.txt` file in our repo.

## How to run?

**On local machine**  

```shell
export TWITTER_APIKEY=EXcYMmDpht0dd910ypKGVLtXV
export TWITTER_APISECRET=keVTvbEDUvDzM4jcFdDTX1QGSNA1E6sthPxANjsusjOi1zhHJk
export TWITTER_ACCESSTOKEN=734117510488854528-qngYxikbUK8s9f72hOjShBc2i873KKI
export TWITTER_ACCESSTOKENSECRET=xabcdefgh18293929c6TZrXy3CmPXxw2Q5qH7RU41uLms
export WORDNIK_APIKEY=dd517d354a95381fd4969056ad70daaa5715d7998e88ee5671

python AwesomeGreBot.py
```

Every time you run above, it will tweet once. To run it as a cron, replace `python AwesomeGreBot.py` with `python clock.py`

**On Heroku**   
Nothing much needs to be done. `Procfile` makes sure to tell Heroku that it has to run `clock.py` which automatically schedules a new tweet every 30 minutes between 1am and 11pm GMT. 

--



