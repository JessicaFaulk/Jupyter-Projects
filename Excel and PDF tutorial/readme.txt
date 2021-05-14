Read Me:

This series can be used to learn how to use the following packages to create excel and PDF files
from a general data csv, to include formatting.

1. pyxl
2. XLSXWrite
3. Jijna2
4. HTML IPython.display
5. Pandas
6. Numpy
7. datetime

I have some extra packages, but I need to check them before removing those lines.

This report requires one data file and a table of holidays for the work days calculation.

The "Excel Files - All Reports" contains all the outputs of the various reports made from the data.
The " HTML Files - Admin Complaints" contains all the HTML pages that are then shunted into a pdf 
	maker of your choice (I used Adobe Acrobat DC) and combined multiple pages into one binder.
The "PDF Files - Admin Complaints" is the PDF file generate from the folder of HTML files.

All output is sent to the top directory. If you wanted, I guess you could direct them into the 
	appropriate folders. 
Two HTML files are located in the topmost directory:
	mytemplate.html
	summary.html
* Please do not move them, it's easier to keep them here.

These are used in conjunction with the JINJA2 package to create and format the HTML output pages. 
	Summary is code that is called up to the mytemplate.html page to create the final page output.
	If you change a variable in the mytemplate.html page or in the notebook, be sure to refer to the
	summary.html page to ensure that all parts are up to date.

Data Disclaimer:
	This data is anonymized with random names, random tracking numbers and agency names changed.
