# Instructions to Reproduce
Preface: During my attempts to run this project I experimented with both python venvs and anaconda virtual environments. I was able to get results with both but for some reason I could not get tensorflow-gpu to work with python venvs (meaning longer run times). Below I will detail both methods but reccomend anaconda virtual environments.

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

## Anaconda Virtual Environments Method

### Environment Setup

#### Create an anaconda environment
Following: [Managing Environments](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#activating-an-environment)
1. `conda create -n [environment name] python=3.5.6 tensorflow-gpu==1.10.0 cudatoolkit==9.2 cudnn==7.6.5`
2. `conda activate [environment name]`

#### Install required packages
Following the dockerfile (`./docker_images/tf150_kr215/Dockerfile`) at: [Driver Attention Prediction](https://github.com/pascalxia/driver_attention_prediction)

NOTE: Some packages could not be found (even when searching on conda forge) and had to be installed via pip
1. `sudo apt-get update`
2. `sudo apt-get install -y ffmpeg`
3. `pip install feather-format
4. `conda install keras==2.1.5`
5. `conda install moviepy`
6. `pip install opencv-python==3.2.0.8`
7. `conda install pandas`
8. `conda install tqdm`

NOTE: I was having issues with scipy and had to uninstall and reinstall scipy 1.2.0 via `pip uninstall scipy` and then `pip install scipy==1.2.0`

#### Running the code
Please follow the steps detailed on: [Driver Attention Prediction](https://github.com/pascalxia/driver_attention_prediction)

NOTE: I encoutered and error when running the code and had to add `allow_pickle=True` to the function call parameters on line 7 in my_alexnet.py
NOTE: Total runtime for me was ~10 mins

## Python venvs Method

### Environment Setup

#### Install pyenv
Following the stepos at: [Install pyenv and venv](https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu)
1. `sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git`
2. `git clone https://github.com/pyenv/pyenv.git ~/.pyenv`
3. `echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc`

#### Create a venv
Following the stepos at: [Install pyenv and venv](https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu)
1. Open a terminal at the project directory
2. `pyenv local 3.5.10`
3. `python -m venv .venv`
4. `source .venv/bin/activate`

#### Install required packages
Following the dockerfile (`./docker_images/tf150_kr215/Dockerfile`) at: [Driver Attention Prediction](https://github.com/pascalxia/driver_attention_prediction)
1. `pip install --upgrade pip`
2. `pip install tensorflow==1.5.0`
3. `pip install ffmpeg`
4. `pip install feather-format`
5. `pip install keras==2.1.5`
6. `pip install moviepy`
7. `pip install opencv-python==3.2.0.8`
8. `pip install pandas`
9. `pip install tqdm`

NOTE: I was having issues with scipy and had to uninstall and reinstall scipy 1.2.0 via `pip uninstall scipy` and then `pip install scipy==1.2.0`

#### Running the code
Please follow the steps detailed on: [Driver Attention Prediction](https://github.com/pascalxia/driver_attention_prediction)

NOTE: I encoutered and error when running the code and had to add `allow_pickle=True` to the function call parameters on line 7 in my_alexnet.py
NOTE: Total runtime for me was ~30 mins
