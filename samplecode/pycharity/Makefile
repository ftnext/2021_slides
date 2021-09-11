help:
	@echo 'Prerequisite: activate virtual environment.'
	@echo 'Type only `make all`'

all: prepare count

prepare:
	pip install -r requirements.in

pyconjp_staff_events.jsonl:
	python scrape_connpass_event.py https://pyconjp-staff.connpass.com/event/ pyconjp_staff_events.jsonl

count: pyconjp_staff_events.jsonl
	python -i count_events.py pyconjp_staff_events.jsonl
