# Gemini-Live Demo

This is a demo repository showcasing Gemini Live x LlamaIndex integration.

## Install and Launch

> [!IMPORTANT]
>
> _This is a [uv](https://docs.astral.sh/uv/) project, so make sure to have uv [installed](https://docs.astral.sh/uv/getting-started/installation/)_

Clone this repository locally:

```bash
git clone https://github.com/run-llama/gemini-live-demo
cd gemini-live-demo
```

And install the needed dependencies:

```bash
uv sync
```

Now create a `.env` file and add your `GOOGLE_API_KEY` there:

```bash
touch .env
echo GOOGLE_API_KEY=*** > .env
```

Launch the application with

```bash
uv run src/gemini_live_demo/main.py
```

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](./LICENSE).
