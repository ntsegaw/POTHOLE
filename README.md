# Pothole Classifier

## Business Understanding
Drivers in the DC metro area very often face the challenge of driving on roads littered with potholes throughout each respective county. Among each county is a totally different method of pothole identification. Mix that in with drivers commuting throughout state and county lines and you have an identification system in which users may have a tough time reporting the potholes to the respective authorities. The goals of this project are therefore threefold. This project aims to simplify, speed up, and modernize the pothole reporting process for the DMV. 

The project also has the long-term goal of creating a substantial data set of potholes. Currently there are not many robust pothole detectors that are currently used. Nor are there particularly large, for commercial purposes, data sets available of potholes. 

![alt text](https://raw.githubusercontent.com/ntsegaw/POTHOLE/master/images/Unknown-2.png)

And among the more robust models contains much more sensitive equipment than an iPhone for example. By having a simple and straightforward way for people to submit images of potholes to their respective counties or states not only will potholes be identified and hopefully filled up faster, but in the future the same images can be used to increase the accuracy of the model and be used to detect potholes in real time passively. If for example a car owned by the county was equipped with a dash cam, GPS, and perhaps a raspberry pi, the car may one day be able to automatically notify the proper authorities to a pothole on the road, not having to wait for an individual to whip out their phone. 



## Notebook steps
Beginning with the Data itself, images of potholes and smooth roads were gathered using various Kagle data sets linked here and here and through two batch downloaders, FATKUN, and simple image downloader. Light oversight was needed for images downloaded using batch downloader tools to make sure the model wasn’t being fed data it didn’t need to be fed. 

![alt text](https://github.com/ntsegaw/POTHOLE/blob/master/images/Unknown-3.png)

After the data sets were found and created came the process of manipulating the images for my model. Throughout the process I created for different models. The first was rather simple and created to test out what would be considered a baseline model. Images were set to one 150 x 150 and converted to grayscale. Then they were passed through a CNN in which the validation accuracy was over 80%. With approximately 800 pictures in each class, not a pothole or a pothole, the model was looking good. However the best performance came from my fourth model which also took the most time. The model and it up with a 91% validation accuracy and furthermore by using lime I was able to better interpret what it is that my model saw.

![alt text](https://raw.githubusercontent.com/ntsegaw/POTHOLE/master/images/Unknown-4.png)

Next came the actual data gathering process from the image. Using various packages, including PIL, I was able to extract metadata from photos taken throughout my neighborhood to pinpoint where exactly a pothole was found. The coordinates can be found under ‘GPS info’. 


![alt text](https://github.com/ntsegaw/POTHOLE/blob/master/images/Unknown-5.png)

![alt text](https://github.com/ntsegaw/POTHOLE/blob/master/images/Unknown-6.png)

As you can see the model did correctly identify where the pothole is. However, it also identified the section to left as part of the pothole. A sign that more training is needed.

## Future Improvements
As mentioned in the business understanding section there are several ways in which the model can be improved. Other than potentially useful applications to be built on top of the model there are certain weaknesses that the model has. First and foremost is the lack of data. There are an extreme amount of roadside variables that this model is not trained for. For example intense shadows can fool the model. Furthermore, potholes tend to develop in the winter, what of salt and snow on the roads. And on top of that what of cracks in the road. When does a crack become a pothole? Not only does the data need to be gathered but it also needs to be correctly labeled. While there are many ways in which the model can be improved upon as it is now under favorable conditions it is fairly accurate at locating potholes within an image and as mentioned before can prove to be the steppingstones in which Real time modeling can occur.


## Presentation Link
https://drive.google.com/file/d/1Mfnyqs16zMYVeOdCydI4aPQxUbwIHaeS/view?usp=sharing

## Sources Links
https://www.kaggle.com/atulyakumar98/pothole-detection-dataset


https://www.kaggle.com/sachinpatel21/pothole-image-dataset
