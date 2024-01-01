# Kimo: An interactive osu! discord bot

## Description

Kimo is a discord bot that fetches information from the osu!API and displays various information depending on which command you type in.
This Discord bot is designed to interact with users and provide specific osu! stats. It currently supports two main commands: `/hi` and `/stats`.

## Commands

### `/hi`
- **Description**: Responds to the user with a greeting and mentions them.
- **Parameters**: None.
- **Usage**: Fun.

### `/stats`
- **Description**: Fetches and displays the current global rank for a specified player in a gamemode. More to come.
- **Parameters**:
- `username`: The name of the player for whom stats are being retrieved.
- `gamemode` (optional): The game mode for which stats are requested. Can be one of `std` (standard), `mania`, `taiko`, or `ctb`. Defaults to `std` if left blank or can't match parameter.
- **Usage**: Check a certain osu! player's ranking.
- **Example**: /stats Einja ==> `Name: Einja. Current rank in standard: #3023`

## Installation and Setup
WIP