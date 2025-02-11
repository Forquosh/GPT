# GPT

A PyTorch implementation of a GPT-like language model with text preprocessing utilities.

## Overview

This project implements a transformer-based language model similar to GPT, designed for character-level text generation. It includes utilities for vocabulary generation and dataset splitting.

In this example, I tested it on the fabulous book The Brothers Karamazov, downloaded from Project Gutenberg. Feel free to change the text file or even try training it on an actual dataset (like OpenWebText for example), though on larger datasets the `vocab.py` and `split.py` might not work properly.

## Features

- Character-level language modeling
- Multi-head self-attention mechanism
- Memory-efficient data loading using memory mapping
- Text preprocessing utilities
- Configurable model architecture

## Requirements

- Python 3.9+
- PyTorch
- CUDA (optional, for GPU acceleration, **on Windows**)

## Project Structure

- `vocab.py` - Generates vocabulary from input text
- `split.py` - Splits text data into training and validation sets
- `GPT.ipynb` - Main model implementation and training

## Usage

### INITIALIZATION STEPS FOR **MAC OS**

Run the terminal in a directory of choice.

Create a _Python Virtual Environment_ and _activate_ it:

```bash
python3 -m venv venv
source ./venv/bin/activate
```

Install the _MacOS requirements_:

```bash
pip3 install -r requirements_macos.txt
```

### INITIALIZATION STEPS FOR **WINDOWS**

Install [Python](https://www.python.org/downloads/) on your system. If you have it already, skip this step.

Install [Anaconda](https://www.anaconda.com/download). Follow the steps from this link.

Once installed, open **Anaconda Prompt**.

Create a _Python Virtual Environment_ and _activate_ it:

```bash
python3 -m venv cuda
cuda\Scripts\activate
```

Install the _Windows requirements_:

```bash
pip3 install -r requirements_windows.txt
```

### ! These requirements are different. On Windows, PyTorch is installed with _CUDA_ support

### 2. Prepare Your Data

First, _add your desired data file and generate the vocabulary from your text_:

```bash
python3 vocab.py
```

Then, _split your data into training and validation sets_:

```bash
python3 split.py
```

### 2. Train the Model

Install a _new kernel_ to use in your Jupyter Notebook:

```bash
python3 -m ipykernel install --user --name=venv --display-name "GPTKernel"
```

Run Jupyter Notebook:

```bash
jupyter notebook
```

Open `GPT.ipynb`.

Select `GPTKernel` and run the cells _sequentially_. The notebook contains:

- Model architecture implementation
- Training loop
- Text generation functionality

### Model Parameters

The default hyperparameters are:

- Batch size: 32
- Block size: 128
- Maximum training iterations: 300
- Learning Rate: 2e-5
- Evaluation: every 50 iterations
- Embedding dimension: 300
- Number of heads: 4
- Number of layers: 4
- Dropout: 0.2

These can be adjusted based on your hardware capabilities and requirements.

## Model Architecture

The model implements a transformer architecture with:

- Multi-head self-attention
- Position embeddings
- Layer normalization
- Feed-forward networks

## License

MIT
