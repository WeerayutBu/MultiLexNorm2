# MultiLexNorm2: Multilingual Lexical Normalization

In our MultiLexNorm2 task, we emphasize non-Indo-European languages, such as Thai, Vietnamese, and Indonesian. Participants are asked to develop a system that performs lexical normalization: the conversion of non-canonical texts to their canonical equivalent form. In particular, this task includes data from 15 languages.

More details about the task can be found [here](https://noisy-text.github.io/2025/multi-lexnorm.html#).

## Baselines
We provide two simple baseline methods for lexical normalization:

- Leave-As-Is (LAI): Simply uses the input as output. Word level accuracy would be equal to the % of words that are not normalized, and ERR is 0.0.
- Most-frequent-Replacement (MFR): Uses the most frequent replacement based on the training data. If the input word is not present in the training data, it returns the input word.

## Directory Structure
```
.
├── data/
│   ├── train/
│   │   ├── new_languages/
│   │   │   ├── vi/train.norm
│   │   │   ├── th/train.norm
│   │   │   └── ...
│   │   └── original_languages/...
│   ├── dev_masked/
│   │   ├── new_languages/
│   │   │   ├── vi/dev.norm.masked
│   │   │   ├── th/dev.norm.masked
│   │   │   └── ...
│   │   └── original_languages/...
│   └── test_masked/...
├── output/...
├── scripts/
│   ├── baseline.py
│   └── normEval.py
├── run.py
└── README.md
```


## Usage
### Run a Baseline
To evaluate a baseline model with the *mfr* method:
```python
python scripts/baseline.py \
    --method mfr \
    --train data/train/new_languages/vi/train.norm \
    --dev data/dev_masked/new_languages/vi/dev.norm.masked \
    --out dev.norm.pred > out.score
```

### Full Pipeline Execution
To execute the full pipeline using a given script and paths:
```python
python run.py \
    --method mfr \
    --path_script scripts/baseline.py \
    --train data/train \
    --pred data/test_masked \
    --out output/test_masked
```