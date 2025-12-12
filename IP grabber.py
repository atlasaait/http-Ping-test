import sys
import socket
import urllib
import os
import gzip

try:
    import pygeoip
except ImportError:
    print("Failed to import pygeoip")
    try:
            choice = raw_input("Attempt to Auto-install pygeoip [y/N ]")
    except KeyboardInterrupt:
         print("L'utilisateur a interrompu l'attente")
         sys.exit(1)
        
    if choice.strip()lower.()[0] == 'y':
            print('Attempting to install pygeoip'),
            sys.stdout.flush()
            try:
                    import pip
                    pip.main(['install', '-q', 'pygeoip'])
                    import pygeoip
                    print('DONE')
            except Exception:
                  print('FAIL')
                  sys.exit(1)
    elif choice.strip().lower()[0] = 'n':
              print('User denied to install')
              sys.exit(1)
    else:
              print('Invalid decision')
              sys.exit(1)

