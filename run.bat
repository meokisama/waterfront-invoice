@echo off
cd /d %~dp0
call env\Scripts\activate
python render.py
call env\Scripts\deactivate