# Multilayer Perceptron Model
An deep neural network (MLP) for toxicity labeling. The pre-trained ```save/model.h5``` can be downloaded [here](https://drive.google.com/file/d/1FMkhv5xE29D5c6UPLBkxvFfVqZkmxzZr/view?usp=sharing).

### Usage
To train a new model, simply run the following. A pre-trained model checkpoint is included with this repository.

```
python train.py
```

To try the model out, run:
```
python evaluate.py -c "You're dumb"
```
To generate a ```submission.csv``` prediction file based on the [Kaggle](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge) ```test.csv``` data, simply run:
```
python evaluate.py
```

### Model
Below is the network architecture used for classification. It was trained on [data from Google](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge/data) available on Kaggle. **Achieves approximately 95% test accuracy** on both validation data and the public Kaggle leaderboard test data.

<p align="center">
<img width="300" src="save/model.png"/>
</p>


### License
The MIT License (MIT)

Copyright (c) 2018 Gautam Mittal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
