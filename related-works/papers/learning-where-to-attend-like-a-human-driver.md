Paper: [Learning Where to Attend Like a Human Driver](https://arxiv.org/pdf/1611.08215.pdf)

# Introduction
* Modern Advanced Driver Assistance Systems are human-centric and rely on monitoring the driver to predict unsafe situations (this method is limited)
* The paper proposed a new paradigm which suggests to the driver where they should focus their attention
    1. Investigates attentional dynamic when driving
    2. Creates a human attention models and evaluates it against humans
 
# Related Works
* Head pose and gaze estimation: Infer dangerous driving habits, next manoeuvres from driving monitoring or scene analysis
* Video saliency: Extracting features from an image
 
# Methodology
* Uses DR(eye)VE
* Most drivers focus on the vanishing point of the road and use peripheral vision to observe signs, cars, etc.
* The faster the car travels or the more object in FOV reduce the size of the visual field.
    * Gaze must be moved around more to conpensate for this
* Model takes in 16 frames and outputs the gaze map of the last frame
 
#Evaluation/Throughts
* The model is successful but only evaluates 16 frames and produces 1 result
