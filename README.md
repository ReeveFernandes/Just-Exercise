# Just-Exercise

Just Exercise is an exercise-based app that was made on Python using mediapipe. The application can count the number of reps and set of a certain exercise that the user performs. When the user no longer wants to continue exercising, they can quit the app with a simple hand gesture. The app then asks for the user's name and adds their total rep score onto a leadersboard. The arcade-like setu of the application was inspired by Just Dance, which also inspired the app's name.

This app was created during the MakeUC hackathon held at the University of Cincinnati on 22nd and 23rd October, 2022. The app was built with the motivation to get people to exercise more and with greater enthusiasm! A simple arcade-based structure was used with hopes that the user will get competitive about trying to get a high score on the leadersboard and hence, will exercise more. 

The application programmers learnt how to use Mediapipe for python durng the hackathon and successfully implemented it to create this project. The app is largely made using Mediapipe because it aided with full-body recognition, allowing the program to track the movements of its user and count the number of reps they take.

The porgrammers faced challenges while trying to code the joint-to-joint connection of a human body (required to properly count reps) into the program. This process alone took a lot of trial and error to be implemented. Currently, the app can only recognise 5 types of exercise. We hope to program it to recognise more soon!









To run this website, first download [install OpenCV](https://google.github.io/mediapipe/getting_started/python.html)

```
-pip install mediapipe
```

##OpenCV Pose Estimation

