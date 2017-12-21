Final project for EECS 6893 Big Data Analytics
===========================================================
Yelp Photos Recommendation

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
	$ python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --model_dir=tf_files/models/ \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --image_dir=tf_files/'Your Directory'
	```
	Change the --image_dir=tf_files/'Your Directory' to Your Directory of dataset.

 Our Accuracy and Loss
-------------------
![Accuracy and Loss](https://bytebucket.org/md3487/ecbm4040_final_project/raw/9ffde6c159cd4b81d6a5d91874332f1e0e3d5420/images/accuracy.png?token=dc66c84fe111f192d8a8a60347ab4c0701d304e2)


