export BUCKET_NAME=mnist-data-1001
export JOB_NAME="cnn_train_$(date +%Y%m%d_%H%M%S)"
export JOB_DIR=gs://$BUCKET_NAME/$JOB_NAME
export REGION=europe-west1

gcloud ml-engine jobs submit training $JOB_NAME \
  --job-dir $JOB_DIR \
  --runtime-version 1.0 \
  --module-name trainer.cnn \
  --package-path ./trainer \
  --region $REGION \
  --config=trainer/cloudml-gpu.yaml \
  -- \
  --train-file gs://$BUCKET_NAME/data/fashion-mnist_train.csv
