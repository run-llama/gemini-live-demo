from llama_index.core.voice_agents import BaseVoiceAgentEvent
from llama_index.core.llms import ChatMessage, TextBlock
from typing import List
import random
import json


# use filter functions to export messages and events without your terminal being swamped by base64-encoded audio bytes :)
def filter_events(
    events: List[BaseVoiceAgentEvent],
) -> List[BaseVoiceAgentEvent]:
    """Filter events to exclude audio-based ones."""
    evs = []
    for event in events:
        if "audio" not in event.type_t:
            evs.append(event)
    return evs


def filter_messages(messages: List[ChatMessage]) -> List[ChatMessage]:
    """Filter messages to exclude audio-based ones."""
    msgs = []
    for message in messages:
        msg = ChatMessage(role=message.role, blocks=[])
        for b in message.blocks:
            if isinstance(b, TextBlock):
                msg.blocks.append(b)
        if len(msg.blocks) > 0:
            msgs.append(msg)
    return msgs


def get_weather(location: str) -> str:
    """Fetch weather data for a given location."""
    return json.dumps(
        {
            "location": location,
            "temperature_c": round(random.uniform(15, 30), 1),
            "humidity_percent": random.randint(40, 90),
            "wind_speed_kmh": round(random.uniform(5, 25), 1),
            "precipitation_probability_percent": random.randint(0, 100),
        },
        indent=4,
    )
