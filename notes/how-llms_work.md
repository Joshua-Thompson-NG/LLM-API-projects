# Tokens
Before an LLM processed a prompt, a component called a tokenizer chops the raw text into smalled units called tokens.
 
Modern LLMs typically use BPE (Byte Pair Encoding). So common words like "apple" is a token on its own, while complex words like tokenization is split into "token" and "ization" (this is just an example). 

1 token is roughly 3/4 of a word (English). 

# Context Window
This is the max number of token an LLM can hold in its active memory during a single request.
Since an API request is stateless, that means for every request you send in an active chat the context windows grows larger since it appends the previous conversations to it as part of its context window.

# Temperature
It's a mathematical rule that determines how a model picks one token from the giant probability list.
Low Temp - 0.0 to 0.3

Med Temp - 0.7 to 0.8

High Temp - 1.0 to 2.0

# Safety Guardrails
- Top K: Tells the model to only consider the top k most likely tokens. e.g. Top K = 40, ignores 41 and below.
- Top P: Tells the model to keep adding the top tokens until their combined possibility reaches P.

# Hallucinations
It's when an LLM generated confident information that is factually false.
## Ways to reduce it
- In-context grounding $ RAG
- Use explicit prompts.
- Give it permission to say "I don't know".
- Requiring Citations, in some scenarios
- Lowering Temperature
 Note: even with all these there's still a chance it still happens.

# Three Core Model Tiers
- Small and Fast
- Flagship or Balanced
- Frontier and Reasoning