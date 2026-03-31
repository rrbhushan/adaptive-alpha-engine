# Adaptive Alpha Engine
## Walk-forward ML research & backtesting framework for short-horizon crypto signals

## Overview
Adaptive Alpha Engine is a modular research framework for evaluating short-horizon trading signals under realistic execution constraints.
Version 1 focuses on:
- BTCUSDT (Kraken), 1-minute bars
- 5-minute directional prediction
- Walk-forward retraining (time-ordered splits)
- Transaction costs + slippage simulation
- Model benchmarking (Logistic Regression, XGBoost, LightGBM)
The objective is not just predictive accuracy, but evaluating whether signals remain robust net of costs and stable across rolling out-of-sample windows.

---

## Key Features
Leakage-safe time-series validation
Walk-forward retraining framework
Modular model interface for fair comparison
Realistic cost & slippage modeling
Reproducible experiment configs

---

## Status
🚧 Initial development — baseline pipeline under construction.
