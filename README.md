This repository contains my attempt for I_Hack by E-Cell IIT Bombay.
I'm planning to use CV along with classical image processing for the task

Dependencies
PIL ( pip install Pillow )
pdf2image ( pip install pdf2image )
docxtopdf ( pip install docxtopdf )
subprocess ( builtin for versions above python2.7 )
opencv (pip install opencv )
scipy ( pip install scipy )
imutils ( pip install imutils )


Input Files
Make sure that the name without the extension is unique. ( person.docx and person.jpg should not be present together )
Input formats accepted:
docx ( the older .doc version was dropped from MS Word 2007, it is highly unlikely someone is still using doc files )
pdf
jpeg
jpg
png

Assumptions:
It is reasonable to assume that, on a given page multiple id proofs won't be present.
For example, pan card and adhar card both won't be present on the same pdf page, although aadhar front and back might be
on the same page. This assumption is validated by talking to various xerox operators.



