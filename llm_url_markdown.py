import llm
import urllib.parse
import httpx
import os

REQUEST_TIMEOUT = 30
URL_MARKDOWN_USER_AGENT = "llm-url-markdown-plugin/0.1"


@llm.hookimpl
def register_fragment_loaders(register):
    """Register the 'md' fragment loader."""
    register("md", load_url_fragment)


def load_url_fragment(url_string: str) -> llm.Fragment:
    """
    Load a fragment from a URL and convert to Markdown.

    Takes the part after 'md:' as input.
    Example input: 'https://example.com' or 'example.com'
    """
    original_url = url_string

    # If URL doesn't have a protocol, default to https://
    parsed_original = urllib.parse.urlparse(original_url)
    if not parsed_original.scheme:
        url_to_fetch = "https://" + original_url
    else:
        url_to_fetch = original_url  # Use the original if it had a scheme

    try:
        quoted_target_url = urllib.parse.quote(url_to_fetch, safe="")
        jina_url = f"https://r.jina.ai/{quoted_target_url}"
    except Exception as e:
        raise ValueError(f"Error creating URL API: {e}")

    headers = {
        "User-Agent": URL_MARKDOWN_USER_AGENT,
        "Accept": "text/markdown,text/plain,*/*",
    }

    token = os.environ.get("JINA_READER_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        response = httpx.get(
            jina_url,
            timeout=REQUEST_TIMEOUT,
            headers=headers,
            follow_redirects=True,
        )
        response.raise_for_status()
        content = response.text
    except Exception as ex:
        err_msg = f"Could not load content for '{original_url}': {str(ex)}"
        raise ValueError(err_msg)

    return llm.Fragment(content, source=original_url)
