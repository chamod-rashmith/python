import os
import subprocess
import sys
from colorama import init, Fore, Style

# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print(Fore.YELLOW + Style.BRIGHT + "   🐍 PYTHON LEARNING COURSE 🐍")
    print(Fore.CYAN + Style.BRIGHT + "="*40)
    print("\n" + Fore.GREEN + "Available Lessons & Exercises:")
    
    # We'll check both lessons and exercises
    content_dirs = ["lessons", "exercises"]
    all_items = []
    
    for c_dir in content_dirs:
        if os.path.exists(c_dir):
            for root, dirs, files in os.walk(c_dir):
                for file in sorted(files):
                    if file.endswith(".py"):
                        rel_path = os.path.relpath(os.path.join(root, file))
                        all_items.append(rel_path)

    for i, item in enumerate(all_items, 1):
        # Color lessons and exercises differently
        # Format path for display: lessons/01_basics/01_intro.py -> [Lesson] 01_intro
        parts = item.split(os.sep)
        category = parts[0].capitalize()
        name = parts[-1].replace(".py", "").replace("_", " ").title()
        
        color = Fore.BLUE if "lessons" in item else Fore.MAGENTA
        print(f"{Fore.WHITE}{i:2}. {color}[{category}] {Fore.WHITE}{name} {Style.DIM}({item})")

    print(f"\n{Fore.RED}Q. Quit")
    
    try:
        choice = input(Fore.WHITE + "\nSelect an item to run (number) or 'Q' to quit: ").strip().lower()
        
        if choice == 'q':
            print(Fore.YELLOW + "Happy coding!")
            return

        index = int(choice) - 1
        if 0 <= index < len(all_items):
            item_path = all_items[index]
            print(f"\n{Fore.GREEN}--- Running: {item_path} ---\n")
            # Using current python associated with the environment
            subprocess.run([sys.executable, item_path])
            print("\n" + Fore.GREEN + "-"*40)
        else:
            print(Fore.RED + "Invalid selection.")
    except ValueError:
        print(Fore.RED + "Please enter a number.")
    except Exception as e:
        print(Fore.RED + f"An error occurred: {e}")

if __name__ == "__main__":
    main()


