Final project for EECS 6893 Big Data Analytics
===========================================================
Yelp Photos Recommendation

More than 100,000 photos are uploaded by Yelp users every day, and this rate is even growing. A fancy picture aside with positive reviews will highly contributes to the first impression of a restaurant. While a terrible cover photo will ruin the efforts of a good restaurant. In this paper, we intro- duce a system to select fascinating Yelp photos with different category such as food, drink, menu, etc. Two deep convolution neural network models, AlexNet and Re-Trained Inception- v3 model, are used in our scoring system and diversification system respectively. We reach more than 90 % accuracy for the classification and scoring. Our system can contribute to several applications such as cover photo sorting.


Follow instrctions below will work on a your local PC or a newly created GCP instance. If you have any problems running the code, please contact us.

If you want to use the system without training, please contact us for our pretrained model files.

Setup
------------
1. Install python dependencies
	```
	$ pip install -r requirements.txt
	```
2. Downloaded Dataset you want ot train with. (Yelp Challenge Dataset or your own)
	For classification task, download the dataset with each catagories in one subfolder.



Usage
-------------
1. Scoring System (training)
	Follow the instruction and demo from Scoring.ipynb

2. Classification System (training)
	```
	$ python -m scripts.retrain \ --bottleneck_dir=tf_files/bottlenecks \ --model_dir=tf_files/models/ \ --output_graph=tf_files/retrained_graph.pb \ --output_labels=tf_files/retrained_labels.txt \ --image_dir=tf_files/'Your Directory'
	```
	Change the --image_dir=tf_files/'Your Directory' to Your Directory of dataset.

 Our Accuracy and Loss
-------------------
![Accuracy and Loss](https://github.com/Sapphirine/YelpRecommendation/blob/master/img/acc.png)(https://github.com/Sapphirine/YelpRecommendation/blob/master/img/loss.png)


