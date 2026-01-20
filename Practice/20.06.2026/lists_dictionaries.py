# List
ai_list = ["Gemini", "Llama", "ChatGPT"]

# Dictionary
ai_model = {
    "Name": "MFK-AI",
    "Parameters": "70B",
    "Usecases": ["Chat", "Coding", "Summarization"]
}

# Add "Claude" to the list.
ai_list.append("Claude")

# Print the list, and the first thing of the list.
print(ai_list)
print(ai_list[0])

# Print the second thing of "Use_cases" in the ai_model.
print(ai_model["Usecases"][1]) 

# Sort the list, then print it.
ai_list.sort()
print(ai_list)

# Add version to the dictionary, then print it.
ai_model["Version"] = "1.0"
print(ai_model)

# Add multiple things to the dictionary, then print it.
ai_model.update({"Status": "Active", "Creator": "MFK-Dev"})
print(ai_model)

# Print the models one-by-one.
for model in ai_list:
    print(f"Model Name: {model}")

# Print the dictionaries keys and values one-by-one.
for key, value in ai_model.items():
    print(f"{key}: {value}")

#  __  __ ___ _  __   ___          
# |  \/  | __| |/ /__|   \ _____ __
# | |\/| | _|| ' <___| |) / -_) V /
# |_|  |_|_| |_|\_\  |___/\___|\_/   
