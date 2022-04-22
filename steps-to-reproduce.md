# Environment Setup (Ubuntu Linux):

## Install pyenv
Following: https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu
1. sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git
2. git clone https://github.com/pyenv/pyenv.git ~/.pyenv
3. echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc

### Using pyenv
See all python versions:
yenv install -l
Install a python version:
pyenv install [PYTHON_VERSION]
View installed python versions (* denotes active version:
pyenv versions
Check current actiuve version:
pyenv version
Set a global python version:
pyenv global [PYTHON_VERSION]
Set project python version:
pyenv local [PYTHON_VERSION]

## Create a virtual environment
Following: https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu
1. Open a terminal at the project directory
2. pyenv local [PYTHON_VERSION]
3. python -m venv .venv
4. source .venv/bin/activate

## Install required packages
In your venv:
1. pip3 install --upgrade pip
2. pip3 install tensorflow==1.5.0
3. pip3 install ffmpeg
4. pip3 install feather-format
5. pip3 install keras==2.1.5
6. pip3 install moviepy
7. pip3 install opencv-python==3.2.0.8
8. pip3 install pandas
9. pip3 install tqdm
10. pip3 uninstall scipy
11. pip3 install scipy==1.2.0
To view installed packages:
pip list

# Running the code
In your venv:
1. Download BDD-Attention dataset (https://bdd-data.berkeley.edu/)
2. Place videos in ./data/inference/camera_videos/
3. Run python parse_videos.py \
--video_dir=data/inference/camera_videos \
--image_dir=data/inference/camera_images \
--sample_rate=3 \
--video_suffix=.mp4
4. Run python write_tfrecords_for_inference.py \
--data_dir=data/inference \
--n_divides=2 \
--longest_seq=35
5. Download pre-trained weights (https://drive.google.com/file/d/1q_CgyX73wrYTAsZjDF9aMXNPURcUmWVy/view)
6. Place unzipped directory in ./ (make sure file structure is correct)
7. Download pre-trained Alexnet weights (https://www.cs.toronto.edu/~guerzhoy/tf_alexnet/bvlc_alexnet.npy)
8. Place in ./
9. Add allow_pickle=True to my_alexnet.py
10. Run python infer.py \
--data_dir=data \
--model_dir=pretrained_models/model_for_inference
Results can be found at ./pretrained_models/model_for_inference/prediction_iter_0/
