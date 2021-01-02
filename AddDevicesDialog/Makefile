.PHONY:run

run:main.py addDeviceFrame.py
	python3 main.py

addDeviceFrame.py:addDeviceFrame.ui
	pyside2-uic -o $@ $<
