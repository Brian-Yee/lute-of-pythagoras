help.stub: help
help:
	@echo "help     Display this message."
	@echo "run      Generate figure."
	@echo "clean    Standardize repository."
	@echo "test     Run testing suite."

run:
	python main.py 32 imgs/lute_of_pythagoras.svg

clean:
	black .

test:
	black --diff .
	pylint *.py src
