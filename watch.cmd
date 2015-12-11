:: batch script to watch directory for specification changes and automatically run the tests
cls
echo Python test specification watcher is watching changes for *_specs.py files in directory "%CD%" ...
python watcher.py .