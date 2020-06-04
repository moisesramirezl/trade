from trade.wsgi import application

   try:
      import googleclouddebugger
      googleclouddebugger.enable()
    except ImportError:
       pass

    import logging
    logging.basicConfig(level=logging.INFO)

app = application
