
# Right Hand Man 

Python based CLI Code Assistant. Hooks into Gemini to handle the 'thinking' that is running under the hood. 

Future Goals / Improvments:
- Hooking into other providers and supporting more models
- Compare and contrast the same problem against different LLM's




## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`GEMINI_API_KEY` 



## Acknowledgements


Teddy bear debugging with Boots

## Usage/Examples

Update **WORKING_DIR** in **config.py** before executing code. It has the abilty to *read and write to files*. 



```python
uv venv
source .venv/bin/activate

uv venv main.py "query" 

# Run verbose for the flags / args
uv venv main.py "query" --verbose
```


