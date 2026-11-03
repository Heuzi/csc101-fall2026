"""CSC 101: Build Your Own Offline AI Chatbot.

First, with internet: python offline_chatbot.py --download
Then, even offline:  python offline_chatbot.py
"""

# 1. SETTINGS: choose the pretrained model and our chatbot's behavior.
# These standard-library imports handle commands, folders, and settings.
import argparse
import os
from pathlib import Path

MODEL_ID = "Qwen/Qwen3-0.6B"
# A fixed revision makes everyone download the same model files.
MODEL_REVISION = "c1899de289a04d12100db370d81485cdf75e47ca"
MODEL_DIR = Path(__file__).resolve().parent / "models" / "Qwen3-0.6B"
SYSTEM_PROMPT = "You are a helpful assistant. Give short, clear answers."
MAX_NEW_TOKENS = 128  # Limit the length and running time of each response.
MAX_INPUT_TOKENS = 2048  # Keep our classroom conversations small.


# 2. DOWNLOAD: copy existing learned weights and supporting files to disk.
# This step needs internet. It does not train a new model.
def download_model():
    from huggingface_hub import snapshot_download

    print(f"Downloading {MODEL_ID} to {MODEL_DIR}", flush=True)
    snapshot_download(
        repo_id=MODEL_ID,
        revision=MODEL_REVISION,
        local_dir=MODEL_DIR,
        # Download the weights, settings, tokenizer, and license, not other apps.
        allow_patterns=["*.safetensors", "*.json", "merges.txt", "LICENSE"],
    )
    print("Download finished. You can now disconnect from the internet.")


# 3. LOAD: create the model using library code and fill it with saved weights.
def load_model():
    if not (MODEL_DIR / "model.safetensors").is_file():
        raise OSError("Model files are missing. Run with --download while online first.")

    # Set these BEFORE importing the libraries so they do not contact the Hub.
    os.environ["HF_HUB_OFFLINE"] = "1"
    os.environ["TRANSFORMERS_OFFLINE"] = "1"
    os.environ["USE_TF"] = "0"  # Use PyTorch only, even if TensorFlow is installed.

    import torch
    from transformers import AutoModelForCausalLM, AutoTokenizer

    # CPU execution works without a special graphics card. A few CPU threads
    # help this small model without overwhelming a laptop with worker threads.
    torch.set_num_threads(min(4, os.cpu_count() or 1))
    print("Loading tokenizer and weights from local files...", flush=True)
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_DIR,
        local_files_only=True,
        dtype=torch.float32,  # Widely supported on laptop CPUs; uses more RAM.
    ).to("cpu")
    model.eval()  # Use the trained model for inference, rather than training.
    print("Ready. The model is running on this computer's CPU.")
    return tokenizer, model


# 4. GENERATE: conversation -> tokens -> model predictions -> readable reply.
def generate_reply(tokenizer, model, messages):
    import torch

    # The template marks which messages came from the system, user, or assistant.
    # Turn off Qwen3's thinking mode to keep our classroom responses short.
    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )
    inputs = tokenizer(text, return_tensors="pt")
    prompt_length = inputs["input_ids"].shape[1]
    if prompt_length > MAX_INPUT_TOKENS:
        raise ValueError("This conversation is full. Type /reset and ask a shorter question.")

    # Inference predicts new tokens without updating the learned weights.
    # Sampling makes repeated answers vary. Temperature controls randomness.
    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=MAX_NEW_TOKENS,
            do_sample=True,
            temperature=0.7,
            top_p=0.8,
            top_k=20,
            pad_token_id=tokenizer.eos_token_id,
        )

    # generate() returns the original prompt AND new tokens. Display only new ones.
    new_tokens = output[0][prompt_length:]
    answer = tokenizer.decode(new_tokens, skip_special_tokens=True).strip()
    if len(new_tokens) >= MAX_NEW_TOKENS:
        answer += "\n[Response reached the length limit. Try asking for a shorter answer.]"
    return answer


# 5. CHAT: keep a conversation in memory so follow-up questions have context.
def chat(tokenizer, model):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    print("Commands: /reset = new conversation; /model = architecture; /quit = exit")
    while True:
        try:
            user_text = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nGoodbye!")
            return
        if user_text == "/quit":
            return
        if user_text == "/reset":
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            print("Conversation cleared. The model's weights have not changed.")
            continue
        if user_text == "/model":
            print(model)  # Show the actual layers assembled by Transformers.
            continue
        if not user_text:
            continue

        messages.append({"role": "user", "content": user_text})
        try:
            answer = generate_reply(tokenizer, model, messages)
        except ValueError as error:
            messages.pop()  # Remove a question that could not fit in the context.
            print(error)
            continue
        print(f"\nAssistant: {answer}")
        messages.append({"role": "assistant", "content": answer})
        # History lives only in this process. The program does not save chat logs.


# 6. START: choose either the online download step or the offline chat step.
def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true", help="Download model files, then exit.")
    parser.add_argument("--prompt", help="Answer one question, then exit (useful for a quick test).")
    args = parser.parse_args()
    if args.download and args.prompt is not None:
        parser.error("Use --download first; then run a separate command to chat.")

    try:
        if args.download:
            download_model()
            return
        tokenizer, model = load_model()
        if args.prompt is not None:
            messages = [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": args.prompt},
            ]
            print(generate_reply(tokenizer, model, messages))
        else:
            chat(tokenizer, model)
    except (ImportError, OSError, ValueError) as error:
        parser.exit(1, f"\nCould not run the chatbot: {error}\nCheck the classwork setup steps.\n")


if __name__ == "__main__":
    main()
