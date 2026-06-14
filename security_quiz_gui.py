#!/usr/bin/env python3
"""
🔐 Random Security Quiz App
A terminal-based cybersecurity quiz with randomized questions and scoring.
"""

import random
import time
import sys

# ─────────────────────────────────────────────
#  QUESTION BANK
# ─────────────────────────────────────────────
QUESTIONS = [
    {
        "question": "What does 'SQL Injection' allow an attacker to do?",
        "options": [
            "A) Crash the web server",
            "B) Execute arbitrary SQL commands on the database",
            "C) Intercept network traffic",
            "D) Crack password hashes"
        ],
        "answer": "B",
        "explanation": "SQL Injection lets attackers manipulate database queries by injecting malicious SQL code."
    },
    {
        "question": "Which protocol is used to securely transfer files over SSH?",
        "options": [
            "A) FTP",
            "B) TFTP",
            "C) SFTP",
            "D) HTTP"
        ],
        "answer": "C",
        "explanation": "SFTP (SSH File Transfer Protocol) encrypts both commands and data using SSH."
    },
    {
        "question": "What is a 'Zero-Day' vulnerability?",
        "options": [
            "A) A vulnerability with no patch available yet",
            "B) A bug that causes system to reboot every day",
            "C) A malware that activates at midnight",
            "D) A denial-of-service attack"
        ],
        "answer": "A",
        "explanation": "A Zero-Day is a flaw unknown to the vendor, meaning 'zero days' have passed to fix it."
    },
    {
        "question": "Which type of attack involves sending excessive traffic to crash a service?",
        "options": [
            "A) Phishing",
            "B) Man-in-the-Middle",
            "C) Denial of Service (DoS)",
            "D) SQL Injection"
        ],
        "answer": "C",
        "explanation": "A DoS attack floods a target with traffic to make it unavailable to users."
    },
    {
        "question": "What is the purpose of a firewall?",
        "options": [
            "A) Speed up internet connection",
            "B) Monitor and control incoming/outgoing network traffic",
            "C) Encrypt hard disk data",
            "D) Scan for viruses in files"
        ],
        "answer": "B",
        "explanation": "A firewall enforces security rules on network traffic based on a defined rule set."
    },
    {
        "question": "What does 'HTTPS' provide over 'HTTP'?",
        "options": [
            "A) Faster page loading",
            "B) Encrypted communication using TLS/SSL",
            "C) Larger file transfer support",
            "D) Better SEO ranking only"
        ],
        "answer": "B",
        "explanation": "HTTPS uses TLS/SSL to encrypt data between browser and server, ensuring confidentiality."
    },
    {
        "question": "Which hashing algorithm is considered BROKEN and should NOT be used for passwords?",
        "options": [
            "A) bcrypt",
            "B) SHA-256",
            "C) MD5",
            "D) Argon2"
        ],
        "answer": "C",
        "explanation": "MD5 is cryptographically broken — it's vulnerable to collision attacks and rainbow tables."
    },
    {
        "question": "What is 'Phishing'?",
        "options": [
            "A) A network scanning technique",
            "B) Tricking users into revealing sensitive info via fake communications",
            "C) Brute-forcing login pages",
            "D) Exploiting buffer overflow vulnerabilities"
        ],
        "answer": "B",
        "explanation": "Phishing uses deceptive emails/sites to steal credentials, credit cards, or personal data."
    },
    {
        "question": "What does 'MFA' stand for in cybersecurity?",
        "options": [
            "A) Malware Free Authentication",
            "B) Multi-Factor Authentication",
            "C) Managed Firewall Access",
            "D) Multiple File Authorization"
        ],
        "answer": "B",
        "explanation": "MFA requires two or more verification factors, making unauthorized access much harder."
    },
    {
        "question": "What is a 'Man-in-the-Middle' (MitM) attack?",
        "options": [
            "A) Attacker physically sits between two computers",
            "B) Attacker secretly intercepts and relays communication between two parties",
            "C) Attacker sends spam emails to both parties",
            "D) Attacker installs malware on a middle server"
        ],
        "answer": "B",
        "explanation": "In a MitM attack, the attacker secretly relays and possibly alters communication."
    },
    {
        "question": "Which command in Linux shows open network ports?",
        "options": [
            "A) ls -la",
            "B) netstat -tuln",
            "C) chmod 777",
            "D) ping localhost"
        ],
        "answer": "B",
        "explanation": "`netstat -tuln` lists all listening TCP/UDP ports without resolving hostnames."
    },
    {
        "question": "What is 'Ransomware'?",
        "options": [
            "A) Software that monitors employee activity",
            "B) Malware that encrypts files and demands payment for decryption",
            "C) A type of antivirus tool",
            "D) Software used to bypass firewalls"
        ],
        "answer": "B",
        "explanation": "Ransomware encrypts victim's data and demands a ransom (often in crypto) for the decryption key."
    },
    {
        "question": "What is the principle of 'Least Privilege'?",
        "options": [
            "A) Give admin rights to all users for efficiency",
            "B) Users/systems should only have the minimum access needed",
            "C) Disable all user accounts by default",
            "D) Limit internet speed for non-admin users"
        ],
        "answer": "B",
        "explanation": "Least Privilege reduces attack surface by limiting what each user/process can access."
    },
    {
        "question": "Which tool is commonly used for network packet analysis?",
        "options": [
            "A) Nmap",
            "B) Metasploit",
            "C) Wireshark",
            "D) John the Ripper"
        ],
        "answer": "C",
        "explanation": "Wireshark is a network protocol analyzer that captures and inspects packets in real time."
    },
    {
        "question": "What does 'CIA Triad' stand for in information security?",
        "options": [
            "A) Cyber Intelligence Agency",
            "B) Confidentiality, Integrity, Availability",
            "C) Control, Inspect, Authorize",
            "D) Central Information Access"
        ],
        "answer": "B",
        "explanation": "The CIA Triad is the core model of information security: keep data secret, accurate, and accessible."
    },
]

