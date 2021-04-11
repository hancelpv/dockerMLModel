# dockerMLModel
ML Model run in docker

# Running in local
```buildoutcfg
pip install virtualenv
python -m venv newenv
source newenv/bin/activate

python main.py
```

# Running in docker container

```buildoutcfg
#ensure dockerfile is present in working directory

#create image
docker build -t sampleapp .

#run container
docker run sampleapp

```
