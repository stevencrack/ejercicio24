grafica.pdf: radio.py d.txt
	python radio.py

d.txt: radio.py
python radio.py > d.txt
