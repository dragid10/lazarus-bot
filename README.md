
# Discord Bot Template (python)

Template for building discord apps  

Oauth2 link: `https://discord.com/api/oauth2/authorize?client_id=<CLIENT_ID>&permissions=<PERMS_INT>&scope=bot%20applications.commands`

## Documentation
- [Discord Scopes Explanation](https://discord.com/developers/docs/topics/oauth2)


## Tech Stack

**Python:** 3.9+

**Dependency Manager**: [Poetry](https://python-poetry.org/)  

**Discord package**: [Py-Cord](https://docs.pycord.dev/en/master/index.html)

## Deployment

To deploy this project:
1. [Template](https://github.com/dragid10/discord-bot-template/generate) this repo
1. Clone and `cd` into the repo
1. Run `make setup` to automatically install `poetry`
1. Run `make update && make install` to update and install dependencies

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`bot_token`: String

