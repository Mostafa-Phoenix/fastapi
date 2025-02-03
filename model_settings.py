# model_settings.py

settings_top_quality = {
    "temperature": 0.4,  # Very focused, deterministic
    "max_tokens": 2048,   # Allow for very detailed answers
    "top_p": 0.9,        # Restrict to highly probable options
    "top_k": 30,         # Only consider the top 30 tokens
    "repeat_penalty": 1.2, # Strongly discourage repetitions
    "mirostat_mode": 2,  # Use Mirostat for perplexity control
    "mirostat_tau": 4.0,  # Target a relatively low perplexity
    "mirostat_eta": 0.05 # adapt slowly
}

settings_high_quality = {
    "temperature": 0.6,   # A bit more creative than "Top Quality"
    "max_tokens": 1500,  # Still detailed, but not extremely long
    "top_p": 0.95,        # Allow a little more flexibility
    "top_k": 40,         # Consider more options than "Top Quality"
    "repeat_penalty": 1.1,  # Still discourage repetitions
    "mirostat_mode": 2,   # Mirostat for perplexity
    "mirostat_tau": 5.0,   # Target a medium level of perplexity
    "mirostat_eta": 0.1 # normal speed
}

settings_balanced = {
    "temperature": 0.7,   # Moderate creativity and randomness
    "max_tokens": 1024, # Reasonable response length
    "top_p": 0.95,        # Moderate flexibility
    "top_k": 50,          # Consider a wider range of options
    "repeat_penalty": 1.05, # Mildly discourage repetitions
    "mirostat_mode": 1,  # Mirostat for perplexity
    "mirostat_tau": 6.0, # Target a higher level of perplexity
    "mirostat_eta": 0.2 # faster adaptation
}

settings_high_speed = {
    "temperature": 0.8,   # More creative, less predictable
    "max_tokens": 512,  # Very short responses
    "top_p": 0.98,        # Very wide sampling, accept many options
    "top_k": 60,         # Consider many choices
    "repeat_penalty": 1.0, # No repetition penalty
    "mirostat_mode": 0,  # Mirostat disabled
    "mirostat_tau": 0.0, # not used
    "mirostat_eta": 0.0 # not used
}

settings_top_speed = {
    "temperature": 0.9,   # Very high randomness
    "max_tokens": 256,  # Extremely short responses
    "top_p": 1.0,         # Essentially no restrictions on token sampling
    "top_k": 0, # Consider every option, not top-k
    "repeat_penalty": 0.9, # Encourage to repeat
    "mirostat_mode": 0,  # Mirostat disabled
    "mirostat_tau": 0.0, # not used
    "mirostat_eta": 0.0 # not used
}
