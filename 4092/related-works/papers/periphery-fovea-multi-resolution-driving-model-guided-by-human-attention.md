Paper: [Periphery-Fovea Multi-Resolution Driving Model Guided by Human Attention](https://openaccess.thecvf.com/content_WACV_2020/papers/Xia_Periphery-Fovea_Multi-Resolution_Driving_Model_Guided_by_Human_Attention_WACV_2020_paper.pdf)

GitHub: [Periphery Fovea Driving](https://github.com/pascalxia/periphery_fovea_driving)
# Introduction
* Vision based driving models have shown promising results but are still far behind humans, due to human vision's multi-res. property.
    * Human vision has Foveal (central visual field) and Peripheral (long range low-res. field)
* This property is advantageous due to its efficiency:
    * Peripheral processes long-range structures in low-res.
    * Foveal dictates resources to salient regions
* Driving contains both long range structures (curves and crossings) and localised regions (pedestrians and traffic signs)
* 1st challenge: Combining both views. Sol. 1: Combined peripheral-fovea planner. Sol. 2: 2 independent peripheral-foveal planners
* 2nd challenge: Guiding foveal vision. Sol.: Guidance with human gaze.
    * Potential problem: Both predicted and ground truth human gaze have not been tested on their benefit to auto. driving models.
 
# Related Works
## End-to-end Learning
* Driving policies can be learnt by NN.
* 2 factors restrict current controllers from learning how to drive:
    1. Low-res. inputs: Done to reduce computational burden. High-res. inputs are required to recognise far away objects.
    2. Uni-res. processing: This wastes computational resources on non-salient regions or produces suboptimal performance.
* Periphery-fovea has been shown to be effective for predicting human gaze.

## Incorporation of Visual Attention
* Human attention prediction for Altari games has been incorporated into the policy network and improved the action prediction accuracy.
* Human visual attention in driving tasks has not yet been incorporated and explored.
* Current visual models can handle basic cues (stop signs, etc.) but struggle with complex ones (pedestrians).

## Predicting Driver Attention
* Human driver attention has been successfully modelled within probabilistic modelling techniques and has been demonstrated to be important in cognitive and social challenges when driving.

# Model
* Takes dash cam video frames and outputs a control signal (in this case speed one second in the future).
* Mimics peripheral (processes video in low-res. to capture long range structures) and foveal (process in high-res. to capture salient regions) systems which are then combined to make a prediction.
* 4 parts, as detailed below:

## Peripheral Visual Encoder
* Extracts high-level convolutional visual features.
* Low-res. images are fed to a CNN which outputs features (a set of co-ordinates) at each time-step which is then consumed by the human attention prediction module and the peripheral-foveal planner.

## Human Attention Prediction Module
* Learns the behaviour of human attention as a supervised learner over image-gaze pairs collected from humans.
* Trained to predict multi-focal human driver attention conditioned on visual features at each time-step.
* The attention function follows the model: [Driver Attention Prediction](https://github.com/pascalxia/driver_attention_prediction).

## Foveal Visual Encoder
* Selects fovea locations, crops the high res. fovea image patches and extracts visual features from said patches.
* The model chooses a number of independent fovea locations for each image. The probability of each location is calculated with respect to temperature factor.
    * Higher temperature factor = Uniform sampling. Lower = sampling from pixels that have the highest attention intensity.
* An image patch is cropped out of the high res. image and its size is determined by clustering of the predicted attention map (this paper restricts the size to 240x240 to improve efficiency).
* The patches are then downsized, raw pixel values are subtracted by a global mean and then passed to the encoder network.

## Peripheral-Foveal Planner
* Combines the peripheral and foveal visual features to make a prediction.
* Creates a foveal feature map which the foveal feature patches are inserted into at locations corresponding to the foveal location.
    * If feature patches overlap, the maximum of each pair is kept.
* Next the peripheral and foveal feature maps are concatenated which is then processed and the speed prediction is made.

# Experiments Setup
## Datasets
* BDD-X: To train and evaluate the driving model. Human-demonstrated dashboard videos in urban settings at various weather/lighting conditions. Includes sensor measurements.
* DR(eye)VE: To test generalisability of models. Human-demonstrated dashboard videos in urban settings in various weather/lighting conditions and times of day.
* BDD-A: To train the human attention prediction module. Similar to BDD-X (but not the same), also provides human attention maps.

## Training
* Video frames are sampled at 10Hz and downsized from 720x1280 to 72x128 and then normalised by subtracting the global mean from the raw pixels.
* Next identical ConvNet base is followed by batch normalisation and dropout.

## Evaluation
* To evaluate speed accuracy the mean absolute error, root-mean-square error and correlation coefficient are used to test against ground truths.

# Results
## Multi-Res. vs Uni-Res.
* Uni-res. prediction errors would increase as video length did.
* Multi-res. prediction errors stayed stable as video length increased.

## Incorporation of Human Attentions
* Compared top-2 model against central fovea section model, as this is most representative of where a vehicle is driving.
* Top-2 model outperformed central model. Note that random fovea selection performed worse than no fovea.

## Top-2 vs Sampled
* A concern when using top-2 is that it may select adjacent locations or the same focus in the next frames, sampling solves this.
* Sampling is determined according to the predicted human attention probability distribution and modulated by a temperature factor.
* Results showed that a balance between high likelihood and low overlap would result in optimal performance. Sampling following the predicted human attention distribution showed the best accuracy.

## Combined vs Dual Planner
* Currently the planner processes peripheral and foveal together, in this attempt they are processed using separate ConvLSTM networks. This did not prove to be better.

## Pedestrian Scenarios
* The model was tested specifically in pedestrian annotated portions of the videos and performed better that non-foveal models


