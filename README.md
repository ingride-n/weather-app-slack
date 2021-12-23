# weather-app-slack
Weather bot on Slack

Delivers afternoon and/or nextday forecast for College Park, MD from weather.gov

## Get Started

1. First you'll need to create a free Slack workspace at https://slack.com. If you have your own, that's great! Then create a channel, for example #local-weather-updates and leave it public.
2. Read this article: https://api.slack.com/messaging/webhooks to learn how to create a webhook to use in that workspace. 
3. Create a Slack app by going here: https://api.slack.com/apps. Choose "from Scratch", give it a name, and choose your own workspace.
4. You should be in the configurations for this app. In the features in the left-side panel, go to Incoming Webhooks and activate this. 
5. Scroll down and add a new webhook url. Choose the channel that you created (#local-weather-updates).


## Create Your Own Project
1. In order to use the webhook, you will need to create a `.env` file in the root of your project directory and add your webhook as an environment variable. Then add the following line without spaces:

`SLACK_WEB_HOOK_URL=[enter-webhook-url]`

2. Next, create a python script and write the code to get weather data. To use the webhook, type `process.env.SLACK_WEB_HOOK_URL` in place of the webhook url. This will use the environment variable. 

3. Run the script from a terminal: `python3 [name_of_script].py` Yay!
