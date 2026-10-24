## Что реализовано

- [x] Свёртки, backward, BatchNorm, AdamW и обучение ResNet
- [x] PGD-L∞ / PGD-L2, targeted-атака, adversarial training
- [x] Бонусы 7.1, 7.2, 7.4, 7.5
- [x] Сохранены результаты всех выполненных ячеек и исходные метаданные задания

## Окружение и данные

- Полный прогон: `FAST_MODE=False`
- Устройство: NVIDIA Tesla T4
- CIFAR-10: 50 000 train / 10 000 test
- FashionMNIST: 60 000 train / 1 000 test
- Ветка атаки: `targeted`

## Ключевые итоги

- ResNet-20 на CIFAR-10: **83,05% test accuracy**.
- PGD-20, ε = 0,1: **0,60% стандартная модель → 70,40% PGD-AT**.
- Исследован catastrophic overfitting при FGSM training; random start улучшил устойчивость.

## Чек-лист проверки

- [x] Сохранены outputs ячеек
- [x] В `artifacts/` находятся `metrics.json` и три checkpoint-файла
- [x] В ноутбуке есть ответы и численные выводы
- [x] Нет приватных ключей, токенов и локальных датасетов

**Прошу оставить замечания и итоговую оценку в комментариях к этому Pull Request.**
