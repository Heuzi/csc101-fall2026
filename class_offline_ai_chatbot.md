# Build Your Own Offline AI Chatbot

Class 13 | November 18, 2026

Today we will build and run a small AI chatbot on our own computers. We will use **Qwen3-0.6B**, a pretrained, open-weight language model, and a commented Python program that we will read together in VS Code.

Our sequence: **watch -> understand the model -> read the code -> download and load the weights -> test -> go offline**.

## Before class: prepare the software

Bring a laptop with VS Code and **Python 3.10, 3.11, or 3.12** installed. Plan for at least 8 GB of RAM and about 6 GB of free disk space for the software and model. These are planning targets; speed and memory use depend on your computer. We will use the CPU, so a dedicated graphics card is optional.

Download these two files into one folder named `offline_chatbot`. On GitHub, open each file and use **Download raw file**:

- [Download the commented Python program](./offline_chatbot/offline_chatbot.py)
- [Download requirements.txt](./offline_chatbot/requirements.txt)

Open that folder in VS Code, then choose **Terminal > New Terminal**. Install the libraries before class while you have internet access. Leave the model-weight download for our in-class walkthrough; if your connection is slow, complete Part 4 beforehand too.

**Windows / PowerShell:**

First, check whether Python 3.12 is installed:

```powershell
py -3.12 --version
```

If it reports **Python 3.12.x**, continue to the setup commands below. If Python 3.12 is missing, you can install it **alongside your newer Python** without uninstalling that version or removing its packages:

