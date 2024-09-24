@echo off

REM 引数は2つ以上指定されているか？
if "%1"=="" (
	echo Usage: %0 filename
	exit /b
)

if "%1"=="abc" (
	if "%2"=="" (
		echo Usage: %0 filename
		exit /b
	)

	mkdir abc%2
	copy template\* abc%2
	chdir abc%2
	exit /b
)
