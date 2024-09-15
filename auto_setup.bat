@echo off

:: Variables for Git installation
set installDir=%1
if [%1]==[] set installDir="C:\Program Files\Git"
set installDir=%installDir:"=%

:: Create config file for Git installation
(
    echo [Setup]
    echo Lang=default
    echo Dir=%installDir%
    echo Group=Git
    echo NoIcons=0
    echo SetupType=default
    echo Components=icons,ext\reg\shellhere,assoc,assoc_sh
    echo Tasks=
    echo PathOption=Cmd
    echo SSHOption=OpenSSH
    echo CRLFOption=CRLFAlways
    echo BashTerminalOption=ConHost
    echo PerformanceTweaksFSCache=Enabled
    echo UseCredentialManager=Enabled
    echo EnableSymlinks=Disabled
    echo EnableBuiltinDifftool=Disabled
) > config.inf

:: Find Git executable
for /r %%f in (git*.exe) do (
    call set file="%%f"
    @echo on
    @echo %%f
    @echo off
)

:: Check if Git executable was found
if [%file%]==[] (
    @echo on
    @echo Error finding "git*.exe" install executable. File may not exist or is not named with the "git" prefix.
    exit /b 2
)

:: Install Git
@echo on
@echo Installing Git..
@echo off
%file% /VERYSILENT /LOADINF="config.inf"
if errorlevel 1 (
    @echo on
    if %errorLevel% == 1 ( echo Error opening %file%. File may be corrupt. )
    if %errorLevel% == 2 ( echo Error reading %file%. May require elevated privileges. Run as administrator. )
    exit /b %errorlevel%
)
del config.inf

:: Check if script is running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    pathman /as "%PATH%;%installDir%/cmd"
) else (
    @echo on
    echo SYSTEM PATH Environment Variable may not be set, may require elevated privileges. Run as administrator if it doesn't already exist.
    exit /b 0
)

:: Clone the repository and run setup.bat
echo,
echo ------------------------------------------------------------------
echo Cloning repository and running setup.bat
echo ------------------------------------------------------------------
echo,

git clone https://github.com/AndreikaKopeika/Discord-openai.git
cd Discord-openai
start setup.bat
