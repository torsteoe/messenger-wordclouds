# Messenger clouds

Make a wordcloud from your facebook messages using wordcloud, pillow, numpy, stop\_words, multidict. Instructions below. 
**Please contact me for any questions**

Thanks to [MrGarret45](https://github.com/mrgarrett45/songclouds) for inspiration and for showing how to use the wordcloud library. 


## Getting started

### 1. Fetch your Facebook data

Go to settings on facebook (small triangle in upper right corner) and go to the section: "Your Facebook Information". Press "Download your information" and check only "Messages". Download in JSON format. 

### 2. Install Python 3+

Python 3 can be installed from [https://www.python.org/downloads/](https://www.python.org/downloads/). I currently have Python 3.8.1.


### 3. Go for a long walk.

The download of Facebook data takes time, it took me three hours. 

### 4. Clone this repository

```
git clone https://github.com/torsteoe/messenger-wordclouds.git

```

### 5. Place facebook files in repository directory

Unpack zip-file and choose a chat you want to make a wordcloud out of. Move all files from /messages/inbox/i\[chat\name\] called message\_1.json, message\_2.json etc to the repository directory. In my script I read from 2 json files, this can be reduced or expanded. 

### 6. Install dependencies

Navigate to the repository directory in the terminal. Write either 
```
pip3 install -r requirements.txt
```

or 

```
pip install -r requirements.txt
```

(depending on how you installed Python 3), then press ENTER.

### 7. Run script
In the same terminal write 
```
python3 messenger-wc.py
```


