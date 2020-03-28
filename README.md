# Lockdown Kings Cup

A virtual game of kings for virtual parties for the Covid-19 lockdown.

![](https://raw.githubusercontent.com/jakekgrog/lockdown-kings-cup/master/assets/lockdown.PNG)

## How it works

- All players connect to the server. The host goes first. Updates get pushed to all connected players.

- If someone joins late, they get the latest updates.

## How to set up

1. Clone this repo to a server e.g. EC2 instance: `git clone https://github.com/jakekgrog/lockdown-kings-cup`

2. `pip install -r requirements.txt`

3. Edit the host on line 68 of templates/index.html.

4. Add the players to players.txt, one name per line.

5. Update the rules in rules.py to meet your needs.

6. `python server.py`

7. Enjoy!

8. The max connections is set to 15, you can increase this if you want :)


### Updates:

- It's not perfect but it does the job :)
    - I hacked this together pretty quickly
    - Works great for video calling friends