1. Open the [Python 3.12.10 release page](https://www.python.org/downloads/release/python-31210/) and download **Windows installer (64-bit)**.
2. Run the installer. Keep `pip` enabled and leave **Add python.exe to PATH** unchecked, so this installation does not change which Python the `python` command finds. The `py -3.12` command selects Python 3.12 explicitly.
3. Reopen the terminal in VS Code and run `py -3.12 --version` again to confirm the installation.

If you already created `.venv` using the wrong Python version, rename that folder to `.venv-old` before continuing. If you are using Python 3.10 or 3.11, you can keep using it instead; replace `-3.12` below with your version.

Run these commands **one line at a time** from the `offline_chatbot` folder:

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m pip install torch==2.8.0 --index-url https://download.pytorch.org/whl/cpu
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

The version check should report the Python version you selected. The `.venv` folder keeps this chatbot's packages separate from your other Python installations and projects. The first install command selects PyTorch's CPU package to keep the download smaller.

**macOS / Linux:**

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
```

In VS Code, use **Python: Select Interpreter** from the Command Palette and select the interpreter inside `.venv`. The commands below use that interpreter directly, so activating the environment is unnecessary. This exercise uses PyTorch and Transformers directly; Ollama is not needed.

## Part 1: Watch and discuss

Watch 3Blue1Brown's [Large Language Models explained briefly](https://www.youtube.com/watch?v=LPZh9BOjkQs&t=34s), starting at the linked 0:34 mark.

Discuss together:

- What does a language model predict?
- What is the difference between training a model and using a trained model?
- How can predicting one token at a time produce an entire conversation?

## Part 2: Meet our model

We will use [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B). It is a small member of the Qwen3 family, designed for tasks such as conversation and instruction following. Its size makes it a practical classroom starting point while still allowing us to explore useful responses, follow-up questions, and mistakes.

Keep these pieces separate:

| Piece | What it does in our chatbot |
|---|---|
| Model code / architecture | Defines the calculations and neural-network layers; supplied by the Transformers library. |
| Weights / parameters | Numbers learned during training; downloaded from the model publisher. |
| Tokenizer | Converts text into token IDs and converts generated IDs back into text. |
| Chat program | Collects our questions, supplies conversation history, runs the model, and displays replies. |

The model's weight file is about **1.5 GB** in this exercise. It is not the smaller, compressed Ollama download. When we run it, our program uses 32-bit numbers for broad CPU compatibility, so the weights occupy about 3 GB of RAM, plus memory for Python and the model's calculations.

We are using an already trained model. Downloading weights does not train it, and chatting with this program does not update its weights. A small model can produce useful text and also confidently give incorrect answers.

## Part 3: Read the code together

Open `offline_chatbot.py`. Its numbered comment sections follow the steps below. We will trace the program before running it; you do not need to understand every library detail.

| Code section | What to look for |
|---|---|
| 1. Settings | `MODEL_ID`, the local model folder, `SYSTEM_PROMPT`, and response-length limits. |
| 2. Download | `snapshot_download(...)` copies the weights, tokenizer, and settings to our computer. |
| 3. Load | `AutoTokenizer` loads the tokenizer; `AutoModelForCausalLM` builds the Qwen3 model and loads its weights. |
| 4. Generate | Format the chat, turn text into token IDs, predict new tokens, and decode the reply. |
| 5. Chat | A loop collects questions and stores both sides of the conversation in `messages`. |
| 6. Start | Command-line options choose downloading, a single test question, or interactive chat. |

To look inside the actual model code, open [Qwen3's implementation in Transformers](https://github.com/huggingface/transformers/blob/v4.57.6/src/transformers/models/qwen3/modeling_qwen3.py). Locate `Qwen3Attention`, `Qwen3MLP`, `Qwen3DecoderLayer`, `Qwen3Model`, and `Qwen3ForCausalLM`. We will identify their roles rather than read every line.

Follow the broad path through the model:

```text
Text -> tokenizer -> token IDs -> token embeddings
     -> repeated transformer layers (attention + feed-forward network)
     -> scores for possible next tokens -> selected token -> repeat
     -> tokenizer decodes the generated IDs into a reply
```

Pause and discuss:

- Which file contains our chatbot interface, and where does the neural-network implementation come from?
- Where do the learned numbers enter the program?
- Why do we keep a list of earlier messages?
- What does `enable_thinking=False` change? Why might shorter generation help on a laptop?

## Part 4: Download the weights

Stay connected to the internet. Run the download command from the folder containing the Python file.

**Windows:**

```powershell
.\.venv\Scripts\python.exe offline_chatbot.py --download
```

**macOS / Linux:**

```bash
.venv/bin/python offline_chatbot.py --download
```

Wait for **Download finished**. The script creates `models/Qwen3-0.6B` next to itself. If the download is interrupted, reconnect and run the same command again.

In VS Code's Explorer, find these files:

- `model.safetensors`: the learned weights; notice its size.
- `config.json`: architecture settings. Find `num_hidden_layers` and `hidden_size`.
- `tokenizer.json` and `tokenizer_config.json`: tokenization and conversation-format settings.

The script requests a fixed version of the publisher's files so we use the same model in class. No account or API key is needed for this public download.

## Part 5: Load and test the chatbot

Run the program again without `--download`:

**Windows:**

```powershell
.\.venv\Scripts\python.exe offline_chatbot.py
```

**macOS / Linux:**

```bash
.venv/bin/python offline_chatbot.py
```

Watch for **Loading tokenizer and weights from local files...**, then **Ready**. Loading moves the saved model into memory. The program now uses local files only.

Try these prompts, one at a time. Responses may take a while on a CPU and will vary:

1. `Explain what a computer file is in two short sentences.`
2. `Now explain it to a ten-year-old.`
3. `My imaginary pet dragon is named Pebble. Reply with its name.`
4. `What is my dragon's name?`

Now try the commands:

- `/model`: show the model's actual layers. Find the embeddings, attention, feed-forward layers, and output head. Compare the number of repeated layers with `config.json`.
- `/reset`: clear the conversation, then ask about your dragon's name again. Observe what happens; answers can be incorrect or guessed.
- `/quit`: exit the program.

Compare the first explanation and the follow-up. What information did the program need to include for the follow-up to make sense?

## Part 6: Prove it works offline

1. Exit the chatbot with `/quit`.
2. Disconnect Wi-Fi and any other internet connection.
3. Start the chatbot again using the same command from Part 5.
4. Ask a new question and a follow-up question.

Restarting while disconnected shows that both loading and generation work from local files. The program sets offline mode and uses `local_files_only=True`; it sends no chat request to a hosted model service.

After your test, reconnect when needed. Keep both the installed libraries and the `models` folder if you want to run the chatbot offline again. Conversation history lasts only until `/reset` or the program exits.

## If time permits: make it yours

Exit the program, edit `SYSTEM_PROMPT`, and restart. For example, give the assistant a role such as a computing vocabulary tutor. Ask the same question before and after your change and compare the responses.

Discuss: Did you change the model's weights, the instructions, or both?

## Troubleshooting

| What you see | What to try |
|---|---|
| `No module named ...` | Use the `.venv` interpreter and rerun the requirements installation while online. |
| Model files are missing or cannot load | Reconnect and rerun `--download`; keep the complete `models` folder next to the script. |
| A long pause after asking a question | CPU generation can be slow. Ask for a short answer and wait; use Ctrl+C to stop. |
| The computer runs out of memory | Close other applications. Ask the instructor about working with a partner. |
| The answer stops mid-sentence | It reached `MAX_NEW_TOKENS`. Ask for a shorter answer. |
| The conversation is full | Type `/reset`; this classroom program limits the input length to control memory use. |

## References

- [Qwen3-0.6B model card and usage example](https://huggingface.co/Qwen/Qwen3-0.6B)
- [Transformers: installation and offline mode](https://huggingface.co/docs/transformers/v4.57.6/installation)
- [Hugging Face Hub: downloading files](https://huggingface.co/docs/huggingface_hub/v0.36.0/guides/download)
