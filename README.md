# Fashion MNIST classification on Google Cloud ML
Fashion MNIST classification using a CNN in Keras running on Google Cloud ML.

## Description
This project is based on the [Fashion_Keras](https://github.com/Matt3164/Fashion_Keras) repository of Matt3164. 
It basically adapts the code to run on Google Cloud ML.

## How to use it
### Step 0
To begin with you will need to setup a [Google Cloud Platform](https://cloud.google.com/) project and enable billing.

### Step 1
Then from the GC console, we first clone the repository:
```
git clone https://github.com/gprieto/fashion_keras.git
```

There are several `launch_ml_engine*.sh` scripts you can choose from:
1. `launch_ml_engine_local.sh` - to run the project locally on the GC local VM machine
2. `launch_ml_engine.sh` - to run the project on a CPU on the cloud
3. `launch_ml_engine_gpu.sh` - to run the project on a GPU on the cloud

If you choose to run the project on the cloud (scripts 2 and 3) follow Step 2. If you choose to run it locally, you can skip to Step 3.

### Step 2
In order to be able to run the project on the cloud (scripts 2 and 3), you will need to upload your data to a Google Storage 
bucket before launching the selected script. To do so, place the data folder at the root of your bucket.


Also, it is necessary to modify the first line to specify the bucket name for the project.
```
export BUCKET_NAME=*your bucket name here*
...
```


### Step 3

We can now, from the `fashion_keras` folder, launch one of the `launch_ml_engine*.sh` scripts.
```
cd fashion_keras
./launch launch_ml_engine.sh
```

You can follow the progress of the job in the logging interface of GC.
