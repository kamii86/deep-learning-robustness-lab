# Methodology

## Data and model family

- **CIFAR-10:** 50,000 train and 10,000 test images, 32×32 RGB. Channel-wise mean/std computed from training images. 20 epochs for ResNet-20; 10 epochs for plain ablations.
- **FashionMNIST:** 60,000 training images and 1,000 test images used in the final experiment. Images are scaled to [0,1]; CNN classifiers are trained for five epochs.
- **Hardware:** Tesla T4 GPU. `FAST_MODE=False`, `ATTACK_TRACK='targeted'`.

## Core implementations

The notebook includes explicit convolution forward/backward, BatchNorm and fusion, custom AdamW with decoupled weight decay and bias corrections, a cosine scheduler, ResNet blocks, gradient-based adversarial attacks, and selected bonus experiments. No claim is made that this is a standalone reusable package; the executable source is the notebook.

## Evaluation protocols

**Do not mix clean accuracy, attacked accuracy, target hit rate, or training-set/held-out estimates.** PGD attack budgets use normalized pixel intensities [0,1]; the norm constraint and `eps` units should be read directly from each experiment. Targeted success is measured as the fraction reaching the selected target class, which is distinct from ordinary classification accuracy.

`sanity_checks` evaluates FGSM, PGD-20, and PGD-100 with five random restarts, and checks the ε=1 case. The reported evaluation subset for sanity checks is 256 images; the PGD-20 accuracy curve uses 1,000 FashionMNIST test images. Those figures need not match exactly.

FGSM metrics recorded *during adversarial training* use a different evaluation setup from the separate held-out `sanity_checks`: the sanity evaluation may also count only images correctly predicted on clean inputs before an adversarial success can be counted. Consequently, a high FGSM result from a training trajectory should **not** be equated with a separate sanity-check figure.

## Scope and limitations

- A single fixed-seed run cannot establish architecture or attack superiority across distributions.
- Adversarial robustness is empirical and attack-specific here; none of the results are certified.
- `PGD-AT` achieves high robustness at the training ε=0.1 but loses accuracy as ε grows.
- The 56-layer plain model was given the same finite epoch budget as the 20-layer one, so its underperformance should be described in terms of this setup.
- Reproducibility of exact GPU numerical results is not guaranteed across PyTorch and CUDA versions.

## Provenance

Figures are exported directly from saved outputs in `hw1.ipynb`; metrics and checkpoints are from the same final Colab run. The pinned `requirements.txt` is from the original assignment distribution.
