import os

_SLEIPNIR_PATH = os.getenv("HERMOD_SLEIPNIR_PATH", '/__sleipnir__/sleipnir.so')
_SKATTKISTA_URL = os.getenv("HERMOD_SKATTKISTA_URL")

if _SKATTKISTA_URL is None:
    raise Exception("Environment variable HERMOD_SKATTKISTA_URL must be set")

_WORKSPACE = os.getenv("HERMOD_WORKSPACE", os.getenv("HERMOD_NAMESPACE", ""))
if _WORKSPACE == "":
    raise Exception("Environment variable HERMOD_WORKSPACE must be set")

def __initialize():
    import urllib.request
    import tempfile
    import sys
    import importlib

    initialize_url = f"{_SKATTKISTA_URL}/sdk/python/hermod/__init__.py"
    temporary_directory = tempfile.TemporaryDirectory()
    sdk_directory = os.path.join(temporary_directory.name, "hermod")
    os.mkdir(sdk_directory)
    urllib.request.urlretrieve(initialize_url, os.path.join(sdk_directory, "__init__.py"))
    hermod_module = importlib.import_module("hermod")
    current_module_directory = os.path.dirname(os.path.abspath(__file__))
    sys_path = [i for i in sys.path if i != current_module_directory]
    sys.path = [temporary_directory.name] + sys_path
    importlib.reload(hermod_module)
    hermod_module = importlib.import_module("hermod")
    sys.modules["hermod"] = hermod_module
    getattr(hermod_module, "_setup")(temporary_directory)

__initialize()
