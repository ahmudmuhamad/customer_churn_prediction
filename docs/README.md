docs/
│
├── models/                       # All saved models
│   ├── final_clf.joblib
│   ├── final_xgb.joblib
│   ├── final_xgb_optuna.joblib
│   ├── final_logistic_regression.joblib
│   ├── final_random_forest.joblib
│   ├── calibrated_clf.joblib
│   ├── calibrated_xgb_optuna.joblib
│   └── cat_maps.joblib
│
├── optuna/                       # Optuna study results
│   ├── optuna_study.pkl
│   ├── optuna_best_params.json
│   ├── optuna_trials.csv
│   ├── optuna_oof_predictions.csv
│   ├── optuna_test_predictions.csv
│   └── optuna_chosen_threshold.txt
│
├── evaluation/                   # Model evaluation metrics
│   ├── confusion_matrix_uncalibrated_test.csv
│   ├── confusion_matrix_calibrated_test.csv
│   ├── confusion_matrix_optuna_test.csv
│   ├── fold_metrics.csv
│   ├── decile_stats.csv
│   ├── threshold_sweep_table.csv
│   ├── error_type_numeric_summary.csv
│   └── run_info.json
│
├── predictions/                  # Predictions from models
│   ├── oof_predictions.csv
│   ├── test_predictions.csv
│   └── confidence_bin_accuracy.csv
│
├── errors/                       # Error analysis
│   ├── test_errors_table.csv
│   ├── top_false_negatives.csv
│   ├── top_false_positives.csv
│   ├── cat_error_rate_last_level.csv
│   └── cat_error_rate_last_location.csv
│
└── notes/                        # Documentation / notes
    └── shap_note.txt
