# Kimo: An interactive osu! discord bot

## Description

Kimo is a discord bot that fetches information from the osu!API and displays various information depending on which command you type in.
This Discord bot is designed to interact with users and provide specific osu! stats. It currently supports two main commands: `/hi` and `/stats`.

## Commands

### `/hi`
- **Description**: Responds to the user with a greeting and mentions them.
- **Parameters**: None.
- **Usage**: Fun.

### `/poke`
- **Description**: Pokes a server member specified in the `user` parameter.
- **Parameters**:
    - `user`: Any user in the current server.
- **Usage**: Fun.
- **Example**: `/poke @Kimo` ==> `@Einja poked @Kimo!`

### `/stats`
- **Description**: Fetches and displays the current global rank for a specified player in a gamemode. More to come.
- **Parameters**:
    - `username`: The name of the player for whom stats are being retrieved.
    - `gamemode` (optional): The game mode for which stats are requested. Can be one of `std` (standard), `mania`, `taiko`, or `ctb`. Defaults to `std` if left blank or can't match parameter.
- **Usage**: Check a certain osu! player's ranking.
- **Example**: `/stats Einja std` ==> `Name: Einja. Current rank in standard: #3023`

## Installation and Setup
If you would like to simulate this on your own discord bot, follow the instructions listed (You MUST have your own discord bot, discord server, and OAuth Application to use this).
1) Download this source code.
2) Open your terminal, go to config.json and replace the filler values with actual tokens.
3) Run `pip install -r requirements.txt`
4) Execute main.py
5) To shutdown, press Ctrl+C while in the terminal.