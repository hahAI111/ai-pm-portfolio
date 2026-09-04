import os

import streamlit as st


def _setting(name: str) -> str | None:
    """Read a setting from Streamlit secrets first, then environment variables."""
    try:
        value = st.secrets.get(name)
        if value:
            return str(value)
    except (FileNotFoundError, AttributeError):
        pass
    return os.getenv(name)


def azure_openai_available() -> bool:
    return all(
        _setting(name)
        for name in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_DEPLOYMENT")
    )


def generate_with_azure_openai(system_prompt: str, user_prompt: str) -> str:
    """Generate via the Azure AI Foundry OpenAI-compatible Responses API."""
    from openai import OpenAI

    client = OpenAI(
        base_url=_setting("AZURE_OPENAI_ENDPOINT"),
        api_key=_setting("AZURE_OPENAI_API_KEY"),
    )
    response = client.responses.create(
        model=_setting("AZURE_OPENAI_DEPLOYMENT"),
        instructions=system_prompt,
        input=user_prompt,
    )
    return response.output_text or "No response was returned."
