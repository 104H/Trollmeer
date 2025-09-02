# Trollmeer

My friend Shamer trolls a lot, but he does it well so I want to build a chatbot which can troll like him.

## Technical Description

This repo comes equipped with a a data prepocessor which takes in a chat exported from whatsapp and pulls out only the messages of one sender.

There is am llm, which is then programmed to replicate the mannerisms in messages.

# How to

- Export a whatsapp chat and place it in a folder. Provide a path to this file and name of your friend in the `config.yml` file.
- Run the preprocessor.
- Clone and install the requirements in a venv. Run `python src/llm/main.py`

## Checklist

[x] Set up precprocessor
[x] Set up basic llm
[x] Provide llm with the ability to search the internet
[x] Give llm memory to maintain conversation
[ ] Use RAG and prompt engineering to make it speak like the corpus
