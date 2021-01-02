.PHONY:run

run:main.py complex_window.py
	python3 main.py

complex_window.py:complex_window.ui
	pyside2-uic -o $@ $<
