# Cricket-Ball-Tracking
This project presents a ball tracking technique that detects and follows a pink ball in test cricket video frames using color segmentation, contour analysis, and Kalman filtering. The approach provides accurate, frame-by-frame estimation of the ball’s position and predicted trajectory in real time, utilizing fundamental image processing methods.

__Course Concepts -__
  1. OpenCV - taught in AHP sessions
  2. Morphological Image Processing

**Additional Concepts -**
  1. Kalman Filtering
  2. HSV Masking
  3. Video Processing using OpenCV

**Testing Datasets -**
https://drive.google.com/drive/folders/1QE91bxsNMkBc9JFOlXJj6DIavCFzku0n

**Novelty -**
  1. The approach strictly relies on digital image processing, making it simple and
     accessible for real-time sports analytics or educational demonstrations without any
     machine learning.

  2. Key contributions include fine-tuning color segmentation, optimizing morphological
     operations for robustness in different lighting, and integrating all steps into a
     consistent workflow for accurate ball tracking.

**Contributors -**
  1. Sagar Rao M - PES1UG23EC262
  2. Sai Charan S - PES1UG23EC264
  3. Sai Sampath Sreeram Makala - PES1UG23EC265

**Outputs -**
<img width="819" height="388" alt="image" src="https://github.com/user-attachments/assets/d89e5f98-0c10-4178-8d66-1fec927ed349" />

<img width="441" height="729" alt="image" src="https://github.com/user-attachments/assets/d3c0358a-01a1-4a3b-aa73-d7ed3a6a43de" />

<img width="702" height="381" alt="image" src="https://github.com/user-attachments/assets/49e32d34-7d81-46c9-a2d5-c4d7f7d496d3" />

<img width="925" height="501" alt="image" src="https://github.com/user-attachments/assets/a4446a2a-7c9e-4c81-8f0e-fdba270c8007" />

**References -**
  1. https://docs.opencv.org/4.x/
  2. Learning OpenCV: Computer Vision with the OpenCV Library -By Gary Bradski and
     Adrian Kaehler

**Limitations and Future Works -**
a. Limitations - 
  1. Looks for the color pink specifically so if the wickets/shoes are pink then it could cause issues.
  2. Detects when there is no ball in the frame, or nothing pink in the frame.
b. Future Works - 
  1. Real-Time Implementation
  2. Use ML for more accuracy
  3. Remove Sampi from team

  





