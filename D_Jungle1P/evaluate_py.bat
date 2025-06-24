@echo off
for %%G in (*.in) do (
	echo Processing %%G
	python main.py < %%G > tmp.ans
	fc %%~nG.ans tmp.ans
	del tmp.ans)
