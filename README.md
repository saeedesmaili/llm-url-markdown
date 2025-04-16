# llm-url-markdown

[![PyPI](https://img.shields.io/pypi/v/llm-url-markdown.svg)](https://pypi.org/project/llm-url-markdown/)
[![Changelog](https://img.shields.io/github/v/release/saeedesmaili/llm-url-markdown?include_prereleases&label=changelog)](https://github.com/saeedesmaili/llm-url-markdown/releases)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/saeedesmaili/llm-url-markdown/blob/main/LICENSE)

LLM plugin for pulling web page content as Markdown.

This plugin fetches the primary content of a URL, formatted as Markdown, and makes it available as an LLM fragment.

For background on LLM fragments:

- [Fragments - LLM Documentation](https://llm.datasette.io/en/stable/fragments.html)

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

```bash
llm install llm-url-markdown
```

## Usage

You can feed the Markdown content of a web page into LLM using the `md:` [fragment](https://llm.datasette.io/en/stable/fragments.html) prefix followed by the URL.

For example:

```bash
# Fetch content from a full URL
llm -f md:https://llm.datasette.io/en/stable/plugins/index.html 'Summarize the types of plugins available'

# Fetch content, defaulting to https://
llm -f md:github.com/simonw/llm 'What is the main goal of this LLM tool?'
```

The plugin prepends `https://` if no protocol (like `http://` or `https://`) is specified in the URL. The fetched content is the Markdown representation of the webpage.

### Jina Reader API Token (Optional)

This plugin uses the Jina Reader API, which allows requests without an API key, although potentially subject to lower rate limits. The plugin functions without an API token, which is often sufficient for typical LLM fragment usage and improves usability.

If you have a Jina Reader API token and want to use it (for higher rate limits), you can set it as an environment variable:

```bash
# Set the token (only needed once per shell session)
export JINA_READER_TOKEN=your_api_token_here

# Then use the plugin as normal
llm -f md:example.com 'Summarize this page'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-url-markdown
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
# Installs llm, httpx, and testing tools like pytest
pip install -e '.[test]'
```

To run the tests:

```bash
python -m pytest
```
