# Python Voice Assistant

This Python project is a voice assistant capable of performing various tasks such as searching Wikipedia, fetching jokes, quotes, and random facts, taking screenshots, playing music, checking the time, and even opening popular websites like YouTube, Google, and Spotify.

## Features

- **Wikipedia Search**: Get a quick summary from Wikipedia.
- **Voice-Controlled Browsing**: Open YouTube, Google, Spotify, GitHub, and more.
- **Get Jokes**: Hear a random joke with `pyjokes`.
- **Check the Time**: Get the current time.
- **Random Facts**: Fetch a random fun fact from an API.
- **Quotes**: Fetch an inspirational quote.
- **Take a Screenshot**: Automatically take and save a screenshot.
- **Weather**: Quickly search for weather information.

## Installation

### Requirements

You need to have Python installed on your system. Then install the required libraries:

```bash
pip install pyttsx3 SpeechRecognition wikipedia pyjokes pyautogui requests
```
# Usage
### Clone this repository:
```bash
git clone https://github.com/yourusername/voice-assistant.git 
```
### Run the Python script:
```bash
python '.\Voice Assistant.py'
```

The assistant will start listening for your commands. Example commands include:

- "Search Wikipedia for Python programming"
- "Open YouTube"
- "Tell me a joke"
- "What's the time?"
- "Give me a fact"
- "Give me a quote"
- "Take a screenshot"

## Available Commands

- **Wikipedia Search**: Say `"Wikipedia [search term]"` to search.
- **Website Opening**: Use `"Open [website]"` like `"Open YouTube"`.
- **Jokes**: Say `"Tell me a joke"` to hear a joke.
- **Current Time**: Ask for the time with `"What's the time?"`.
- **Random Fact**: Ask for a fact with `"Give me a fact"`.
- **Quote**: Ask for a quote with `"Give me a quote"`.
- **Screenshot**: Say `"Take a screenshot"` to save a screenshot.
- **Close the Assistant**: Say `"Sleep"` to close the assistant.

## Libraries Used

- **pyttsx3**: Text-to-speech conversion.
- **SpeechRecognition**: Recognize voice commands using Google’s speech API.
- **Wikipedia**: For Wikipedia search summaries.
- **webbrowser**: For opening websites.
- **os**: To interact with system-level operations.
- **pyjokes**: Generate random jokes.
- **datetime**: Get the current time.
- **pyautogui**: Take screenshots.
- **requests**: Fetch quotes and facts from APIs.

## APIs Used

- **Useless Facts API**: Provides random fun facts.
- **ZenQuotes API**: Fetches random motivational quotes.


