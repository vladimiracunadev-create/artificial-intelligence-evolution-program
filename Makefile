.PHONY: validate test site desktop zip

validate:
	python scripts/validate_repository.py --strict

test:
	python -m unittest discover -s tests -v

site:
	python -m http.server 8080

desktop:
	python apps/desktop/main.py

zip:
	python scripts/package_release.py
