# Sagemaker Pipeline with Custom Image Example

This repository contains an example of a Sagemaker Pipeline using a custom docker image stored in ECR. The custom image is built using a Dockerfile, which loads a `requirements.txt` and custom modules that are called in the scripts. Scripts are passed in from the pipeline, which means that the custom image must be flexible so that it can be used by multiple scripts.

## Workflow

1. Run `00a_config.ipynb`. This file establishes the initial configuration file. 
1. Run `00b_files.ipyngb`. This creates the `Dockerfile` and `requirements.txt`.
1. Run `00c_scripts.ipynb`. This creates the modules and scripts that are required for both the docker container and the pipeline.
1. Use `Dockerfile`, `requirements.txt`, and `source_dir` to create a docker container and load it to ECR.
    - This process is separate from the included files and will need to be accomplished per your acount configuration/permission.
    - The pipeline definition assumes that the ECR is in the same account and region.
1. Update `config.yaml` with the image tag generated when the image was loaded to ECR. 
1. Run `02_pipeline.ipynb` to kick off the pipeline.