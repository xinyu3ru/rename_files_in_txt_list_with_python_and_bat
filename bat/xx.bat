@echo off
for /r "d:\pdf" %%a in (*.pdf) do (
   for /f "tokens=1,2 delims= " %%b in (1.txt) do ( 
   if "%%~nxa"=="%%b" ren "%%a" "%%c.pdf"
   )
)