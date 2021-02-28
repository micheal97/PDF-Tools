@echo off

SET ext=-p.pdf
SET pdfext=.pdf


FOR /R %%G IN (*.pdf) DO (

	FOR %%A in ('%%G') do (
    		
		gswin64c.exe ^
			-dPDFA ^
        		-dBATCH ^
        		-dNOPAUSE ^
        		-dUseCIEColor ^
        		-sProcessColorModel=DeviceCMYK ^
        		-sPAPERSIZE=a4 ^
        		-sDEVICE=pdfwrite ^
        		-sPDFACompatibilityPolicy=1 ^
        		-sOutputFile=%%~nA%ext% ^
        		%%~nA%pdfext% ^
	)


)	