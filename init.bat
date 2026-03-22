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
	copy template\abc\python\* abc%2
	chdir abc%2
    uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
    uv sync
	exit /b
)else if "%1"=="other" (
	if "%2"=="" (
		echo Usage: %0 filename
		exit /b
	)

	mkdir %2
	copy template\other\* %2
	chdir %2
	uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
	uv sync
	exit /b
)
