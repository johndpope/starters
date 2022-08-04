# Unweave MNIST Starter

This starter will help you train an MNIST model using Unweave and serverless infra.

This MNIST code is taken from the official [PyTorch examples](https://github.com/pytorch/examples) where you can find more examples to try running with Unweave.

## Run the starter on Unweave

1. If you don't have Unweave CLI installed, you can get it from homebrew

```bash
$ brew install unweave/unweave/unweave
==> Downloading https://github.com/unweave/cli/releases/download/v0.0.19/unweave_0.0.19_darwin_arm64.tar.gz
Already downloaded: /Users/markwinter/Library/Caches/Homebrew/downloads/fb4b2b676e3b8680405f5094e438827fead5210146df54cc96aad0ea026ae1e3--unweave_0.0.19_darwin_arm64.tar.gz
==> Installing unweave from unweave/unweave
🍺  /opt/homebrew/Cellar/unweave/0.0.19: 5 files, 7.4MB, built in 1 second
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

5. Run the training script with the Unweave CLI. This will create a zepl with your data and run it on our infrastructure.

```bash
$ unweave python main.py
Executing command 'python main.py' in serverless zepl. Press Ctrl+C to cancel
Executing...

Created zepl "secret-got-rubbed-clock" with ID "a1bee62f-b4c9-44ac-a880-ec04d178b015"

Starting zepl. Press Ctrl+C while it is running to cancel the run

🔄 Initializing serverless compute node

✅ Compute node assigned to zepl

🔄 Syncing Unweave Store

🔄 Building environment

🚀 Zepl running. Fetching logs ...

Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
Downloading http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz to ../data/MNIST/raw/train-images-idx3-ubyte.gz
100.0%
Extracting ../data/MNIST/raw/train-images-idx3-ubyte.gz to ../data/MNIST/raw
...

Train Epoch: 1 [0/60000 (0%)]	Loss: 2.329474
Train Epoch: 1 [640/60000 (1%)]	Loss: 1.425063
Train Epoch: 1 [1280/60000 (2%)]	Loss: 0.815459
Train Epoch: 1 [1920/60000 (3%)]	Loss: 0.535510
Train Epoch: 1 [2560/60000 (4%)]	Loss: 0.425536
Train Epoch: 1 [3200/60000 (5%)]	Loss: 0.253121
Train Epoch: 1 [3840/60000 (6%)]	Loss: 0.353541
...

🧹 Cleaning up

✅ Zepl complete
```

6. Your MNIST training is complete! You can explore more helpful CLI commands

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