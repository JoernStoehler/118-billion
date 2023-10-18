# 117 Billion

This is the source code for [117billion.com](https://117billion.com).

We don't know most of humanity. 

This project aims to give a fake impression of what it would be like to remember.

## Development

### Prerequisites

- An OpenAI API key
- Python 3.8+ & Pip

### Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy and edit `.env.example` to `.env`, or set the environment variable `OPENAI_API_KEY`
4. Start a local http server in the `docs` folder, e.g. `python3 -m http.server -d docs`

Avoid exposing or committing your `.env` file as it contains API keys.  
Avoid exposing or committing the log files in `logs/` as they contain the ids of your openai requests (no idea if that's bad).

### Make A Human

Run `python3 src/main.py --new` to automatically sample another random member of humanity.

This will result in the following files:
- `docs/data/<uuid>.json`: The JSON file containing all data about the human
- `docs/data/<uuid>.html`: The obituary text
- `docs/data/<uuid>.png`: The portrait image
- `logs/<uuid>.log`: The log file containing the full output of the script

You can run `python3 src/costs.py logs/<id>.log` to parse the (estimated) amount of money spent on the human. Usually this is around $0.23.

### Customiziation

Edit `src/main.py:make_human` to change which variables are used to describe the human population, and how they are sampled.

### License

This project is licensed under the [MIT License](LICENSE).