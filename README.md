# MultiLexNorm2

### Methods
- mfr
- lai

### Run a baseline
```python
python scripts/baseline.py \
    --method mfr \
    --train data/train/new_languages/vi/train.norm \
    --dev data/dev_masked/new_languages/vi/dev.norm.masked \
    --out dev.norm.pred > out.score
```

### Run a baseline
```python
python run.py --method mfr --path_script scripts/baseline.py --train data/train --pred data/test_masked --out output/test_masked
python run.py --method mfr --path_script scripts/baseline.py --train data/train --pred data/dev_masked  --out output/dev_masked
python run.py --method lai --path_script scripts/baseline.py --train data/train --pred data/test_masked --out output/test_masked
python run.py --method lai --path_script scripts/baseline.py --train data/train --pred data/dev_masked  --out output/dev_masked
```