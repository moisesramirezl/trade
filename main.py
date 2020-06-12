import logging
from trade.wsgi import application

app = application

try:
    import googleclouddebugger
    googleclouddebugger.enable()
except ImportError:
    pass

logging.basicConfig(level=logging.INFO)
