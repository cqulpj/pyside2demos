.PHONY:run

run:main.py MainDialog.py
	python3 main.py

MainDialog.py:MainDialog.ui
	pyside2-uic -o $@ $<

dist:main.py MainDialog.py CommonHelper.py
	pyinstaller -F -w main.py

