import logging
import platform
import setproctitle
import flaskr
import sys
import nw_logging

def main():
    flask_app = flaskr.create_app()
    flask_app.debug = True
    flask_app.run(host="localhost", port="5000")

if __name__ == "__main__":

    if platform.system() == "Linux":
        setproctitle.setproctitle('ninewatt_app')
    
    sys.exit(main())