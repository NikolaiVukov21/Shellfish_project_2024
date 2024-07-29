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
The data set for these tests were collected using clips found through online, primarily through youtube channels (All credits can be found in References). In total we were able to collect 8 videos that ranged from a few seconds still photos of a single oyster to long moving videos of multiple oysters.
### - Training:

### - Evaluation:

### - Website:

### - Results 

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

