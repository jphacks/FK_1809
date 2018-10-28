@ECHO OFF
IF NOT "%~f0" == "~f0" GOTO :WinNT
@"C:\Ruby24\bin\ruby.exe" "D:/test_app/vendor/bundle/ruby/2.4.0/bin/rackup" %1 %2 %3 %4 %5 %6 %7 %8 %9
GOTO :EOF
:WinNT
@"C:\Ruby24\bin\ruby.exe" "%~dpn0" %*
