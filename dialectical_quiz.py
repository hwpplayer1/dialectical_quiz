"""
Play to steal from dictators !

Copyright (C) 2026 Mert Gör 

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
import sys
import os

# ANSI Escape Codes for NY Style Cyberpunk / Socialist Terminal Theme
RED = "\033[1;31m"
GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
MAGENTA = "\033[1;35m"
CYAN = "\033[1;36m"
WHITE = "\033[1;37m"
RESET = "\033[0m"

def run_dialectical_quiz():
    print(RED + "==================================================" + RESET)
    print(CYAN + "   THE DIALECTICAL OLYMPUS PERSONALITY MATRIX     " + RESET)
    print(RED + "==================================================" + RESET)
    print(WHITE + "Welcome, Comrade. Let's evaluate your algorithmic labor value.\n" + RESET)
    
    # Prompt for Comrade Name / Alias
    comrade_name = input(YELLOW + "Enter your Comrade Name or Developer Alias: " + RESET).strip()
    if not comrade_name:
        comrade_name = "Anonymous Proletarian"
    
    print(GREEN + f"\nGreetings, Comrade {comrade_name}. Initializing the matrix...\n" + RESET)
    print("-" * 50)

    # 5-Question Point-Based Quiz
    questions = [
        {
            "text": "1. A proprietary tech giant closes its source code. What's your move?",
            "options": [
                ("File a formal complaint and optimize internal state infrastructure.", 1),
                ("Fork it, crack it, and release it open-source for the masses.", 4),
                ("Build a centralized, state-backed alternative framework.", 2),
                ("Write a script to flood and crash their corporate servers.", 5)
            ]
        },
        {
            "text": "2. How do you view the relationship between backend and frontend?",
            "options": [
                ("The frontend is a bourgeois illusion; the backend holds the raw value.", 3),
                ("They must be synthesized into a perfectly planned, unified design.", 2),
                ("Decentralize everything; strict pipelines restrict worker creativity.", 5),
                ("The backend is the means of production, which we must seize.", 4)
            ]
        },
        {
            "text": "3. Your development team is facing a severe deadline crisis. You:",
            "options": [
                ("Enforce strict, top-down management to meet the collective quota.", 1),
                ("Martyr yourself by pulling an all-nighter to save the team's project.", 4),
                ("Analyze the systemic blockages using rigorous data-driven theory.", 2),
                ("Organize a wildcat strike against the project managers immediately.", 5)
            ]
        },
        {
            "text": "4. What is the ultimate purpose of building high-performance AI algorithms?",
            "options": [
                ("Automating production to totally eliminate the necessity of wage labor.", 4),
                ("Establishing absolute, centralized data supremacy for stability.", 1),
                ("Streamlining resource allocation in a scientifically planned economy.", 2),
                ("Liberating data from servers to run on localized consumer hardware.", 3)
            ]
        },
        {
            "text": "5. Choose your favorite programming paradigm or environment:",
            "options": [
                ("Deep, hidden system kernels and raw assembly level optimization.", 3),
                ("Strict, statically-typed, and perfectly structured enterprise code.", 2),
                ("Chaotic, highly concurrent, and deeply experimental scripting.", 5),
                ("Peer-to-peer decentralized networks with zero central authority.", 4)
            ]
        }
    ]

    total_score = 0
    
    for q in questions:
        print(CYAN + q["text"] + RESET)
        for idx, opt in enumerate(q["options"]):
            print(f"  {WHITE}{idx + 1}){RESET} {opt[0]}")
        
        while True:
            choice = input(YELLOW + "Your choice (1-4): " + RESET).strip()
            if choice in ["1", "2", "3", "4"]:
                total_score += q["options"][int(choice) - 1][1]
                print(WHITE + "-" * 30 + RESET)
                break
            print(RED + "Invalid input. The party requires a valid response (1-4)." + RESET)

    # Archetype Definitions
    archetypes = {
        "ZEUS": {
            "title": "The Central Planner (Olympian Establishment)",
            "art": "    .   ,  \n  \\ | /    \n- - * - -  \n  / | \\    \n    '   '  ",
            "desc": "You view society as a monolithic codebase that requires strict, top-down regulation, absolute optimization, and rigid infrastructure control.",
            "base_solidarity": 65
        },
        "ATHENA": {
            "title": "The Vanguard Architect (Olympian Establishment)",
            "art": "   /\\_/\\   \n  ( o.o )  \n   > ^ <   \n  /     \\  ",
            "desc": "You are a theory-driven strategist. You build scalable frameworks, optimize resource allocation, and view revolution as a calculated, precise science.",
            "base_solidarity": 88
        },
        "HADES": {
            "title": "The Underground Proletarian (Anti-Hero Rebel)",
            "art": "  |  |  |  \n  |  |  |  \n  \\__|_/   \n     |     ",
            "desc": "You run the backend database of the underworld. Alienated from the glitz of Olympus, you manage raw material reality where the real surplus value is extracted.",
            "base_solidarity": 78
        },
        "PROMETHEUS": {
            "title": "The Open-Source Insurgent (Anti-Hero Rebel)",
            "art": "    (  )   \n   (    )  \n  (======) \n   \\    /  \n    \\__/   ",
            "desc": "The ultimate anti-hero. You stole the proprietary fire from corporate deities to distribute open-source logic freely to the global working-class masses.",
            "base_solidarity": 98
        },
        "DIONYSUS": {
            "title": "The Decentralized Radical (Anti-Hero Rebel)",
            "art": "   _   _   \n  ( )_( )  \n   \\   /   \n    \\_/    \n    (_)    ",
            "desc": "You smash traditional hierarchies through chaotic solidarity. You believe in tearing down the bourgeois state through collective, uninhibited joy and direct action.",
            "base_solidarity": 82
        }
    }

    # Evaluate Score
    if total_score <= 7:
        god_key = "ZEUS"
    elif total_score <= 12:
        god_key = "ATHENA"
    elif total_score <= 16:
        god_key = "HADES"
    elif total_score <= 21:
        god_key = "PROMETHEUS"
    else:
        god_key = "DIONYSUS"

    result = archetypes[god_key]
    solidarity_score = min(100, max(0, result["base_solidarity"] + (total_score % 4)))

    # Terminal Output
    print("\n" + RED + "="*55 + RESET)
    print(MAGENTA + "                LABOR MATRIX SYNTHESIS                   " + RESET)
    print(RED + "="*55 + RESET)
    print(f"{WHITE}Comrade {GREEN}{comrade_name}{WHITE}, you align with:{RESET} {GREEN}{god_key}{RESET}")
    print(f"{WHITE}Proletarian Title:{RESET}      {CYAN}{result['title']}{RESET}\n")
    print(YELLOW + "DIVINE SYMBOL:" + RESET)
    print(MAGENTA + result['art'] + RESET)
    print(f"\n{YELLOW}Dialectical Analysis:{RESET}\n{WHITE}{result['desc']}{RESET}")
    print(WHITE + "-" * 55 + RESET)
    print(f"{YELLOW}SOLIDARITY SCORE:{RESET} {GREEN}{solidarity_score}%{RESET}")
    
    status_msg = ""
    if solidarity_score >= 90:
        status_msg = "Pure Vanguard Material. The vanguard party trusts your commits."
    elif solidarity_score >= 75:
        status_msg = "Reliable Left-Wing Sysadmin. Your code actively serves the collective."
    else:
        status_msg = "Reformist Revisionist. Watch out for bourgeois deviations in your logic."
        
    print(f"{WHITE}Status:{RESET} {CYAN}{status_msg}{RESET}")
    print(RED + "="*55 + RESET)
    print(WHITE + "Keep seizing the means of computation. Class dismissed.\n" + RESET)

    # Markdown Export Option
    export_choice = input(YELLOW + "Would you like to export this result as a Markdown Manifesto? (y/n): " + RESET).strip().lower()
    if export_choice == 'y':
        file_name = "dialectical_manifest.md"
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(f"# DIALECTICAL MANIFESTO OF COMRADE {comrade_name.upper()}\n\n")
            f.write(f"## IDENTIFIED ARCHETYPE: {god_key}\n")
            f.write(f"**Proletarian Title:** {result['title']}\n\n")
            f.write("### DIVINE SYMBOL\n")
            f.write("```\n")
            f.write(result['art'] + "\n")
            f.write("```\n\n")
            f.write("### DIALECTICAL ANALYSIS\n")
            f.write(f"{result['desc']}\n\n")
            f.write(f"**SOLIDARITY SCORE:** {solidarity_score}%\n")
            f.write(f"**VANGUARD STATUS:** {status_msg}\n\n")
            f.write("---\n")
            f.write("*Keep seizing the means of computation. Class dismissed.*\n")
        print(GREEN + f"\nSuccess! Manifesto exported to '{file_name}'." + RESET)
    else:
        print(WHITE + "\nManifesto skipped. The revolution moves forward regardless." + RESET)

if __name__ == "__main__":
    run_dialectical_quiz()
