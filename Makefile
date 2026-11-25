.PHONY: check lean papers sources
check:
	python3 verification/run_all.py
	python3 scripts/verify_repository.py
lean:
	python3 scripts/verify_lean.py
papers:
	python3 scripts/build_manuscripts.py
sources:
	python3 scripts/fetch_sources.py
