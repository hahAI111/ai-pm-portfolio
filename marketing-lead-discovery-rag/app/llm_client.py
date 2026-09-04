import os

import streamlit as st


def setting(name: str) -> str | None:
    try:
        value = st.secrets.get(name)
        if value:
            return str(value)
    except (FileNotFoundError, AttributeError):
        pass
    return os.getenv(name)


def azure_openai_available() -> bool:
    return all(setting(name) for name in ("AZURE_OPENAI_ENDPOINT", "AZURE_OPENAI_API_KEY", "AZURE_OPENAI_DEPLOYMENT"))


def generate_grounded_profile(profile: dict) -> str:
    from openai import OpenAI

    evidence = "\n".join(
        "[{}] {} ({}): {}".format(source["source_id"], source["source_title"], source["source_date"], source["content"])
        for source in profile["citations"]
    )
    client = OpenAI(base_url=setting("AZURE_OPENAI_ENDPOINT"), api_key=setting("AZURE_OPENAI_API_KEY"))
    response = client.responses.create(
        model=setting("AZURE_OPENAI_DEPLOYMENT"),
        instructions="You draft source-grounded B2B lead research profiles. Use only supplied evidence. Do not infer facts, promise outcomes, or recommend contacting a company. Write two concise sentences. Cite every material claim using exact source IDs in square brackets. State an evidence gap when needed.",
        input="Company: {}\nRegion: {}\nDeterministic ICP score: {}\nEvidence:\n{}".format(profile["company_name"], profile["region"], profile["icp_score"], evidence),
    )
    return response.output_text or "No response was returned."
