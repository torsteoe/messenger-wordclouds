## Messenger clouds

Make a wordcloud from your facebook messages using wordcloud, pillow, numpy, stop\_words, multidict.

Thanks to [MrGarret45](https://github.com/mrgarrett45/songclouds) for inspiration and for showing how to use the wordcloud library. 


### Getting started

#### 1. Install Python 3+

Python 3 can be installed from [https://www.python.org/downloads/](https://www.python.org/downloads/). I currently have Python 3.8.1.

#### 2. Fetch your Facebook data

Go to settings on facebook (small triangle in upper right corner) and go to the section: "Your Facebook Information". Press "Download your information" and check only "Messages". Download in JSON format. 

#### 3. Go for a long walk

The download takes time, for me three hours. 

#### 4. Clone this repository

```
git clone https://github.com/torsteoe/messenger-wordclouds.git

```

#### 5. Install dependencies

Navigate to the directory containing "messenger-wc.py".  In your terminal, write either 
```
pip3 install -r requirements.txt
```

or 

```
pip install -r requirements.txt
```

(depending on how you installed Python 3), then press ENTER.

#### 6. Run script
In the same terminal write 
```
python3 messenger-wc.py
```


