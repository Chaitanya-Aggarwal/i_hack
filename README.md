## About this
This repository contains my solution to the i_hack machine learning and data science hackathon organized by Entrepreneur Cell, IIT Bombay in collaboration with Primal Finance. E-KYC is a challenging domain and classifying the variety of documents submitted by users online manually is a time consuming process. The aim of this model was to classify differnt types of identity proofs submitted by users into categories such as Pan Card, Aadhar Card, Voter Card etc and read data from them. The variety of formats in which these documents are avalaible and privacy concers related to them make desiging and training the machine learning model very hard. Still an acceptable level of accuracy has been achieved. The pipeline accepts the input in a variety of formats (pdf, jpeg, png etc.) and tries to classify whatever is present in the documents. 

## Achievement
The model was placed at 3rd position in the Hackathon, beaten only by the much more resource intesive models based on inverse pyramid designs. 

## Approach
This repository contains my attempt for I_Hack by E-Cell IIT Bombay. I've used deep learning along with transfer learning to create the model and trained the last 1000 variables on 5000+ images. The images were created artifically using image augmentation techniques to create real world distortions, blurring and rotations.  

## Dependencies
PIL ( pip install Pillow )
pdf2image ( pip install pdf2image )
docxtopdf ( pip install docxtopdf )
subprocess ( builtin for versions above python2.7 )
opencv (pip install opencv )
scipy ( pip install scipy )
imutils ( pip install imutils )
dlib ( pip install dlib )


## Input Files
Make sure that the name without the extension is unique. ( person.docx and person.jpg should not be present together )
Input formats accepted:
docx ( the older .doc version was dropped from MS Word 2007, it is highly unlikely someone is still using doc files )
pdf
jpeg
jpg
png

Assumptions:
It is reasonable to assume that, on a given page multiple id proofs won't be present. For example, pan card and adhar card both won't be present on the same pdf page, although aadhar front and back might beon the same page.
