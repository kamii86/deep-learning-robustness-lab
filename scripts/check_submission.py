#!/usr/bin/env python3
"""Static validation for the published, executed deep-learning notebook."""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ('metrics.json', 'resnet20.pt', 'fashion_standard.pt', 'fashion_pgd_at.pt')

def main():
    path = ROOT / 'hw1.ipynb'
    notebook = json.loads(path.read_text(encoding='utf-8'))
    cells = notebook['cells']
    codes = [c for c in cells if c['cell_type'] == 'code']
    bad_outputs = [(i, j) for i,c in enumerate(cells) if c['cell_type'] == 'code'
                   for j,o in enumerate(c.get('outputs', [])) if o['output_type'] == 'error']
    assert not bad_outputs, f'Notebook errors: {bad_outputs}'
    assert len(cells) >= 162 and len(codes) >= 80, 'Notebook appears incomplete'
    assert all(c.get('execution_count') is not None for c in codes), 'Some code cells have not been executed'
    assert len({c['id'] for c in cells}) == len(cells), 'Duplicate cell IDs'
    assert sum(c['metadata'].get('hw1') is not None for c in cells) == 162, 'Missing original hw1 metadata'
    for filename in REQUIRED:
        file = ROOT / 'artifacts' / filename
        assert file.is_file() and file.stat().st_size > 0, f'Missing/empty: {file}'
    m = json.loads((ROOT/'artifacts/metrics.json').read_text())
    assert m['fast_mode'] is False and m['attack_track'] == 'targeted'
    assert m['data']['cifar_train'] == 50000 and m['data']['cifar_test'] == 10000
    assert m['data']['fashion_train'] == 60000 and m['data']['fashion_test'] == 1000
    assert len(m['cifar']['history']['test_acc']) == 20
    acc = m['cifar']['history']['test_acc'][-1]
    assert acc >= 0.82, f'Expected >=82% ResNet-20 test accuracy, got {acc:.2%}'
    print(f'PASS: {len(codes)} executed code cells, 0 errors, CIFAR test accuracy {acc:.2%}, 3 checkpoint files.')
    print('Note: this is static validation only; it does not rerun training or hidden grader tests.')

if __name__ == '__main__':
    try: main()
    except (AssertionError, KeyError, ValueError, OSError) as exc:
        print(f'FAIL: {exc}', file=sys.stderr)
        raise SystemExit(1)
