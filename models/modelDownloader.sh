#!/bin/bash

# Different models to get
declare -A MODELS
MODELS["DeepSeek-R1-Distill-Qwen-1.5B-Uncensored"]="https://huggingface.co/mradermacher/DeepSeek-R1-Distill-Qwen-1.5B-uncensored-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-uncensored.Q2_K.gguf"
MODELS["DeepSeek-R1-Distill-Qwen-7B-Uncensored"]="https://huggingface.co/mradermacher/DeepSeek-R1-Distill-Qwen-7B-Uncensored-i1-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-7B-Uncensored.i1-Q4_K_M.gguf"
MODELS["DeepSeek-R1-Distill-Qwen-14B-Uncensored"]="https://huggingface.co/mradermacher/DeepSeek-R1-Distill-Qwen-14B-Uncensored-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-14B-Uncensored.Q4_K_M.gguf"
MODELS["DeepSeek-R1-Distill-Qwen-32B-Uncensored"]="https://huggingface.co/mradermacher/DeepSeek-R1-Distill-Qwen-32B-Uncensored-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-32B-Uncensored.Q4_K_M.gguf"
MODELS["DeepSeek-R1-Distill-Llama-70B-Uncensored"]="https://huggingface.co/mradermacher/DeepSeek-R1-Distill-Llama-70B-Uncensored-i1-GGUF/resolve/main/DeepSeek-R1-Distill-Llama-70B-Uncensored.i1-Q4_K_M.gguf"



MODELTOGET=${MODELS["DeepSeek-R1-Distill-Qwen-7B-Uncensored"]}

# Download the model
wget -O model.gguf "$MODELTOGET"
