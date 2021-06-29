@echo off
cls
:start
echo Select an option
echo 0) Get start up instructions
echo 1) Add a new entry (POSTing to /birthday will post a new birthday , and create an entry)
echo 2) View entry by number (an entry that can be viewed at /birthday/:number: (like /birthday/0001 for the first entry))
echo 3) Update an entry by number (PUTing to /birthday/:number: will update details on that birthday)
echo 4) Show list of all entries (GETing  to /birthdays will list all birthdays in the system )
echo 5) Quit

SET/P _input=Please enter your choice: 
IF "%_input%"=="0" GOTO :Start
IF "%_input%"=="1" GOTO :AddNewEntry
IF "%_input%"=="2" GOTO :ViewEntryByNumber
IF "%_input%"=="3" GOTO :UpdateEntryByNumber
IF "%_input%"=="4" GOTO :ShowList
IF "%_input%"=="5" GOTO :end

:Start
	echo Run the supplied script on SQLLite script.txt
	echo Open cmd cd to the directory where the app.py file is
	echo Type python app.py
	echo Then select the command you want to execute.
	PAUSE
	GOTO :Start

:AddNewEntry
	SET/P Name=Please enter the name:
	SET/P Birthday=Please enter the Birthday:
	curl -X POST localhost:5000/Birthday -d "Name=%Name%&Birthday=%Birthday%"
	GOTO :Start

:ViewEntryByNumber
	SET/P EntryNumber=Please enter the number of the record you want to view: 
	echo viewing record %EntryNumber%
	curl -X GET http://localhost:5000/Birthday/%EntryNumber%
	PAUSE
	GOTO :Start

:UpdateEntryByNumber
	SET/P Name=Please enter the name:
	SET/P Birthday=Please enter the Birthday:
	SET/P Number=Please enter the Record Number:
	curl -X PUT localhost:5000/Birthday/%Number% -d "Name=%Name%&Birthday=%Birthday%"
	GOTO :Start

:ShowList
	echo Showing all records
	curl -X GET localhost:5000/Birthdays
	PAUSE
	GOTO :Start

:end
echo end
