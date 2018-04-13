#!/usr/bin/env python3

import os
import numpy as np
import cv2
import tensorflow as tf
from fr_utils import *
from inception_blocks_v2 import *
from keras import backend as K
from keras.models import load_model
import pickle
from plyer import notification
