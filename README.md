# Detecting the Multiple States of Oyster Activity and Orientation using Deep Learnng Image Processing and Computer Vision Algorithim

## This research project was done and improved at Salisbury university as part of teh NSF REU Summer 2024 Program:
-[Salisbury University Website](https://www.salisbury.edu/)
  
-[NSF REU Salisbury Homepage](http://faculty.salisbury.edu/~ealu/REU/Schedule.html)

## Faculty Mentors:
 - Dr. Yuanwei Jin (Engineering Professor, University Maryland)
 -  Dr. Enyue (Annie) Lu (Computer Science Professor, Salisbury University)

## Project Title: 
    
Identification of Oysters in Imagines and Videos using Machine Learning

## Contributors:
 - Joshua Essandoh  (Computer Engineer, Virgina Tech), jessandoh7@vt.edu
 - Michael Straus  (Computer Science, Columbia University), mjs2435@columbia.edu
 - Nikolai Vukov   (Statistics, Salisbury University), nvukov1@gulls.salisbury.edu

## Previous Work Done:
 The groups before us were able to establish code using an older version of YOLO being YOLOv5. They were able to train YOLOv5 using over 800 imagines that they collected and annotated using [Roboflow](https://roboflow.com/) These imagines depicts oysters in three states (Closed,Semi-open,fully-open) within different environments. They were also able to address the problem of negative coordinate values by writting a shell script. They used [Google Colab](https://colab.research.google.com/) to conduct the trainning and [precision](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [recall](https://developers.google.com/machine-learning/crash-course/classification/precision-and-recall), [average precision (AP)](https://link.springer.com/referenceworkentry/10.1007/978-0-387-39940-9_482), and [mean average precision (mAP)](https://www.v7labs.com/blog/mean-average-precision#:~:text=Average%20Precision%20is%20calculated%20as,mAP%20varies%20in%20different%20contexts.) to conduct the evaluation.

Next, the group was able to determine the orientation to allow for more accurate classification of activity using [YOLOv5_OBB](https://github.com/hukaixuan19970627/yolov5_obb) to localized the oysters with rotated bounding boxes and apply color coded arrows that were parallel to the axis of orientation. Next, they were able to caculate depth inference of 3-dimensional images using [DenseDepth](https://github.com/ialhashim/DenseDepth).

# References & Acknowledgements: 
- [Detecting and Counting Oysters](https://arxiv.org/abs/2105.09758)
- [Fish Recognition Dataset](https://homepages.inf.ed.ac.uk/rbf/Fish4Knowledge/GROUNDTRUTH/RECOG/)
- [Underwater image processing](https://www.sciencedirect.com/science/article/pii/S0923596520302137)
- [Oyster detection system](https://github.com/bsadr/oyster-detection)
- [DenseDepth](https://github.com/ialhashim/DenseDepth)
- #[Remember to give credit to YOLOV8](Insert Yolov8_github link here)

## Methods:

### - DataSet:
The final dataset used can be found [here](https://app.roboflow.com/oyster-pt-3/reu_oyster_2024_improved/6). This dataset was formed by combining imagines found from the universal workspace [Bivalves Detection by DigiAqua](https://universe.roboflow.com/search?q=oyster) and media gathered by the 2022-2024 NSF REU project.

The dataset for this project was initially a combination of imagines found online through various sources like [Youtube](https://www.youtube.com/) and [Google](https://www.google.com/). The group in 2023 expanded this dataset by adding more imagines as well of videos that they took during their trip to [Horn Point Hatchery](https://hatchery.hpl.umces.edu/).This group also added 890 oysterless medias into the dataset to deter the model from commiting false postives. Lastly, in 2024 our group tried to expand this dataset by adding frames from videos that we've gather through youtube to expand the machine learning to better handel video annontations. We also added more oysterless photos into the dataset, finding photos that ranged from a single crush can of soda to piles of trash and debris underwater.

  While this was a good start, the model constantly failed to reach about 50% in [precision, recall,](https://blog.roboflow.com/precision-and-recall/) and [Average Precision](https://blog.roboflow.com/mean-average-precision/). 


### - Training:

### - Evaluation:

### - Website:

### - Results: 

## Additional Links & Resources:
- [3D boundary boxing paper](https://arxiv.org/pdf/1612.00496)
- [3D boundary boxing GitHub](https://github.com/skhadem/3D-BoundingBox/tree/master)
- [Ultralytics YOLOv8 all-encompasing guide](https://docs.ultralytics.com/)
- [YOLOv8 GitHub repository](https://github.com/ultralytics/ultralytics.git)
- [YOLOv10 Github](https://github.com/THU-MIG/yolov10)
- [Using YoloV10 on Video and Images](https://www.youtube.com/watch?v=YWpMgVGk2Y8)
- [Depth program for YOLO](https://github.com/ultralytics/ultralytics/issues/6920)
- [Training YOLOv10 for Videos](https://www.linkedin.com/posts/pyresearch_yolov10-how-to-train-for-object-detection-activity-7201118390420180992-2nX7)
- [How to Start a Google Storage Bucket](https://medium.com/google-cloud/automating-google-cloud-storage-management-with-python-92ba64ec8ea8)
- [Link to OddAI Github](https://github.com/michaelalt2304/oddai_website)
Please reach out to Michael Straus (mjstraus2304@gmail.com) with your Github account email for permission first, since OddAI is private for Google key integrity reasons.

## Getting Started:

To get started, please go to [Getting Started](https://github.com/NikolaiVukov21/Shellfish_project_2024/blob/Grand-Master/GettingStarted.md)

