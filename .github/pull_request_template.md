## Summary

- [ ] Implemented and tested the required notebook tasks
- [ ] Completed the chosen adversarial-attack track and bonus experiments
- [ ] Preserved the original notebook cell metadata and outputs

## Experiments and environment

- Full run: `FAST_MODE=False`
- GPU: NVIDIA Tesla T4
- CIFAR-10: 50,000 train / 10,000 test
- FashionMNIST: 60,000 train / 1,000 test evaluated
- Attack track: `targeted`
- Selected bonuses: `7.1`, `7.2`, `7.4`, `7.5`

## Key observations

- ResNet-20 CIFAR-10 test accuracy: **83.05%**.
- PGD-20 accuracy at ε=0.1: **0.60% standard → 70.40% PGD-AT**.
- FGSM vs FGSM-RS show contrasting robustness trajectories in the bonus case study.

## Review checklist

- [ ] All notebook cells execute and their outputs are saved
- [ ] Checkpoint and `metrics.json` files are present in `artifacts/`
- [ ] Notebook answers describe the actual results
- [ ] No private tokens or local data dumps are included

**Feedback / verdict:** Please leave the evaluation and comments in this pull request, as requested in the assignment.
