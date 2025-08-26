# Canvas Quizzes with Local AI

## Overview
This project is a web application that allows users to generate Canvas quizzes using local LLMs (via Ollama) through a chatbox interface. Users can select from available local models, interact via chat, and download quizzes in the Canvas quiz template format for easy upload to Canvas LMS.

## Features
- Streamlit-based chat UI
- Ollama LLM integration with selectable models
- Canvas quiz template generation
- Downloadable quiz file
- Instructions for uploading to Canvas

## Setup
1. Install [Ollama](https://ollama.com/) and ensure at least one LLM is available locally.
2. Clone this repository.
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the app:
   ```bash
   streamlit run app.py
   ```

## Usage
- Select the desired LLM from the menu.
- Use the chatbox to instruct the LLM to generate a quiz (e.g., "Create a 5-question multiple choice quiz on photosynthesis").
- Download the generated quiz file and upload it to Canvas LMS.

## Project Structure
- `app.py` - Main Streamlit app
- `ollama_utils.py` - Functions for interacting with Ollama
- `canvas_template.py` - Canvas quiz template generation
- `requirements.txt` - Python dependencies
- `README.md`, `PLAN.md`, `ROADMAP.md`, `CONTRIBUTING.md` - Documentation

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md)

## License
MIT License
