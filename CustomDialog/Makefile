.PHONY:run

run:MyDialog.py cusDialog.py
	python3 $< 

cusDialog.py:cusDialog.ui
	pyside2-uic -o $@ $<
