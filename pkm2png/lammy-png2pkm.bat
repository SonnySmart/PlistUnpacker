@echo off

set /p a=please input png dictionary: 
DIR %a% /B >list.txt

@echo convert start ...
for /f "delims=[" %%i in (list.txt) do etcpack.exe %a%/%%i %a%_pkm -c etc1 -s slow -as -ext PNG

@echo png successful convert to pkm

del list.txt
pause