#--------------------------#

### Slicing

# list of models
models = ["GPT-4", "Llama-3", "Claude-3", "Gemini", "Mistral"]

# select first 3, then print it
top_3 = models[0:3]
print(top_3)

# select last 2, then print it.
last_2 = models[-2:]
print(last_2)

#--------------------------#

### Tuples

api_config = ("https://api.openai.com/v1", 443, "v1")
# api_config[0] = "yeni_link" ( you cant say this, because tuples are not changeable. )

#--------------------------#

### Sets

# Set the list, then clear the repeats and print it.
raw_data = ["AI", "ML", "AI", "DL", "ML"]
unique_data = set(raw_data)
print(unique_data)

#--------------------------#

# Create a list, select the ones in the middle and print it.
ai_tools = ["Flowith", "Pdf-Translator", "Image-Translator", "AppWizzy", "MindStudio", "Dropmagic"]
middle = ai_tools[2:4]
print(middle)

#--------------------------#

# Create a list, clear the repeats and print it.
numbers = [1, 2, 2, 3, 4, 5, 5, 6, 6, 7, 8, 8,]
unique_numbers = set(numbers)
print(unique_numbers)

#--------------------------#

#  __  __ ___ _  __   ___          
# |  \/  | __| |/ /__|   \ _____ __
# | |\/| | _|| ' <___| |) / -_) V /
# |_|  |_|_| |_|\_\  |___/\___|\_/  

#--------------------------#
