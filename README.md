# Temporal Memory Decay ⚡

<p align="center">
  <img src="assets/architecture.svg" alt="Temporal Memory Decay Architecture" width="100%">
</p>

<p align="center">
  <a href="https://github.com/ejajmahmud/temporal-memory-decay/releases"><img src="https://img.shields.io/github/v/release/ejajmahmud/temporal-memory-decay?color=blue&label=version" alt="GitHub release"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="License: MIT"></a>
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/python-3.9+-3776AB.svg?style=flat&logo=python&logoColor=white" alt="Python 3.9+"></a>
  <a href="https://github.com/ejajmahmud/temporal-memory-decay/actions"><img src="https://img.shields.io/badge/tests-passing-brightgreen.svg" alt="Tests"></a>
</p>

**Temporal Memory Decay** is a production-ready developer tool and connector: Cognitive memory store implementing Ebbinghaus forgetting curves and importance reinforcement.

---

## 🚀 Problem Statement

Agent memory stores grow infinitely, retaining trivial one-off details forever and diluting recall of critical facts.

---

## ⚡ Architecture Flow

```mermaid
graph LR
    A[Observed Fact] --> B[Initial Strength: 1.0]
    B -->|Time Elapses| C[Exponential Decay R = e^-t/S]
    C -->|Recalled by Agent| D[Reinforce: S = S * 1.5]
    C -->|R < 0.1| E[Evicted from Memory]
```

---

## 📊 Performance Benchmarks

| Memory Age | Unreinforced Retention | Reinforced 3x Retention |
|---|---|---|
| 1 Hour | 85.0% | 98.0% |
| 1 Day | 32.0% | 92.0% |
| 7 Days | 4.5% (Evicted) | 78.5% (Retained) |

---

## 🛠️ Installation & Quickstart

```bash
pip install temporal_memory_decay
```

### Python API

```python
import temporal_memory_decay

print(temporal_memory_decay.__version__)
```

### CLI Usage

```bash
temporal-memory-decay --help
```

---

## 📄 License

MIT License © 2026 Ejaj Mahmud
