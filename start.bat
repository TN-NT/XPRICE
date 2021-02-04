@echo off
title XPRICE BY TIAGZ


:choice
set /P c= Do you install requirements [Y/N] = 
if /I "%c%" EQU "Y" goto :install
if /I "%c%" EQU "N" goto :start
goto :choice

:install
pip install requirements.txt
goto :start

:start
python "XPRICE.py"
pause