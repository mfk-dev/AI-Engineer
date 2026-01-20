import sys
import os
import time

# --- Configuration & Colors ---
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[33m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
    "bold": "\033[1m"
}

# --- Utility Functions ---
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow(text, color=COLORS["reset"], delay=0.04):
    for ch in text:
        sys.stdout.write(color + ch + COLORS["reset"])
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")

def menu_header(title):
    print(f"\n{COLORS['purple']}{'='*40}")
    print(f"{COLORS['bold']}{title.upper()}{COLORS['reset']}")
    print(f"{COLORS['purple']}{'='*40}{COLORS['reset']}")

# --- Content Data (The Roadmap) ---
ROADMAP_DATA = {
    "1": {
        "title": "Months 1-2: Foundations",
        "content": [
            "• Python (Deep Dive) & Asynchronous Programming",
            "• Basic Linear Algebra & Statistics",
            "• Roadmap.sh Fundamentals (OS, Networking)",
            "• Git & GitHub (Version Control)",
            "• Data Power: Pandas & NumPy"
        ]
    },
    "2": {
        "title": "Month 3: Machine Learning Core",
        "content": [
            "• Scikit-learn (Classical ML)",
            "• Neural Networks (Theory & Math)",
            "• PyTorch (Building Tensors & Models)",
            "• HuggingFace (Model Hub & Transformers)"
        ]
    },
    "3": {
        "title": "Month 4: API & Prompting",
        "content": [
            "• API Integration (OpenAI / Anthropic)",
            "• Advanced Prompt Engineering",
            "• Function Calling (Teaching AI to use tools)"
        ]
    },
    "4": {
        "title": "Month 5: RAG Systems",
        "content": [
            "• RAG (Retrieval-Augmented Generation)",
            "• Vector Databases (Pinecone, ChromaDB)",
            "• Chunking Strategies (Data Processing)"
        ]
    },
    "5": {
        "title": "Months 6-7: AI Agents",
        "content": [
            "• Orchestration: LangChain or LlamaIndex",
            "• Agentic Workflows (Autonomous Logic)",
            "• LangGraph (Cyclic Agent Structures)"
        ]
    },
    "6": {
        "title": "Month 8+: Deployment & MLOps",
        "content": [
            "• Docker & Kubernetes (Containerization)",
            "• Model Monitoring (Evaluation & Hallucination tracking)"
        ]
    }
}

# --- Screens ---
def show_roadmap_details():
    while True:
        clear()
        menu_header("AI Engineer Roadmap")
        for key, data in ROADMAP_DATA.items():
            print(f"{COLORS['yellow']}[{key}]{COLORS['reset']} {data['title']}")
        
        print(f"\n{COLORS['cyan']}Input '.' to go back | 'exit' to quit{COLORS['reset']}")
        choice = input(f"{COLORS['green']}> {COLORS['reset']}").lower()

        if choice in ROADMAP_DATA:
            clear()
            selected = ROADMAP_DATA[choice]
            menu_header(selected['title'])
            for item in selected['content']:
                slow(item, COLORS["yellow"], 0.02)
            
            input(f"\n{COLORS['blue']}[*] Press Enter to return to roadmap list...{COLORS['reset']}")
        elif choice == ".":
            break
        elif choice == "exit":
            sys.exit()

def welcome_screen():
    clear()
    slow(">>> INITIALIZING AI-GUIDE TERMINAL...", COLORS["cyan"], 0.02)
    time.sleep(0.5)
    print(f"\n{COLORS['purple']}Welcome, Future Engineer.{COLORS['reset']}")
    print("This guide is designed to take you from zero to AI Engineering.")
    time.sleep(1)

# --- Main Program ---
def main():
    welcome_screen()
    while True:
        clear()
        menu_header("Main Menu")
        print(f"{COLORS['yellow']}[1]{COLORS['reset']} Start Roadmap")
        print(f"{COLORS['yellow']}[2]{COLORS['reset']} Help / Commands")
        print(f"{COLORS['yellow']}[3]{COLORS['reset']} System Info")
        print(f"{COLORS['red']}[exit]{COLORS['reset']} Quit")

        cmd = input(f"\n{COLORS['green']}@ai_engineer ~ {COLORS['reset']}").lower()

        if cmd == "1" or cmd == "roadmap":
            show_roadmap_details()
        elif cmd == "2" or cmd == "help":
            clear()
            menu_header("Available Commands")
            print("- '1' or 'roadmap' : View the 8-month plan")
            print("- '.'               : Go back one step")
            print("- 'exit'            : Close terminal")
            input(f"\n{COLORS['blue']}[*] Press Enter to continue...{COLORS['reset']}")
        elif cmd == "3":
            clear()
            print(f"{COLORS['cyan']}AI-Guide v1.0 (2026 Edition)")
            print(f"Status: Online")
            print(f"Goal: Zero to Hero AI Engineering{COLORS['reset']}")
            input(f"\n{COLORS['blue']}[*] Press Enter to continue...{COLORS['reset']}")
        elif cmd == "exit":
            clear()
            slow("Terminating session... Happy coding!", COLORS["red"], 0.05)
            break
        else:
            print(f"{COLORS['red']}Unknown command.{COLORS['reset']}")
            time.sleep(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nForcefully closing...")
        sys.exit()