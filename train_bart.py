from datasets import *
from transformers import *
from tokenizers import *
import os
import json
# download and prepare cc_news dataset
dataset = load_dataset("cc_news", split="train")
