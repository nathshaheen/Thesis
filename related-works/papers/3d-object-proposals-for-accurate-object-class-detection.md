Paper: [3D Object Proposals for Accurate Object Class Detection](https://proceedings.neurips.cc/paper/2015/file/6da37dd3139aa4d9aa55b8d237ec5d4a-Paper.pdf)

# Introduction
* Modern day cars have many cameras which can be used for autonomous driving.
* Object detection has improved by shifting from sliding window to multi-layer visual representations (Selective search, energy minimization)
* Current approaches do not work well in auto. driving applications
* This paper's approach reasons in 3D and utilizes various features to improve current detection models
 
#Related Works
* RGB:
    * Combine super pixels into larger regions based on colour, texture, etc.
    * These regions can then be scored based on various features
* RGB-D:
    * Like RGB but includes depth data
    * Current models have been trained on CAD models
 
# Methodology
1. Depth computed via sota approach
2. Propose generation as an energy minimization problem
3. Discretise accumulators
4. Perform inference
5. Perform learning
6. Estimate objects and their orientation
 
# Evaluation
* Tested on KITTI dataset - moderate regime was used to rank different methods
* Improvements in reaching 90% recall compared to sota
    * This model requires less candidates or can reach higher recall %'s in the same number of candidates
* Faster runtimes
* Precise proposals
* Improvements in all categories over sota for both object detection and orientation
 
# Thoughts
* Very thorough but do all objects need to be labelled and are the relevant to autonomous driving improvements (See DrEYEVe paper)
