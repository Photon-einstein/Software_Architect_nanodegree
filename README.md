# Software_architect_nanodegree

## To activate the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
deactivate
```

## To get the requirements and install from it

```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

## Conda commands

```bash
conda create -n soft_arch python=3
conda activate soft_arch
conda list
conda env list
conda install pytest

conda update --all
conda upgrade --all
conda env export > environment.yaml
conda env create -f environment.yaml
conda env remove -n env_name

conda deactivate
```

[Conda Command reference guide](https://docs.conda.io/projects/conda/en/latest/commands/index.html)

## To test PEP 8 style violations

```bash
pip3 install pycodestyle
pycodestyle starter
```
