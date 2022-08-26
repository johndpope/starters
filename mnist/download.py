import os
import gzip
import shutil
import urllib.request

base = "http://yann.lecun.com/exdb/mnist/"

out_dir = "uwstore/data/MNIST/raw/"
download_dir = "tmp/"

files = [
    "train-images-idx3-ubyte.gz",
    "train-labels-idx1-ubyte.gz", 
    "t10k-images-idx3-ubyte.gz",
    "t10k-labels-idx1-ubyte.gz",
]


if not os.path.exists(download_dir):
    os.makedirs(download_dir)

if not os.path.exists(out_dir):
    os.makedirs(out_dir)


def main():
    for f in files:
        url = base + f
        download_path = download_dir + f
        out_path = out_dir + f[:-3]
        
        print("Downloading file: ", f)
        with urllib.request.urlopen(url) as response, open(download_path, 'wb') as out_file:
            shutil.copyfileobj(response, out_file)

        with gzip.open(download_path, 'rb') as f_in:
            with open(out_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

    print("Finished downloading %d files" % len(files))
    shutil.rmtree(download_dir)


if __name__ == '__main__':
    main()
