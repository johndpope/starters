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

5. Upload the sample images to the uwstore so they're available to your zepls without uploading it every time your start a zepl. We can then delete the images after they're in the uwstore

```bash
❯ unweave store upload img
❯ rm -rf img
```

6. Run the main python script with the Unweave CLI. This will create a serverless compute node (`zepl`) with your data and run it. **This requires access to GPUs. If you need access please contact us**

```bash
❯ unweave --gpu python main.py -- --base configs/latent-diffusion/txt2img-1p4B-finetune.yaml -t --actual_resume ./uwstore/data/textual/model.ckpt -n test --gpus 0, --data_root ./uwstore/data/textual --init_word sculpture --no-test --logdir ./uwstore/output
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
Epoch 46:   1%|▏         | 1/76 [00:00<00:47,  1.58it/s, loss=0.202, v_num=0, train/loss_simple_step=0.167, train/loss_vlb_step=0.000563, train/loss_step=0.167, global_step=3449.0, train/Epoch 46:   1%|▏         | 1/76 [00:00<00:47,  1.58it/s, loss=0.21, v_num=0, train/loss_simple_step=0.257, train/loss_vlb_step=0.0568, train/loss_step=0.257, global_step=3450.0, train/losEpoch 46:   3%|▎         | 2/76 [00:00<00:35,  2.08it/s, loss=0.21, v_num=0, train/loss_simple_step=0.257, train/loss_vlb_step=0.0568, train/loss_step=0.257, global_step=3450.0, train/losEpoch 46:   3%|▎         | 2/76 [00:00<00:35,  2.08it/s, loss=0.201, v_num=0, train/loss_simple_step=0.115, train/loss_vlb_step=0.00043, train/loss_step=0.115, global_step=3451.0, train/lEpoch 46:   4%|▍         | 3/76 [00:01<00:31,  2.33it/s, loss=0.201, v_num=0, train/loss_simple_step=0.115, train/loss_vlb_step=0.00043, train/loss_step=0.115, global_step=3451.0, train/lEpoch 46:   4%|▍         | 3/76 [00:01<00:31,  2.33it/s, loss=0.196, v_num=0, train/loss_simple_step=0.120, train/loss_vlb_step=0.000615, train/loss_step=0.120, global_step=3452.0, train/Epoch 46:   5%|▌         | 4/76 [00:01<00:29,  2.47it/s, loss=0.196, v_num=0, train/loss_simple_step=0.120, train/loss_vlb_step=0.000615, train/loss_step=0.120, global_step=3452.0, train/Epoch 46:   5%|▌         | 4/76 [00:01<00:29,  2.47it/s, loss=0.186, v_num=0, train/loss_simple_step=0.163, train/loss_vlb_step=0.000609, train/loss_step=0.163, global_step=3453.0, train/Epoch 46:   7%|▋         | 5/76 [00:01<00:27,  2.56it/s, loss=0.186, v_num=0, train/loss_simple_step=0.163, train/loss_vlb_step=0.000609, train/loss_step=0.163, global_step=3453.0, train/Epoch 46:   7%|▋         | 5/76 [00:01<00:27,  2.56it/s, loss=0.198, v_num=0, train/loss_simple_step=0.359, train/loss_vlb_step=0.00504, train/loss_step=0.359, global_step=3454.0, train/lEpoch 46:   8%|▊         | 6/76 [00:02<00:26,  2.63it/s, loss=0.198, v_num=0, train/loss_simple_step=0.359, train/loss_vlb_step=0.00504, train/loss_step=0.359, global_step=3454.0, train/lEpoch 46:   8%|▊         | 6/76 [00:02<00:26,  2.62it/s, loss=0.199, v_num=0, train/loss_simple_step=0.282, train/loss_vlb_step=0.00227, train/loss_step=0.282, global_step=3455.0, train/lEpoch 46:   9%|▉         | 7/76 [00:02<00:25,  2.68it/s, loss=0.199, v_num=0, train/loss_simple_step=0.282, train/loss_vlb_step=0.00227, train/loss_step=0.282, global_step=3455.0, train/lEpoch 46:   9%|▉         | 7/76 [00:02<00:25,  2.68it/s, loss=0.208, v_num=0, train/loss_simple_step=0.348, train/loss_vlb_step=0.00496, train/loss_step=0.348, global_step=3456.0, train/lEpoch 46:  11%|█         | 8/76 [00:02<00:25,  2.72it/s, loss=0.208, v_num=0, train/loss_simple_step=0.348, train/loss_vlb_step=0.00496, train/loss_step=0.348, global_step=3456.0, train/lEpoch 46:  11%|█         | 8/76 [00:02<00:25,  2.72it/s, loss=0.208, v_num=0, train/loss_simple_step=0.174, train/loss_vlb_step=0.000594, train/loss_step=0.174, global_step=3457.0, train/Epoch 46:  12%|█▏        | 9/76 [00:03<00:24,  2.75it/s, loss=0.208, v_num=0, train/loss_simple_step=0.174, train/loss_vlb_step=0.000594, train/loss_step=0.174, global_step=3457.0, train/Epoch 46:  12%|█▏        | 9/76 [00:03<00:24,  2.75it/s, loss=0.201, v_num=0, train/loss_simple_step=0.0818, train/loss_vlb_step=0.000285, train/loss_step=0.0818, global_step=3458.0, traiEpoch 46:  13%|█▎        | 10/76 [00:03<00:23,  2.77it/s, loss=0.201, v_num=0, train/loss_simple_step=0.0818, train/loss_vlb_step=0.000285, train/loss_step=0.0818, global_step=3458.0, traEpoch 46:  13%|█▎        | 10/76 [00:03<00:23,  2.77it/s, loss=0.218, v_num=0, train/loss_simple_step=0.475, train/loss_vlb_step=0.00408, train/loss_step=0.475, global_step=3459.0, train/Epoch 46:  14%|█▍        | 11/76 [00:03<00:23,  2.79it/s, loss=0.218, v_num=0, train/loss_simple_step=0.475, train/loss_vlb_step=0.00408, train/loss_step=0.475, global_step=3459.0, train/Epoch 46:  14%|█▍        | 11/76 [00:03<00:23,  2.79it/s, loss=0.218, v_num=0, train/loss_simple_step=0.213, train/loss_vlb_step=0.000999, train/loss_step=0.213, global_step=3460.0, train
..
🧹 Cleaning up
✅ Zepl complete
```

