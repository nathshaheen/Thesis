# Environment Setup (Ubuntu Linux):
## Install pyenv
Following: [How to Install Multiple Python Versions on your Computer and use them with VSCode](https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu):
1. Install initial packages:
```
sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
git
```
2. Clone pyenv into home:
```
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
```
4. Add pyenv to $PATH:
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
```
### Using pyenv
See all python versions: `yenv install -l`

Install a python version: `pyenv install [PYTHON_VERSION]`

View installed python versions (* denotes active version): `pyenv versions`

Check current actiuve version: `pyenv version`

Set a global python version: `pyenv global [PYTHON_VERSION]`

Set project python version: `pyenv local [PYTHON_VERSION]`

## Create a virtual environment
Following: [How to Install Multiple Python Versions on your Computer and use them with VSCode](https://k0nze.dev/posts/install-pyenv-venv-vscode/#linux-debianubuntu):
1. Open a terminal at the project directory
2. Set the local python version:
```
pyenv local [PYTHON_VERSION]
```
4. Create a virtual environment:
```
python -m venv .venv
```
6. Activate it your virtual environment:
```
source .venv/bin/activate
```
## Install the required packages
After activating your virtual environment:
```
pip3 install --upgrade pip
pip3 install tensorflow==1.5.0
pip3 install ffmpeg
pip3 install feather-format
pip3 install keras==2.1.5
pip3 install moviepy
pip3 install opencv-python==3.2.0.8
pip3 install pandas
pip3 install tqdm
pip3 uninstall scipy
pip3 install scipy==1.2.0
```
To view installed packages: `pip list`
# Running the code
After activating your virtual environment:
1. Download BDD-Attention dataset [Berkelery DeepDrive](https://bdd-data.berkeley.edu/)
4. Place videos in `./data/inference/camera_videos/`
5. Run:
```
python parse_videos.py \
--video_dir=data/inference/camera_videos \
--image_dir=data/inference/camera_images \
--sample_rate=3 \
--video_suffix=.mp4
```
4. Run:
```
python write_tfrecords_for_inference.py \
--data_dir=data/inference \
--n_divides=2 \
--longest_seq=35
```
5. Download pre-trained weights [Pretrained Models](https://drive.google.com/file/d/1q_CgyX73wrYTAsZjDF9aMXNPURcUmWVy/view)
6. Place unzipped directory in `./` (make sure file structure is correct)
7. Download pre-trained Alexnet weights [Pretrained Alexnet](https://www.cs.toronto.edu/~guerzhoy/tf_alexnet/bvlc_alexnet.npy)
8. Place in `./`
9. Replace line 7 in `my_alexnet.py` with `net_data = np.load(open("bvlc_alexnet.npy", "rb"), encoding="latin1", allow_pickle=True).item()` to 
10. Run:
```
python infer.py \
--data_dir=data \
--model_dir=pretrained_models/model_for_inference
Results can be found at ./pretrained_models/model_for_inference/prediction_iter_0/
```
