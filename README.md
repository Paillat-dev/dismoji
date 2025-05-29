<div align="center">
<h1>dismoji</h1>

<!-- badges -->

![PyPI - Version](https://img.shields.io/pypi/v/dismoji)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/dismoji)
![PyPI - Types](https://img.shields.io/pypi/types/dismoji)
![PyPI - License](https://img.shields.io/pypi/l/dismoji)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Paillat-dev/dismoji/CI.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Paillat-dev/dismoji/main.svg)](https://results.pre-commit.ci/latest/github/Paillat-dev/dismoji/main)

<!-- end badges -->

A Python library for converting Discord emoji names to their Unicode equivalents and
vice versa.

</div>

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Features](#features)
- [Limitations](#limitations)
- [Getting Help](#getting-help)
- [Development](#development)
- [Contributing](#contributing)
- [License](#license)

## Overview

Dismoji is a lightweight Python library that provides a simple way to convert Discord
emoji names to their Unicode equivalents and vice versa. With just two function calls,
you can transform text containing Discord-style emoji codes (like `:smile:`) into text
with actual Unicode emoji characters (like "😄") and back again.

This library uses
[Paillat-dev/discord-emojis](https://github.com/Paillat-dev/discord-emojis) as the
source for Discord emoji names and aliases.

## Installation

```bash
pip install dismoji
```

## Quick Start

<!-- quick-start -->

```python
import dismoji

# Convert Discord emoji names to Unicode emojis
text = "Hello, :wave: I'm excited! :partying_face:"
converted_text = dismoji.emojize(text)
print(converted_text)  # Output: "Hello, 👋 I'm excited! 🥳"

# Convert Unicode emojis back to Discord emoji names
emoji_text = "Hello, 👋 I'm excited! 🥳"
named_text = dismoji.demojize(emoji_text)
print(named_text)  # Output: "Hello, :wave: I'm excited! :partying_face:"
```

## Features

- **Simple API**: Just two functions to remember - `dismoji.emojize()` and
  `dismoji.demojize()`
- **Discord Compatible**: Supports Discord's emoji naming conventions
- **Comprehensive**: Includes all standard emojis available on Discord
- **Type Safe**: Fully type-annotated for better IDE integration
- **Zero Dependencies**: Lightweight with no external dependencies
- **Fast**: Optimized for quick emoji replacement
- **Bidirectional**: Convert between emoji names and characters in both directions

## Getting Help

If you encounter issues or have questions about dismoji:

- **GitHub Issues**:
  [Submit a bug report or feature request](https://github.com/Paillat-dev/dismoji/issues)
- **Discord Support**: Join the [Pycord Official Server](https://discord.gg/pycord) and
  mention `@paillat`

## Development

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linter, formatter and type checker: `ruff check .`, `ruff format .`,
   `basedpyright .`
5. Submit a pull request

**Development Tools**:

- **uv**: For dependency management
- **Ruff**: For linting and formatting
- **HashiCorp Copywrite**: For managing license headers
- **basedpyright**: For type checking

## License

MIT License - Copyright (c) 2025 Paillat-dev

---

Made with ❤ by Paillat-dev
