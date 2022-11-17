# OCR_Skewed_Document_App

### Problem Description

An insurance company is working on a system that can perform Optical Character Recognition (OCR) on documents from their archives. Unfortunately, their documents have been scanned at angles ranging from -5° to 5° from the horizontal. To increase OCR accuracy, they need a preprocessing step that determines the angle of a given page so this distortion can be corrected.


### Approach

- The input of learning algorithm will be the scanned document images and the labels which are the different possible scanning angles.

- Labels have been provided, treat with the problem as regression problem to get accurate result as much as possible.

- Here we are trying to solve this probelm using Classical approaches **Hough Transform**.

- Using Hough Transform Algorithm to Detection and Correction Skewed Document.

- Using OCR to see our result **pytesseract** model provided by Google.

- Build web app using django.

- Optional:- deploy Using heroku.

Data link:-

https://www.kaggle.com/datasets/sthabile/noisy-and-rotated-scanned-documents

### Challenges

Work with noisy and rotated document images which language Spanish that make OCR model perform poor.
Get only words with accuarcy more than 60%.

### Result

Achieve with mean square error on 500 label data 0.09492877999439271 error loss without rounding angle with rounding get 0.054 error.
Execution time less than: 
300 ms ± 38.9 ms per loop (mean ± std. dev. of 7 runs, 1 loop each).

### References
- [Fast Hough Transform](https://arxiv.org/abs/1912.02504v1).
Bezmaternykh, P. V., and Dmitry P. Nikolaev. "A document skew detection method using fast Hough transform." Twelfth International Conference on Machine Vision (ICMV 2019). Vol. 11433. SPIE, 2020.
- [Skew Detection and Correction using Hough Transform](https://muthu.co/skew-detection-and-correction-of-document-images-using-hough-transform/).
 Muthukrishnan,Computer Vision,August 22, 2020.
- [Skew correction in Documents using Deep learning](https://medium.com/mlearning-ai/skew-correction-in-documents-using-deep-learning-8e19609107b6).
  Vishnu Nandakumar.