# ─────────────────────────────────────────────
#  COLORS (ANSI)
# ─────────────────────────────────────────────
class Color:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    CYAN    = "\033[96m"
    MAGENTA = "\033[95m"
    WHITE   = "\033[97m"
    DIM     = "\033[2m"

def c(text, *colors):
    return "".join(colors) + text + Color.RESET

# ─────────────────────────────────────────────
#  UI HELPERS
# ─────────────────────────────────────────────
def clear_line():
    print("\r" + " " * 60 + "\r", end="")

def banner():
    print(c("""
╔══════════════════════════════════════════════════════╗
║       🔐  RANDOM SECURITY QUIZ APP  🔐               ║
║         Test Your Cybersecurity Knowledge!           ║
╚══════════════════════════════════════════════════════╝
""", Color.CYAN, Color.BOLD))

def separator():
    print(c("─" * 56, Color.DIM))

def loading_bar(label="Loading", duration=0.8):
    bar = ""
    steps = 20
    for i in range(steps + 1):
        filled = "█" * i + "░" * (steps - i)
        percent = int((i / steps) * 100)
        print(f"\r  {label}: [{c(filled, Color.CYAN)}] {percent}%", end="", flush=True)
        time.sleep(duration / steps)
    print()

# ─────────────────────────────────────────────
#  QUIZ LOGIC
# ─────────────────────────────────────────────
def get_num_questions():
    max_q = len(QUESTIONS)
    while True:
        try:
            print(c(f"\n  How many questions? (1–{max_q}) : ", Color.YELLOW), end="")
            n = int(input().strip())
            if 1 <= n <= max_q:
                return n
            print(c(f"  ⚠  Enter a number between 1 and {max_q}.", Color.RED))
        except ValueError:
            print(c("  ⚠  Please enter a valid number.", Color.RED))

def ask_question(idx, total, q_data):
    separator()
    print(c(f"\n  Question {idx}/{total}", Color.MAGENTA, Color.BOLD))
    print(c(f"  {q_data['question']}\n", Color.WHITE, Color.BOLD))
    for opt in q_data["options"]:
        print(c(f"    {opt}", Color.WHITE))
    print()

    valid = {"A", "B", "C", "D"}
    while True:
        print(c("  Your answer (A/B/C/D): ", Color.YELLOW), end="")
        ans = input().strip().upper()
        if ans in valid:
            return ans
        print(c("  ⚠  Enter A, B, C, or D.", Color.RED))

def evaluate(user_ans, correct_ans, explanation):
    if user_ans == correct_ans:
        print(c("\n  ✅  CORRECT!", Color.GREEN, Color.BOLD))
        result = True
    else:
        print(c(f"\n  ❌  WRONG! Correct answer: {correct_ans}", Color.RED, Color.BOLD))
        result = False
    print(c(f"  💡 {explanation}\n", Color.DIM))
    time.sleep(0.5)
    return result

def show_result(score, total):
    separator()
    pct = (score / total) * 100
    print(c(f"\n  📊  QUIZ COMPLETE!", Color.CYAN, Color.BOLD))
    print(c(f"\n  Score: {score} / {total}  ({pct:.1f}%)\n", Color.WHITE, Color.BOLD))

    if pct == 100:
        grade = c("🏆  PERFECT SCORE! You're a Security Expert!", Color.GREEN, Color.BOLD)
    elif pct >= 80:
        grade = c("🥇  Excellent! Strong security knowledge.", Color.GREEN)
    elif pct >= 60:
        grade = c("🥈  Good effort! Keep studying.", Color.YELLOW)
    elif pct >= 40:
        grade = c("🥉  Fair. Review the basics again.", Color.YELLOW)
    else:
        grade = c("📚  Needs improvement. Keep learning!", Color.RED)

    print(f"  {grade}\n")
    separator()

def play_again():
    print(c("\n  Play again? (y/n): ", Color.CYAN), end="")
    return input().strip().lower() == "y"

# ─────────────────────────────────────────────
#  MAIN
# ─────────────────────────────────────────────
def main():
    banner()
    print(c("  Welcome! This quiz covers core cybersecurity concepts.\n", Color.DIM))

    while True:
        num_q = get_num_questions()
        selected = random.sample(QUESTIONS, num_q)

        print()
        loading_bar("Preparing questions")
        print()

        score = 0
        for i, q in enumerate(selected, 1):
            user_ans = ask_question(i, num_q, q)
            if evaluate(user_ans, q["answer"], q["explanation"]):
                score += 1

        show_result(score, num_q)

        if not play_again():
            print(c("\n  Thanks for playing! Stay secure. 🔒\n", Color.CYAN, Color.BOLD))
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(c("\n\n  Quiz interrupted. Goodbye! 👋\n", Color.YELLOW))
        sys.exit(0)
