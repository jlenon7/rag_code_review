# RAG Code Review 🤖

> Implementation of RAG techniques to make code reviews in git repositories.

## Tools

The project uses the following tools to work:

- [LangChain](https://python.langchain.com/docs/introduction/)
- [Chroma as Vector DB](https://www.trychroma.com/)
- [GPT 3.5 Turbo as LLM](https://platform.openai.com/docs/models#gpt-3-5-turbo)
- [ADA 002 for Text Embedding](https://platform.openai.com/docs/models#embeddings)

## Running

To run the project first create a new Python environment and activate it. I'm using [Anaconda](https://www.anaconda.com/) for setting the python version that pipenv should use to set up the environment. The command bellow will automatically setup the environment with conda and pipenv:

```shell
make env
```

Now install all the project dependencies:

```shell
make install-all
```

Clone the repositories you want the model to code review:

```shell
make clone
```

You can change the repositories you want to clone inside `bin/clone.py`. Also take a look inside `bin/insert.py`
when calling `load_code_folder_chunks()` function to verify which paths and code languages you want to include in
the VectorDB. You can also define files that you want to exclude.

Insert the file chunks in Chroma database by running:

```shell
make insert
```

Ask something by running the following:

```shell
make ask
```

You can change your question inside `bin/ask.py`.
