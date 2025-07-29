import pytest
import json
from typing import List, Optional

from src.gemini_live_demo.utils import get_weather, filter_events, filter_messages  # type: ignore
from llama_index.core.llms import ChatMessage, AudioBlock, TextBlock
from llama_index.core.voice_agents import BaseVoiceAgentEvent


@pytest.fixture()
def messages() -> List[ChatMessage]:
    return [
        ChatMessage(role="user", blocks=[AudioBlock(audio=b"Hello")]),
        ChatMessage(
            role="assistant",
            blocks=[
                AudioBlock(audio=b"Hello back"),
                TextBlock(text="hello back"),
            ],
        ),
        ChatMessage(role="user", content="now what?"),
    ]


class Audio(BaseVoiceAgentEvent):
    pass


class Text(BaseVoiceAgentEvent):
    pass


@pytest.fixture()
def events() -> List[BaseVoiceAgentEvent]:
    return [
        Audio(type_t="audio"),
        Text(type_t="text"),
        Text(type_t="text"),
    ]


def is_serializable(s: str) -> tuple[bool, Optional[dict]]:
    try:
        d = json.loads(s)
        return True, d
    except json.JSONDecodeError:
        return False, None


def test_weather_tool() -> None:
    a = get_weather("San Francisco")
    assert isinstance(a, str)
    serializable, serialized = is_serializable(a)
    assert serializable
    assert serialized is not None
    assert serialized["location"] == "San Francisco"


def test_filter_messages(messages: List[ChatMessage]):
    filtered = filter_messages(messages)
    assert isinstance(filtered, list)
    assert isinstance(filtered[0], ChatMessage)
    assert len(filtered) == 2
    assert filtered[1].content == "now what?"


def test_filter_events(events: List[BaseVoiceAgentEvent]):
    filtered = filter_events(events)
    assert isinstance(filtered, list)
    assert isinstance(filtered[0], BaseVoiceAgentEvent)
    assert len(filtered) == 2
    assert all(ev.type_t == "text" for ev in filtered)
