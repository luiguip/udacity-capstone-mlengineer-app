# Dog Breed Detector App

## 1. Installation pre requisites

Github has a limit of size and the model.pt is bigger than the limit, so the models have to be downloaded.
You can download for yourself at https://drive.google.com/open?id=1ovY9s3_yTVgWQPPSZVq_VFOfjkevJmYE
or can run the script download-model.

## 2. Installation

```console

foo@bar:~$ git clone https://github.com/luiguip/udacity-capstone-mlengineer-app.git
foo@bar:~$ cd dog_breeds_app
foo@bar:~$ python -m venv .env
foo@bar:~$ source .env/bin/activate
foo@bar:~$ pip install .

```

## 3. Usage

```console

foo@bar:~$ dog-breeds-app --help
usage: dog-breeds-app [-h] [--model MODEL] [--labels LABELS] image

Bog Breed detector.

positional arguments:
  image            Path of the image to be labeled. Dog or human image only.

optional arguments:
  -h, --help       show this help message and exit
  --model MODEL    Model path. For the default path leave it empty.
  --labels LABELS  Labels path. For the default path leave it empty.

```