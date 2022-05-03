# Introduction
* A humans ability to perceive and interact with traffic plays a crucial role in understanding a scene and improving vehicle control behaviour.
* Why a drivers see where and what is far from being understood
 
# Related Works
* Current systems rely on driver monitoring systems (head pose/eye location)
* There are many theoretical/computational models to explain eye movement but they are not reliable in complex naturalistic settings (driving)
* Saliency: Top-down events compete with bottom-up events but in driving bottom-up emerges naturally
    * Bottom-up: Identifies parts or events that stand out from the neighbouring background
    * Top-down: Task-driven, goal orientated. Conceptually a hard problem as different task require a different algorithm
 
# Methodology
* Frames with errors and stationary frames are excluded
 
# Evaluation
* Proposed method achieves higher correlation coefficients
* As experimental settings become more complex, bottom-up cues perform very poorly
* This method only uses a single frame to predict the fixation region
* Following the vanishing point is an optimal strategy to mimic drivers gaze
* There is a need to collect more reactive events for training and evaluation
 
# Thoughts
* This paper was a much easier read that the rest so far
* This model only takes in one frame to predict gaze and therefore does not require much computational power. This could be applied to a video sequence once it has been split into frames
