# clear battle log and logs directory before running tests
rm -f logs/battles/*.csv
python3 -m unittest discover engine.test
