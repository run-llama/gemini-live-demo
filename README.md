# Gemini-Live Demo

This is a demo repository showcasing Gemini Live x LlamaIndex integration.

Watch the [python](https://www.loom.com/share/3f9b5c53d6c84fa89e7498a3ce7f1b99?sid=b87329ec-9278-439c-a626-dd1e13adbc97) and the [typescript](https://www.loom.com/share/97119c8b424e4246af591637d1f1ce3d?sid=5ec40ea7-e7e4-4bfd-a748-4263ed98100b) demo videos for a quick overview!

## Python

### Install and Launch

> [!IMPORTANT]
>
> _This is a [uv](https://docs.astral.sh/uv/) project, so make sure to have uv [installed](https://docs.astral.sh/uv/getting-started/installation/)_

Clone this repository locally:

```bash
git clone https://github.com/run-llama/gemini-live-demo
cd gemini-live-demo/python
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

## TypeScript

### Install and Launch

Make sure to export your `GOOGLE_API_KEY` before running the demo.

```bash
export GOOGLE_API_KEY="my-google-api-key"
```

**User Set-Up**

```bash
npx @cle-does-things/live-chat
```

**Developer Set-Up**

Clone this repository locally:

```bash
git clone https://github.com/run-llama/gemini-live-demo
cd gemini-live-demo/ts
```

And install the needed dependencies:

```bash
npm install
```

Build the package:

```bash
npm run build
```

Run the package:

```bash
npm run start
```

Try running the executable with:

```bash
npx live-chat
```

If you run into problems like `Permission Denied`, make sure you make `live-chat` an executable - for example, on Linux/macOs:

```bash
chmod +x $HOME/.npm/_npx/*/node_modules/.bin/live-chat
```

## Contributing

We welcome contributions! Please read our [Contributing Guide](CONTRIBUTING.md) to get started.

## License

This project is licensed under the [MIT License](./LICENSE).
