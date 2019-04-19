## What is it about?

Sixth place solution to kaggle bengali handwritten digit recognition. Achieved 97.606%. A VGG16 architecture pre-trained on imagenet used as a baseline with hyperparameter tuning, fine tuning intermediate layers, data augmentation and test time augmentation.

The unconventional approach led to surprising results which caught Jeremy Howard's attention which he ended up [tweeting about](https://twitter.com/jeremyphoward/status/1050427625011703808)! 

## Usage 

This architecture is implemented in Python 3.6 and Keras using Tensorflow as backend.

## Data set  
* [Numta DB](https://www.kaggle.com/c/numta/data)

## Cite

If you find this work useful in your research, please consider citing:
```
@inproceedings{zunair2018unconventional,
  title={Unconventional Wisdom: A New Transfer Learning Approach Applied to Bengali Numeral Classification},
  author={Zunair, Hasib and Mohammed, Nabeel and Momen, Sifat},
  booktitle={2018 International Conference on Bangla Speech and Language Processing (ICBSLP)},
  pages={1--6},
  year={2018},
  organization={IEEE}
}
```
You can also find it in IEEE Xplore Digital Library [here](https://ieeexplore.ieee.org/document/8554435)
