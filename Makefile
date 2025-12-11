.PHONY: new test run setup clean
.DEFAULT_GOAL := run

setup:
	@python3 -m venv .venv
	@source .venv/bin/activate
	@pip install -r requirements.txt

clean:
	@rm -rf .venv
	@rm -rf __pycache__
	@rm -rf src/*/__pycache__

new:
	@chmod +x scripts/new.sh
	@scripts/new.sh 

test:clean
	@chmod +x scripts/run.sh
	@scripts/run.sh

run:clean
	@chmod +x scripts/run.sh
	@scripts/run.sh
