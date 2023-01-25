## Important
This repository is still under-development as due to academic commitments, I was unable to work on it last week. The major challenge of this model remains the lack of data due to privacy constrains. Therefore transfer learning model has been used. I've achieved correct classification for about 25% data among 8 sets. But while training the data, there is not much improvement after 2 epochs. This is clearly because the data of almost 500 images is insufficient for training 1000 variables. I'm currently working on aritifical data augmentation to create more test data to improve my model.

Also after a satisfactory level of accuracy has been rechieved, I plan to incorporate openCV, and OCR into the model to make it even better.

This repository contains my attempt for I_Hack by E-Cell IIT Bombay.
I'm planning to use CV along with classical image processing for the task.

Dependencies
PIL ( pip install Pillow )
pdf2image ( pip install pdf2image )
docxtopdf ( pip install docxtopdf )
subprocess ( builtin for versions above python2.7 )
opencv (pip install opencv )
scipy ( pip install scipy )
imutils ( pip install imutils )
dlib ( pip install dlib )


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


Approach 1
            Has Photo   Regex_With_AdharNumber or Regex_with_Aadhar  Regex_with_UniqueIdentificationAuthorityofIndia 
AadharFront 1           1                         Depends            Depends         
AadharBack  0           1                         Depends            Depends
AadharBoth  1           1                         Depends            Depends
