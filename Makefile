.PHONY: check papers sources
check:
	python3 verification/run_all.py
	python3 scripts/verify_repository.py
papers:
	python3 scripts/build_manuscripts.py
sources:
	python3 scripts/fetch_sources.py
