@echo off
Title "run"
cmd /k "cd Env\Scripts & activate & cd ..\..\ & py manage.py runserver 192.168.1.58:80"