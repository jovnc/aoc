.PHONY: new test run setup clean
.DEFAULT_GOAL := run

setup:
	@python3 -m venv .venv
	@source .venv/bin/activate
	@pip install -r requirements.txt

clean:
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true

new:
	@chmod +x scripts/new.sh
	@scripts/new.sh 

test:clean
	@chmod +x scripts/run.sh
	@scripts/run.sh
	@make clean

run:clean
	@chmod +x scripts/run.sh
	@scripts/run.sh
