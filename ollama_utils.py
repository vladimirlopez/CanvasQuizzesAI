import requests

def list_ollama_models():
    """List available Ollama models running locally."""
    try:
        resp = requests.get("http://localhost:11434/api/tags")
        resp.raise_for_status()
        data = resp.json()
        return [m["name"] for m in data.get("models", [])]
    except Exception:
        return ["llama2", "mistral", "phi3"]  # fallback example

def chat_with_model(model, chat_history):
    """Send chat history to Ollama and get response from selected model."""
    messages = [{"role": m["role"], "content": m["content"]} for m in chat_history]
    payload = {"model": model, "messages": messages}
    try:
        resp = requests.post("http://localhost:11434/api/chat", json=payload, timeout=60)
        resp.raise_for_status()
        data = resp.json()
        return data.get("message", {}).get("content", "[No response]")
    except Exception as e:
        return f"[Error communicating with Ollama: {e}]"
