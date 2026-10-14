from huggingface_hub import model_info

models = [
    "meta-llama/Llama-3.2-1B-Instruct",
    "Qwen/Qwen2.5-1.5B-Instruct",
    "Qwen/Qwen3-1.7B",
    "Qwen/Qwen3-4B-Instruct-2507",
]

for model in models:
    info = model_info(
        model,
        expand="inferenceProviderMapping"
    )
    print(f"\n{model}")

    for mapping in info.inference_provider_mapping:
        print(f"  {mapping.provider}: {mapping.status}")