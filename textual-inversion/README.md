# Unweave Textual Inversion Starter

This starter will help you to run [Textual Inversion](https://github.com/rinongal/textual_inversion) on Unweave.

## Run the starter on Unweave

1. If you don't have the Unweave CLI installed, you can get it from homebrew:

```bash
brew install unweave/unweave/unweave
````

2. Use the CLI to login, following the login flow in your browser.

```bash
❯ unweave login
? Do you want to open the browser to login? (Y/n)
```

3. Clone this repository and cd into this Time Sequence Prediction starter directory

```bash
git clone https://github.com/unweave/starters.git
cd textual-inversion 
```

4. Initialise the directory with unweave and hit enter to name the project after the current directory name.

```bash
❯ unweave init
? Enter project name [textual-inversion]:
Created project textual-inversion
Path:    	/Users/markwinter/Code/starters/textual-inversion
Project: 	textual-inversion
```

5. Download an image set from the authors found [here](https://drive.google.com/drive/folders/1d2UXkX0GWM-4qUwThjNhFIPP7S6WUbQJ). You should then upload the images to your uwstore so they are available to your zepls without uploading them every time you start a zepl.

```bash
# Download an image set from the google drive link and unzip it to a directory.
# If you used the thin_bird dataset and unzipped it, you woud upload it like below
❯ unweave store upload ~/Downloads/thin_bird
```

6. Run the main python script with the Unweave CLI. This will create a serverless compute node (`zepl`) with your data and run it. **This requires access to GPU zepls. If you need access please contact us.**

```bash
❯ unweave --gpu python main.py -- --base configs/latent-diffusion/txt2img-1p4B-finetune.yaml -t --actual_resume ./uwstore/data/model.ckpt -n test --gpus 0, --data_root ./uwstore/data/thin_bird --init_word sculpture --no-test --logdir ./uwstore/output
Created zepl "wooden-dish-most-sea" with ID "52bf79f0-643d-4d6c-b4e6-6ecbef3c9315"

Starting zepl
Press Ctrl+C to cancel the zepl
Press Ctrl+D to detach

🔄 Initializing serverless compute node
✅ Compute node assigned to zepl
🔄 Syncing Unweave Store
🔄 Building environment
🚀 Zepl running. Fetching logs ...
Global seed set to 23
Running on GPUs 0,
Loading model from ./uwstore/data/textual/model.ckpt
LatentDiffusion: Running in eps-prediction mode
DiffusionWrapper has 872.30 M params.
making attention of type 'vanilla' with 512 in_channels
Working with z of shape (1, 4, 32, 32) = 4096 dimensions.
making attention of type 'vanilla' with 512 in_channels
..
Epoch 81:   1%|▏         | 1/76 [00:00<00:45,  1.65it/s, loss=0.173, v_num=0, train/loss_simple_step=0.175, train/loss_vlb_step=0.000764, train/loss_step=0.175, global_step=6074.0, train/
Epoch 81:   9%|▉         | 7/76 [00:02<00:25,  2.72it/s, loss=0.17, v_num=0, train/loss_simple_step=0.201, train/loss_vlb_step=0.000685, train/loss_step=0.201, global_step=6080.0, train/l
Epoch 81:  20%|█▉        | 15/76 [00:05<00:21,  2.88it/s, loss=0.167, v_num=0, train/loss_simple_step=0.104, train/loss_vlb_step=0.000359, train/loss_step=0.104, global_step=6089.0, train
Epoch 81:  34%|███▍      | 26/76 [00:08<00:16,  3.05it/s, loss=0.17, v_num=0, train/loss_simple_step=0.205, train/loss_vlb_step=0.00104, train/loss_step=0.205, global_step=6099.0, train/l
..
🧹 Cleaning up
✅ Zepl complete
```

