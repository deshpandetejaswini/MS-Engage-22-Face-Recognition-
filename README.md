# MS-Engage-22-Face-Recognition
ATTENDANCE GOVERNANCE SYSTEM (USING FACE RECOGNISION)




This project involves development of web application which takes attendance as well as maintains attendance records.It implements features such as face recognission as well as detection and marks the in-time, out -time and presence of a employees.It exhibits the attendance in form of  graphs and tabular format in accordance to the requirement of admin/employee.The graphs help in visualization of data such as number of hours a particular employee has worked ,number of employees present at that day .It helps to automate the treditional way of tacking as well and maintaining attendance .This project can be implemented for schools,offices and the places where attendance tracking is necessary.





SYSTEM FLOW
ADMIN DASHBOARD 



1.Registration of a new employee/student by admin

2.Clicking of photos by webcam for the dataset

3.Training of dataset






![admin dashboard](https://user-images.githubusercontent.com/102857029/170040527-11c6eb0e-4823-41d2-9bec-aa3788abd6d0.JPG)






4.Viewing attendance report by admin 


   ATTENDANCE DASHBOARD-This dashboard gives the admin information regarding
   
   
 a)Shows statistics-Number of employees present on that day ,graph for previous week and ongoing week (no of employee vs date)
   
   
 b)Attendance report for a particular employee-attendence of a employee in a particular duration(duration is inserted by admin according to his convinence.Also this webpage shows graph between number of hours that employee worked on all the different days he was present
   
   
   
c)Attendance of all the employees for a particular date- Number of employees present on a particular date with graph representing number of hours each employee          was present at that particular date(date is inserted by the admin according to his convinience)

5.Employee dashboard - Graph showing number of hours worked on all the dates when he was present and showing statistics such as intime and the out time of that employee


FLOW OF 
           FACE DETECTION
1.HOG face detector-Histogram Oriented Gradients (HOG) used in computer vision for object detection.


2.Shape Predictor-dilib Frontal Facial landmark predictor is used 


 Shape _predictor_68_face landmark -It estimates the location of 68 co-ordinates (x, y) that map the facial points of a particular person’s face.


 CAPTURING IMAGES FROM WEBCAM
 
 
1.Capturing image by webcam at that instant using vs=VedioStream (src=0)


2.Read from the image for each frame vs.read() 


3.Resizing the image 


4.Converting Colored image to black and white image (for classifiers to work we need gray style image)


5.Storing the faces- Detecting all the images in the current frame and returning the co-ordinates of faces.


6.Drawing the rectangle around each face which webcam has captured.


7.Writing the captured face in the file in the folder. Before capturing the face, we need to tell the script whose face it is. We save the image in the dataset, but only the face part we crop the remaining part.


8.After capturing image stop the video stream .





