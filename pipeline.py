from agents import build_reader_agent, build_search_agent, get_writer_chain, get_critic_chain


def _extract_result_text(result):
    """Robust extractor for different possible result shapes returned by agents/chains."""
    # If result is a dict with messages
    try:
        if isinstance(result, dict):
            if "messages" in result:
                msgs = result.get("messages")
                if isinstance(msgs, (list, tuple)) and msgs:
                    last = msgs[-1]
                    # many frameworks use objects with a .content attribute
                    if hasattr(last, "content"):
                        return last.content
                    return str(last)
            if "output" in result:
                return result.get("output")
        # fallback to string conversion
        return str(result)
    except Exception:
        return str(result)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    # Step - 1: search agent working
    print("\n" + " =" * 50)
    print("step 1 - search agent is working...")
    print("\n" + " =" * 50)

    search_agent = build_search_agent()
    search_result = search_agent.invoke({
        "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
    })
    state["search_results"] = _extract_result_text(search_result)

    print("\n search result", state["search_results"])

    # Step - 2: reader agent 
    print("\n" + " =" * 50)
    print("step 2 - Reader agent is scraping top resources...")
    print("\n" + " =" * 50)

    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages": [(
            "user",
            f"Based on the following search results about '{topic}', "
            f"Pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}"
        )]
    })

    state['scraped_content'] = _extract_result_text(reader_result)

    print("\nScraped content\n", state['scraped_content'])

    # Step - 3: Writer chain
    print("\n" + " =" * 50)
    print("step 3 - Writer is drafting the report...")
    print("\n" + " =" * 50)

    research_combined = (
        f"SEARCH RESULTS: \n {state['search_results']} \n\n"
        f"DETAILED SCRAPED CONTENT: \n {state['scraped_content']}"
    )

    writer_chain = get_writer_chain()
    writer_result = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })

    state["report"] = _extract_result_text(writer_result)

    print("\n Final Report\n", state['report'])

    # Step - 4: critic report
    print("\n" + " =" * 50)
    print("step 4 - Critic is reviewing the report...")
    print("\n" + " =" * 50)

    critic_chain = get_critic_chain()
    critic_result = critic_chain.invoke({
        "report": state['report']
    })

    state["feedback"] = _extract_result_text(critic_result)

    print("\n critic report \n", state['feedback'])

    return state


if __name__ == "__main__":
    topic = input("\n Enter a research topic : ")
    run_research_pipeline(topic)
