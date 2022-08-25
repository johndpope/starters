# Unweave MNIST Starter

This starter will help you train an MNIST model using Unweave and serverless infra.

This MNIST code is taken from the official [PyTorch examples](https://github.com/pytorch/examples) where you can find more examples to try running with Unweave.

## Run the starter on Unweave

1. If you don't have Unweave CLI installed, you can get it from homebrew

```bash
$ brew install unweave/unweave/unweave
==> Downloading ...
````

2. Use the Unweave CLI to login, following the login flow in your browser.

```bash
$ unweave login
? Do you want to open the browser to login? (Y/n)
```

3. Clone this repository and cd into this MNIST starter directory

```bash
$ git clone https://github.com/unweave/starters.git
$ cd mnist
```

4. Initialise the directory with unweave and call this project `mnist-starter`

```bash
$ unweave init
? Enter project name [mnist]: mnist-starter
Created project mnist-starter
Path:    	/Users/markwinter/Code/starters/mnist
Project: 	mnist-starter
```

5. Downloda the MNIST training data set using the provided script. This will download to the `./uwstore/data/MNIST` directory.

```bash
$ python download.py
```

6. Upload the MNIST data to the uwstore. This data will now always be available for each of your training scripts at the path `./uwstore/data`. If you inspect
the `main.py` script you will see that we load the MNIST dataset from that local path without downloading the data again.

```bash
$ unweave store upload uwstore/data/MNIST
Uploading file MNIST/raw/t10k-images-idx3-ubyte Uploaded!
Uploading file MNIST/raw/t10k-images-idx3-ubyte.gz Uploaded!
Uploading file MNIST/raw/t10k-labels-idx1-ubyte Uploaded!
Uploading file MNIST/raw/t10k-labels-idx1-ubyte.gz Uploaded!
Uploading file MNIST/raw/train-images-idx3-ubyte Uploaded!
Uploading file MNIST/raw/train-images-idx3-ubyte.gz Uploaded!
Uploading file MNIST/raw/train-labels-idx1-ubyte Uploaded!
Uploading file MNIST/raw/train-labels-idx1-ubyte.gz Uploaded!
```

7. Run the training script with the Unweave CLI. This will create a serverless compute node (`zepl`) with your data and run it.

```bash
$ unweave python main.py
Executing command 'python main.py' in serverless zepl. Press Ctrl+C to cancel
Executing...

Created zepl "donkey-lie-poet-other" with ID "a5825ccc-9c83-4bb8-84a0-f16801ffaba1"

Starting zepl
Press Ctrl+C to cancel the zepl
Press Ctrl+D to detach

🔄 Initializing serverless compute node
✅ Compute node assigned to zepl
🔄 Syncing Unweave Store
🔄 Building environment
🚀 Zepl running. Fetching logs ...
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ./uwstore/data/MNIST/raw/train-images-idx3-ubyte.gz
100.0%
Extracting ./uwstore/data/MNIST/raw/train-images-idx3-ubyte.gz to ./uwstore/data/MNIST/raw

...

Train Epoch: 1 [0/60000 (0%)]	Loss: 2.305400
Train Epoch: 1 [640/60000 (1%)]	Loss: 1.359780
Train Epoch: 1 [1280/60000 (2%)]	Loss: 0.830670
Train Epoch: 1 [1920/60000 (3%)]	Loss: 0.605963
...
Train Epoch: 1 [58240/60000 (97%)]	Loss: 0.020182
Train Epoch: 1 [58880/60000 (98%)]	Loss: 0.017681
Train Epoch: 1 [59520/60000 (99%)]	Loss: 0.002070
🧹 Cleaning up
✅ Zepl complete
```

8. Your MNIST training is complete! You can now fetch the model that was saved in remote storage. In the future you'll be able to use the output of one zepl in another zepl.

```bash
$ unweave store list 
2022-08-25 10:34:46 +0900 KST	7.8 MB	data/MNIST/raw/t10k-images-idx3-ubyte
2022-08-25 10:34:47 +0900 KST	1.6 MB	data/MNIST/raw/t10k-images-idx3-ubyte.gz
2022-08-25 10:34:48 +0900 KST	10 kB	data/MNIST/raw/t10k-labels-idx1-ubyte
2022-08-25 10:34:48 +0900 KST	4.5 kB	data/MNIST/raw/t10k-labels-idx1-ubyte.gz
2022-08-25 10:34:50 +0900 KST	47 MB	data/MNIST/raw/train-images-idx3-ubyte
2022-08-25 10:35:09 +0900 KST	9.9 MB	data/MNIST/raw/train-images-idx3-ubyte.gz
2022-08-25 10:35:10 +0900 KST	60 kB	data/MNIST/raw/train-labels-idx1-ubyte
2022-08-25 10:35:10 +0900 KST	29 kB	data/MNIST/raw/train-labels-idx1-ubyte.gz
...
2022-08-16 09:49:54 +0900 KST	4.8 MB	output/000f422b-a293-4f9f-be22-ce1f66d00533/mnist_cnn.pt

$ unweave store download output/000f422b-a293-4f9f-be22-ce1f66d00533/mnist_cnn.pt 
Saved to local file "./uwstore/output/000f422b-a293-4f9f-be22-ce1f66d00533/mnist_cnn.pt"
```

10. Explore other unweave cli commands

```bash
# Open the Unweave dashboard in your browser
$ unweave open
```

```bash
# Check the logs of a zepl
$ unweave logs <zepl-id>
```

```bash
# Check all your zepls
$ unweave zepls
```

```bash
# Run a zepl but immediately detach once it has successfully launched
$ unweave -d python main.py
```
