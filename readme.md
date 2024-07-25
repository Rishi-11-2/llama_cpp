A Fake OPEN AI Server Created using llama-cpp

We can run llama-cpp server on local machine at no cost

* Overview
  * GGUF Models are used for inferencing with llama-cpp

  * in 'app.py' (mistral-7b-instruct-v0.1.Q2_K.gguf) is used for any stock data analysis. Mixtral model can also be used depending on the local computer's physical memory(RAM)

  * in 'multimodal.py' , user can enter images along with prompt and 'llava' model is used for inferencing. 

* How to Run the llama-cpp server
  * Single Model Chat: _ python -m --model models/mistral-7b-instruct-v0.1.Q4_0.gguf_

  * Single Model Chat with GPU Offload: _ python -m --model models/mistral-7b-instruct-v0.1.Q4_0.gguf --n_gpu -1 _

   * Single Model Function Calling with GPU Offload: _ python -m --model models/mistral-7b-instruct-v0.1.- Q4_0.gguf --n_gpu -1 --chat functionary _

   * Multiple Model Load with Config: _ python -m --config_file config.json _

   * Multi Modal Models: _ python -m llama_cpp.server --model models/llava-v1.5-7b-Q4_K.gguf --clip_model_path models/llava-v1.5-7b-mmproj-Q4_0.gguf --n_gpu -1 --chat llava-1-5 _

* Models used :
  * mistral-7b-instruct-v0.1.Q2_K.gguf

  * llava-v1.5-7b-mmproj-Q4_0.gguf

  * llava-v1.5-7b-Q4_K.gguf