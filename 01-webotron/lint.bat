@echo off


pipenv run pydocstyle webotron/

pipenv run pyflakes webotron/
