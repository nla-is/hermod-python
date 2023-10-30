# DataX SDK for Python

## Install
Install the SDK using `pip` from `git`:

```shell
pip install git+https://github.com/nla-is/datax-python.git@v2.0.0-alpha.12
```

## Usage
```python
import datax

# initialize
dx = datax.DataX()

while True:
    # receive message
    stream, reference, message = dx.next()
    
    output = process(message)

    # publish message
    dx.emit(output, reference)
```
