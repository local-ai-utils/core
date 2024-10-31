# Local AI Utils - Core
Local AI Utils is a framework and set of local utilities for interacting with AI on your local computer. Conceptually each piece of local-ai-itls should be single-purpose and modular, such that end users can piece together their own AI-powered tool chains.

![Local AI Utils Demo](/docs/full_assist.gif)

## Quickstart
Currently installation is only supported via the GitHub remote.
```
pip install git+https://github.com/local-ai-utils/core
```

## Configuration
Local AI Utils utilizes a YAML config file, which by default is stored at `~/.config/ai-utils.yml`. If you would like to store configs in a different location, you can set a custom path with the `AI_UTILS_CONFIG_PATH` environment variable.

The config file will need different values based on which AI providers you are using, and which plugins.

`~/.config/ai-utils.yml`
```
plugins:
    listen:
    assist:
        assistant: 'assistant_id'
        thread: 'thread_id'
keys:
    openai: "secret_key"
```

## Plugins
Local AI Utils finds almost all of its power in its plugin ecosystem. Plugins extend LAIU in ways that expand what both the AI can do, as well as what can be done on your local system.

Some plugins we'd recommend:
- [**assist**](https://github.com/local-ai-utils/assist) for prompting an AI assistant
- [**listen**](https://github.com/local-ai-utils/listen) for getting quick text-to-speech from your microphone

## TODO
- [x] Plugin loading  
- [] Push notifications  
- [x] Config  
- [x] Client management  
- [] Logging  