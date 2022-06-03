.PHONY:run

run:main.py MainDialog.py
	python3 main.py

MainDialog.py:MainDialog.ui
	pyside2-uic -o $@ $<

dist:main.py MainDialog.py 
	pyinstaller -F -w -i visitor.ico -n jgbDataCapturer main.py

