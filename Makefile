build:
	pelican src -s pelican.conf.py -t plagiarism/
clean:
	rm -rf output
