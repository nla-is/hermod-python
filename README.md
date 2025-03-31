# Hermod SDK for Python

## Install
Install the SDK using `pip` from `git`:

```shell
pip install git+https://github.com/nla-is/hermod-python.git
```

## Usage
```python
import hermod

def handler() -> str:
    return hermod.invoke_sync("generate-random-sentence")

```
