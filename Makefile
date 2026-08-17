.PHONY: validate test site desktop zip papers papers-check pdf pdf-papers all-checks hooks

hooks:
	git config core.hooksPath .githooks
	@echo "hook pre-push activo: corre la tanda de CI antes de cada push"

validate:
	python scripts/validate_repository.py --strict

test:
	python -m unittest discover -s tests -v

papers:
	python scripts/generate_papers.py
	python scripts/link_papers_to_classes.py

papers-check:
	python scripts/generate_papers.py --check
	python scripts/link_papers_to_classes.py --check

pdf:
	python scripts/generate_pdfs.py

pdf-papers:
	python scripts/generate_pdfs.py --papers

site:
	python scripts/generate_site.py
	python -m http.server 8080

desktop:
	python apps/desktop/main.py

zip:
	python scripts/package_release.py

all-checks: test validate papers-check
	python -m compileall -q src scripts classes apps
