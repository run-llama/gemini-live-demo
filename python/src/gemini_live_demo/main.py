from llama_index.voice_agents.gemini_live import GeminiLiveVoiceAgent  # type: ignore
from llama_index.core.tools import FunctionTool
from utils import get_weather, filter_events, filter_messages  # type: ignore
from dotenv import load_dotenv

load_dotenv()

weather_tool = FunctionTool.from_defaults(
    fn=get_weather,
    name="get_weather",
    description="Get the weather at a given location",
)


async def main():
    conversation = GeminiLiveVoiceAgent(tools=[weather_tool])

    await conversation.start()

    if conversation._quitflag:
        print("Events")
        print(conversation.export_events(filter=filter_events))
        print()
        print("Messages")
        print(conversation.export_messages(filter=filter_messages))


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
