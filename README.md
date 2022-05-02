![Build Status](https://github.com/dragid10/lazarus-bot/actions/workflows/python-tests.yml/badge.svg)
# Lazarus Discord Bot  

A discord bot that automatically unarchives threads as soon as they're archived.

[Install link](https://discord.com/api/oauth2/authorize?client_id=965283118477094992&permissions=543582182592&scope=bot%20applications.commands)

## Documentation

- [Discord Scopes Explanation](https://discord.com/developers/docs/topics/oauth2)

## Tech Stack

**Python:** 3.9+

**Dependency Manager**: [Poetry](https://python-poetry.org/)

**Discord package**: [Py-Cord](https://docs.pycord.dev/en/master/index.html)

**Unit Test Runner**: [Pytest](https://docs.pytest.org/en/stable/)

## Deployment

To deploy this project:

1. [Template](https://github.com/dragid10/discord-bot-template/generate) this repo
1. Clone and `cd` into the repo
1. Run `make setup` to automatically install `poetry`
1. Run `make update && make install` to update and install production dependencies
1. _Alternatively_, you can run `make install-dev` or `make install-test` to install all dev dependencies or test dependencies respectively
## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

- Clone the `.env-sample` [file](https://github.com/dragid10/lazarus-bot/blob/master/.env.sample) and rename it `.env`
- If you're using a `.env` file, then the environment variables will be set automatically(thanks
  to [dotenv](https://pypi.org/project/python-dotenv/))
    - Otherwise you can export each of the environment variables manually
   ```bash
    export bot_token=<bot_token>
   ```

### [Discord]

`bot_token`: **String**

### [Redis]

`redis_user`: **String**  
`redis_password`: **String**  
`redis_host`: **String**  
`redis_port`: **Int**  