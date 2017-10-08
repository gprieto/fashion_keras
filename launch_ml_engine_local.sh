export JOB_DIR=.

gcloud ml-engine local train \
  --job-dir $JOB_DIR \
  --module-name trainer.cnn \
  --package-path ./trainer \
  -- \
  --train-file ./data/fashion-mnist_train.csv