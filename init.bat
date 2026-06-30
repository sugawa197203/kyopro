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

	mkdir -p abc%2
	copy template\abc\python\* abc%2
	chdir abc%2
    uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
    uv sync
	cmd
	exit /b
)else if "%1"=="other" (
	if "%2"=="" (
		echo Usage: %0 filename
		exit /b
	)

	mkdir -p %2
	copy template\other\* %2
	chdir %2
	uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
	uv sync
	cmd
	exit /b
)else if "%1"=="adt" (
	if "%2"=="" (
		echo Usage: %0 filename
		exit /b
	)

	mkdir -p adt\%2
	copy template\other\* adt\%2
	chdir adt\%2
	uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
	uv sync
	cmd
	exit /b
)else if "%1"=="arc" (
	if "%2"=="" (
		echo Usage: %0 filename
		exit /b
	)

	mkdir -p arc\%2
	copy template\other\* arc\%2
	chdir arc\%2
	uv init .
	uv add numpy sortedcontainers git+https://github.com/not522/ac-library-python
	uv sync
	cmd
	exit /b
)

