# Experiment results

All numbers below refer to the recorded final run (`FAST_MODE=False`); the machine-readable experiment configuration and mandatory results are in [`../artifacts/metrics.json`](../artifacts/metrics.json).

## CIFAR-10 — ResNet and plain-network ablation

| Model | Epochs | Train accuracy | Test accuracy | Final train loss |
|---|---:|---:|---:|---:|
| ResNet-20 | 20 | 99.98% | 83.05% | 0.0105 |
| Plain-20 | 10 | 86.01% | 78.62% | 0.4419 |
| Plain-56 | 10 | 57.62% | 54.83% | 1.1619 |

ResNet-20's train/test gap is **16.93 p.p.** Under the same budget, the deeper *plain* network performed worse on train and test, consistent with an optimization/degradation problem in this experiment.

## FashionMNIST — adversarial robustness

| PGD-20 L∞ budget | Standard accuracy | PGD-7 adversarially trained accuracy |
|---:|---:|---:|
| ε=0.00 | 91.70% | 82.90% |
| ε=0.05 | 12.20% | 77.70% |
| ε=0.10 | 0.60% | 70.40% |
| ε=0.15 | 0.00% | 51.50% |
| ε=0.20 | 0.00% | 16.00% |
| ε=0.30 | 0.00% | 0.10% |

Clean accuracy trade-off: **−8.80 p.p.**. Empirical PGD-20 gain at ε=0.10: **+69.80 p.p.**

Strong-attack sanity evaluation is measured separately (256-image evaluation subset): Standard FGSM/PGD-20/PGD-100×5 = 7.42%/1.17%/0.78%; PGD-AT = 75.78%/71.88%/71.48%. These should not be mixed with the 1,000-image ε-sweep.

## Other observations

- **PGD-L2 vs PGD-L∞:** the closest ε₂ grid point (1.5) yielded 1.10% vs 0.60% L∞ accuracy, difference 0.50 p.p. Matching accuracy is not a matching norm budget.
- **Targeted PGD:** direction matters; Pullover → Sneaker had 18.02% target hit rate, while several ankle-boot target pairs reached 100%. Reported rates depend on sample selection.
- **Saliency background share:** 59.25% standard vs 21.36% PGD-AT, reported on 1,000 images. This correlates with, but does not prove, robustness.
- **Sharpness:** final estimates of approx. 9.99 / 38.44 / 21.34 for step sizes 0.01 / 0.05 / 0.10, against local quadratic thresholds 200 / 40 / 20.
- **L0 attacks:** at k=10 modified pixels, standard and PGD-AT accuracies were 38.40% and 59.80%; at k=30, 3.20% and 29.40%. L∞ training does not mathematically guarantee L0 robustness.
- **Catastrophic overfitting:** the FGSM-trained model's PGD-20 accuracy collapsed to ~0% by epoch 3; FGSM-RS did not collapse over five epochs. PGD-100×5 reached 0% vs 38.28% on the selected sanity subset.

**A note on certainty:** single seed, finite training budget, finite attack steps and random restarts — these are experiment results, not global statements or security guarantees.
