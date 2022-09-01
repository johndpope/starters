# Unweave Time Sequence Prediction Starter

This starter will help you train an Time Sequence Prediction model using Unweave and serverless infra.

This Time Sequence Prediction code is taken from the official [PyTorch examples](https://github.com/pytorch/examples) where you can find more examples to try running with Unweave.

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

3. Clone this repository and cd into this Time Sequence Prediction starter directory

```bash
$ git clone https://github.com/unweave/starters.git
$ cd time_sequence_prediction 
```

4. Initialise the directory with unweave and hit enter to name the project after the current directory name

```bash
$ unweave init
? Enter project name [time_sequence_prediction]:
Created project time_sequence_prediction
Path:    	/Users/markwinter/Code/starters/time_sequence_prediction
Project: 	time_sequence_prediction
```

5. Run the training script with the Unweave CLI. This will create a serverless compute node (`zepl`) with your data and run it.

```bash
$ unweave python train.py
Created zepl "wooden-dish-most-sea" with ID "52bf79f0-643d-4d6c-b4e6-6ecbef3c9315"

Starting zepl
Press Ctrl+C to cancel the zepl
Press Ctrl+D to detach

🔄 Initializing serverless compute node
✅ Compute node assigned to zepl
🔄 Syncing Unweave Store
🔄 Building environment
🚀 Zepl running. Fetching logs ...
STEP:  0
loss: 0.5023738120466186
loss: 0.4985663932454724
loss: 0.479011960201462
loss: 0.44633490395179287
loss: 0.3540631027261268
loss: 0.20507018018165285
..
🧹 Cleaning up
✅ Zepl complete
```

8. Your Time Sequence Prediction training is complete! You can now view and download all the PDFs that were generated with the prediction plots.

```bash
$ unweave store list 
2022-09-01 20:06:03 +0900 KST	25 kB	output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict0.pdf
2022-09-01 20:06:03 +0900 KST	40 kB	output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict1.pdf
2022-09-01 20:06:03 +0900 KST	28 kB	output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict2.pdf
2022-09-01 20:06:03 +0900 KST	40 kB	output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict3.pdf
2022-09-01 20:06:03 +0900 KST	38 kB	output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict4.pdf

$ unweave store download output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315
predict0.pdf saved to ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict0.pdf
predict1.pdf saved to ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict1.pdf
predict2.pdf saved to ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict2.pdf
predict3.pdf saved to ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict3.pdf
predict4.pdf saved to ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict4.pdf

$ open ./uwstore/output/52bf79f0-643d-4d6c-b4e6-6ecbef3c9315/predict0.pdf
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
$ unweave -d python train.py
```
