# Публикация проекта и сдача домашнего задания

В учебном задании требуется **публичный репозиторий GitHub и Pull Request**, в котором проверяющий оставит комментарии и итоговую оценку.

## Текущее состояние

Ветка `main` уже опубликована как документационный старт проекта. Если русская версия README устроит, закоммитьте обновлённые тексты и дополнительные графики в `main`. Затем добавьте выполненный ноутбук, веса и проверки в отдельной ветке `submission/hw1`.

## 1. Обновить русское оформление в main

Из папки репозитория:

```bash
git switch main
git add README.md docs/ figures/ .github/pull_request_template.md
git status
git commit -m "docs: localize portfolio and add all experiment figures"
git push origin main
```

Эти команды нужно выполнять **только после проверки предпросмотра и копирования обновлённых файлов в локальную папку**.

## 2. Добавить код и результаты отдельной веткой

```bash
git switch -c submission/hw1
git add hw1.ipynb artifacts/ scripts/check_submission.py .github/workflows/validate.yml
git status
git commit -m "feat: add deep learning experiments and trained checkpoints"
git push -u origin submission/hw1
```

`main` содержит документацию, а ветка `submission/hw1` — полный код и веса. Так Pull Request действительно будет показывать изменения.

## 3. Открыть Pull Request

На GitHub выберите **Pull requests → New pull request**. Проверьте: base = `main`, compare = `submission/hw1`. Заголовок: **«ДЗ 1 — свёртки, оптимизация, ResNet и adversarial robustness»**.

Не закрывайте PR до проверки преподавателем. Если преподаватель требует PR в иной целевой репозиторий, следуйте условиям курса.

## 4. После проверки

Когда преподаватель разрешит, можно объединить PR с `main`. После этого корневая страница станет полноценным портфолио с работающими ссылками на ноутбук и веса.

**Рекомендуемые GitHub topics:** `deep-learning`, `pytorch`, `computer-vision`, `resnet`, `adversarial-robustness`, `cifar10`, `fashion-mnist`.

**Текст для резюме:** «Deep Learning & Adversarial Robustness (PyTorch): реализация свёрток и оптимизатора AdamW, ResNet-20 с 83,05% на CIFAR-10, PGD adversarial training и исследование catastrophic overfitting».
