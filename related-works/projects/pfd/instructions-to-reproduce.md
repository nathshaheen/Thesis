# Instructions to Reproduce

## My Setup

### Hardware
* CPU: Intel i9-9900k
* GPU: Nvidia GeForce RTX 2080ti
* RAM: 32 GB RAM

### Software
* OS: Ubunutu 20.04
* Nvidia Drivers: 470.103.01
  * CUDA 10.1
  * CuDNN 8.0.5

## Prepare the Data
Following step 1 from: [Periphery Fovea Driving](https://github.com/pascalxia/periphery_fovea_driving)

### Environment Setup

#### Create an anaconda environment
Following: [Managing Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
1. `conda create -n [environment name] python=3.5.6 tensorflow-gpu==1.10.0 cudatoolkit==9.2 cudnn==7.6.5`
2. `conda activate [environment name]`

#### Install required packages
Following the dockerfile (`./docker_images/bdd/Dockerfile`) at: [BDD Driving Model](https://github.com/pascalxia/BDD_Driving_Model-1)

NOTE: Some packages could not be found (even when searching on conda forge) and had to be installed via pip
1. `sudo add-apt-repository -y ppa:mc3man/trusty-media`
2. `sudo apt-get update`
3. `sudo apt-get install -y dist-upgrade`
4. `sudo apt-get install -y ffmpeg`
5. `pip install opencv-python`
6. `conda install pillow`
7. `conda install scikit-learn`
8. `conda install pandas`
9. `conda install tqdm`
10. `pip install feather-format`

#### Running the code
Please follow the steps detailed on: [BDD Driving Model](https://github.com/pascalxia/BDD_Driving_Model-1)

NOTE: I encoutered errors when running the code and had to change lines in both filter.py and prepare_tfrecords_bddx.py. I have provided both files incase you wish to use them (find them in this directory under the same names)
NOTE: In my attempts to obtain the BDD-V datset from [BDD Datasets](https://bdd-data.berkeley.edu/) it was no where to be found. Instead I used the following files:
* BDD100K "Info" for video info
* BDD100K video parts "bdd100k_videos_train_00.zip" for train videos
* BDD100K video parts "bdd100k_videos_val_00.zip " for validation and test videos

NOTE: In doing this you will need to find video, info pairs and create both `./data/videos/test/info/` and `/data/videos/test/videos/` directories to place the above downloads in (this also applies to validation (`./data/videos/val/info/`, etc) and train (`./data/videos/train/info/`, etc).
