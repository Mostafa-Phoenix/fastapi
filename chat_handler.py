from model_loader import model_instance
from model_settings import (
    settings_high_quality,
    settings_balanced,
    settings_high_speed,
    settings_top_quality,
    settings_top_speed,
)

# Choose the settings you want to use (change this to select a different set)
# settings_to_use = settings_high_quality
# settings_to_use = settings_balanced
settings_to_use = settings_high_speed
# settings_to_use = settings_top_quality
# settings_to_use = settings_top_speed


def generate_response(user_message: str) -> str:
    """
    Generates a response from the model given a user message
    """
    if not model_instance:
        return "Error: Model not loaded"

    try:
        # Create the full prompt with chat formatting
        prompt = (
            f"<|im_start|>user\n{user_message}<|im_end|>\n<|im_start|>assistant\n"
        )

        # Generate response using the chosen settings
        response = model_instance.create_chat_completion(
            messages=[{"role": "user", "content": user_message}],
            temperature=settings_to_use["temperature"],
            max_tokens=settings_to_use["max_tokens"],
            stop=["<|im_end|>"],
            top_p=settings_to_use["top_p"],
            top_k=settings_to_use["top_k"],
            repeat_penalty=settings_to_use["repeat_penalty"],
            mirostat_mode=settings_to_use["mirostat_mode"],
            mirostat_tau=settings_to_use["mirostat_tau"],
            mirostat_eta=settings_to_use["mirostat_eta"],
        )

        return response["choices"][0]["message"]["content"]
    except Exception as e:
        return f"Error generating response: {str(e)}"
