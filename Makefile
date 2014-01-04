build:
	pelican src -s pelican.conf.py -t neat/

clean:
	rm -rf output

deploy:
	fab deploy
