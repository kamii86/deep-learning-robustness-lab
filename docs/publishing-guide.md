# Publish for coursework review and a portfolio

The instructions request a **public GitHub repository and a pull request to that repository**. Keep `main` and `submission/hw1` separate until the instructor has had the opportunity to review the PR. After review, merge the PR if permitted to make the complete portfolio project visible on the repository's default branch.

## 1. Create the remote repository

At GitHub, create a **public** repository called `deep-learning-robustness-lab` under your account. Do **not** initialize it with a README, .gitignore, or license (those exist locally).

## 2. Prepare and push main

Open a terminal in this project folder. The first commit stages only the portfolio documentation and plots, so the notebook and checkpoints can be introduced via an actual PR:

```bash
git init -b main
git add README.md .gitignore requirements.txt docs/ figures/ .github/pull_request_template.md
git commit -m "docs: initialize deep learning portfolio"
git remote add origin https://github.com/YOUR_USERNAME/deep-learning-robustness-lab.git
git push -u origin main
```

Replace `YOUR_USERNAME` in the URL with your GitHub username. This first push intentionally leaves the notebook out of the default branch; the notebook will appear in the PR and, after merging, on `main`. The existing README links to it in anticipation of that merge.

## 3. Push the solution in its own branch

```bash
git switch -c submission/hw1
git add -A
git status
git commit -m "feat: implement deep learning and robustness experiments"
git push -u origin submission/hw1
```

The PR should contain `hw1.ipynb`, the trained checkpoints in `artifacts/`, and lightweight checks/CI.

## 4. Open the PR and submit the link

On GitHub, click **Compare & pull request** or go to **Pull requests → New pull request**. Ensure **base: `main`** and **compare: `submission/hw1`**; use title `Deep learning HW1 — convolution, optimization and adversarial robustness`. Leave the PR **open** for teaching staff to comment and grade. Submit the PR URL to the course platform, and include the repository URL if the form requests it.

> The course requirements take precedence over this suggested workflow. If an instructor requests a particular branch naming convention or review state, follow that requirement.

## 5. After review

If approved and allowed by your course process, merge the PR. Your `main` branch then becomes the portfolio landing page. Edit the GitHub repository description and topics, and optionally pin the repository on your profile.

**Suggested repository description:** `From-scratch CNN building blocks, ResNet on CIFAR-10, and adversarial robustness experiments in PyTorch.`

**Suggested topics:** `deep-learning`, `pytorch`, `computer-vision`, `resnet`, `adversarial-robustness`, `cifar10`, `fashion-mnist`, `ml-research`.

**CV entry (English):** *Deep Learning & Adversarial Robustness — PyTorch: implemented convolution and optimization primitives, trained ResNet-20 to 83.05% CIFAR-10 test accuracy, and studied PGD-based robustness and catastrophic overfitting.*
