# JokeBot README

## Introduction
**JokeBot** is a Discord bot powered by OpenAI's GPT-4, designed to generate humorous one-liner jokes and compliments about "Steve Pruitt." The bot provides two main commands: `/stevejoke` for funny jokes and `/stevecompliment` for exaggerated, over-the-top compliments. These commands create an interactive and entertaining experience for Discord users.

---

## Features
- **AI-Generated Jokes**: The `/stevejoke` command delivers one-liner jokes about Steve Pruitt, parodying the style of Chuck Norris jokes by highlighting Steve's "bad luck" and "lack of skills."
- **AI-Generated Compliments**: The `/stevecompliment` command flips the script, providing overly dramatic compliments about Steve Pruitt, styled as heroic and absurd feats.

---

## Prerequisites
1. **Python 3.8 or later**: Ensure Python is installed on your machine.
2. **Discord Bot Token**: Obtain a bot token from the [Discord Developer Portal](https://discord.com/developers/applications).
3. **OpenAI API Key**: Sign up for OpenAI and get an API key from [OpenAI's platform](https://platform.openai.com/signup/).
4. **Dependencies**: Install the required libraries via `pip`.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   ```bash
   pip install discord.py openai
   ```

3. **Set Environment Variables**:
   Create a `.env` file or set the environment variables directly:
   ```
   DISCORD_TOKEN=<your_discord_bot_token>
   OPENAI_API_KEY=<your_openai_api_key>
   ```

---

## Usage

1. **Run the Bot**:
   ```bash
   python <script_name>.py
   ```
   Replace `<script_name>` with the name of the Python file containing the bot code.

2. **Invite the Bot to a Discord Server**:
   - Go to the [Discord Developer Portal](https://discord.com/developers/applications).
   - Select your bot application.
   - Navigate to the OAuth2 tab and generate an invite URL with the `bot` and `applications.commands` scopes.
   - Use the generated URL to invite the bot to your server.

3. **Commands**:
   - `/stevejoke`: Generates a humorous one-liner joke about Steve Pruitt.
   - `/stevecompliment`: Generates an exaggerated, funny compliment about Steve Pruitt.

---

## Example Interaction
### Joke:
- **User**: `/stevejoke`
- **Bot**: "Steve Pruitt tried to save the day once, but the day filed a restraining order."

### Compliment:
- **User**: `/stevecompliment`
- **Bot**: "When Steve Pruitt walks into a room, Wi-Fi signals increase to 10 bars just to impress him."

---

## Customization
To modify the humor or tone:
1. Update the system prompts in the `/stevejoke` and `/stevecompliment` commands.
2. Adjust the `max_tokens` and `temperature` parameters in the OpenAI API calls for different response lengths or creativity.

---

## Troubleshooting
- **OpenAI Errors**: Ensure the OpenAI API key is valid and active.
- **Discord Bot Not Responding**: Verify the bot token and permissions in the Discord Developer Portal.
- **Environment Variables Missing**: Confirm that the `DISCORD_TOKEN` and `OPENAI_API_KEY` variables are set correctly.

---

## Contributing
Feel free to fork this repository and submit pull requests for improvements or additional features!

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.