gcloud ml-engine local train \
  --job-dir $JOB_DIR \
  --module-name trainer.cnn \
  --package-path ./trainer \
  -- \
  --train-dir ./data/fashion
