"""
module		: watcher.py
description	: Script to automatically watch a directory (via watchdog) for tests and run them via py.test
"""
import sys
import os.path
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class SpecificationsEventHandler(FileSystemEventHandler):
	"""Runs the tests inside the specifications class when any specification file is modified
	"""
	
	def __init__(self): 
		self.paused = False


	# on_moved event not needed for watching files...
	#def on_moved(self, event):
	#	super(FireSpecificationsEventHandler, self).on_moved(event)
   
    # on_created event not needed for watching files...
	#def on_created(self, event):
	#	super(SpecificationsEventHandler, self).on_created(event)
	#	what = 'directory' if event.is_directory else 'file'
	#	print("Created %s: %s", what, event.src_path)

	#def on_deleted(self, event):
	#	super(FireSpecificationsEventHandler, self).on_deleted(event)
        
	def on_modified(self, event):
		super(SpecificationsEventHandler, self).on_modified(event)
		
		# file modified triggers directory modified as well...		
		if event.is_directory:
			return

		if self.paused: 
			return

		if event.src_path.endswith("_specs.py") and not self.paused:
			self.paused = True
			filename = os.path.basename(event.src_path)
			print("testing specifications found in file: {0}".format(filename))
			subprocess.call(['py.test', '-v', filename], shell=True)	
			self.paused = False
			return


if __name__ == "__main__":
    path = sys.argv[1]
    event_handler = SpecificationsEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join() 