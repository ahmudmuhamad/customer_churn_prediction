src/
└── churn/
    ├── __init__.py
    ├── config.py
    ├── data.py                 # data loading / paths helpers
    ├── features.py             # feature engineering functions
    ├── modeling/
    │   ├── __init__.py
    │   ├── train.py            # training flow (re-usable)
    │   └── predict.py          # inference wrapper (model + pipeline)
    ├── api/
    │   ├── __init__.py
    │   └── app.py              # importable FastAPI app (uvicorn runs this)
    └── utils.py                # small helpers (logging, validation)
tests/
└── test_predict.py
