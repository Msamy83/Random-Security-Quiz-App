# 🔐 Random Security Quiz App

ஒரு terminal-based cybersecurity quiz application இது randomized questions மற்றும் scoring system உடன் வருகிறது. இந்த app cybersecurity concepts-ஐ test செய்து improve செய்ய help செய்கிறது.

## ✨ Features

### 🎯 Core Functionality
- **15 Comprehensive Questions**: SQL Injection, Network Security, Attack Vectors, Security Tools
- **Randomized Quizzes**: ஒவ்வொரு session-லும் different questions
- **Flexible Length**: 1-15 questions வரை choose செய்யலாம்
- **Multiple Choice**: A, B, C, D format-ல் questions
- **Immediate Feedback**: Correct/Wrong answers உடன் detailed explanations

### 🎨 Visual Experience
- **Colorful Interface**: ANSI colors உபயோகித்து attractive terminal UI
- **Loading Animations**: Progress bars மற்றும் smooth transitions
- **Performance Grading**: Score-based feedback system
- **Clean Layout**: Professional மற்றும் readable formatting

### 📚 Educational Value
- **Instant Learning**: ஒவ்வொரு question-க்கும் detailed explanation
- **Score Tracking**: Real-time performance monitoring
- **Repeat Practice**: Play again option continuous learning-க்கு

## 🚀 Getting Started

### Prerequisites
- Python 3.x installed on your system
- Terminal/Command Prompt access

### Installation & Usage

1. **Download the application:**
   ```bash
   git clone <repository-url>
   cd security-quiz-app
   ```

2. **Run the quiz:**
   ```bash
   python security_quiz_gui.py
   ```

3. **Follow the prompts:**
   - Choose number of questions (1-15)
   - Answer each question (A/B/C/D)
   - Review your score and explanations
   - Play again or exit

## 📖 How to Use

### Starting the Quiz
```
╔══════════════════════════════════════════════════════╗
║       🔐  RANDOM SECURITY QUIZ APP  🔐               ║
║         Test Your Cybersecurity Knowledge!           ║
╚══════════════════════════════════════════════════════╝

  How many questions? (1–15) : 5
```

### Answering Questions
```
────────────────────────────────────────────────────────

  Question 1/5
  What does 'SQL Injection' allow an attacker to do?

    A) Crash the web server
    B) Execute arbitrary SQL commands on the database
    C) Intercept network traffic
    D) Crack password hashes

  Your answer (A/B/C/D): B
```

### Getting Results
```
  📊  QUIZ COMPLETE!

  Score: 4 / 5  (80.0%)

  🥇  Excellent! Strong security knowledge.
```

## 🎓 Question Topics Covered

| Topic | Examples |
|-------|----------|
| **Web Security** | SQL Injection, HTTPS vs HTTP |
| **Network Security** | SFTP, Firewalls, Network Analysis |
| **Attack Vectors** | Phishing, DoS, Man-in-the-Middle |
| **Malware** | Ransomware, Zero-Day vulnerabilities |
| **Security Practices** | MFA, Least Privilege, CIA Triad |
| **Tools & Commands** | Wireshark, netstat, Linux security |
| **Cryptography** | Hash algorithms, Encryption practices |

## 🏆 Scoring System

| Score Range | Grade | Description |
|-------------|-------|-------------|
| 100% | 🏆 Perfect Score | Security Expert! |
| 80-99% | 🥇 Excellent | Strong security knowledge |
| 60-79% | 🥈 Good | Keep studying |
| 40-59% | 🥉 Fair | Review the basics |
| <40% | 📚 Needs Improvement | Keep learning! |

## 🛠️ Technical Details

### Architecture
- **Single File Design**: Self-contained Python application
- **No External Dependencies**: Uses only Python standard library
- **Cross-Platform**: Works on Windows, macOS, Linux terminals
- **Memory Efficient**: Lightweight with minimal resource usage

### Code Structure
```
security_quiz_gui.py
├── Question Bank (15 questions with explanations)
├── Color Management (ANSI color codes)
├── UI Helpers (animations, formatting)
├── Quiz Logic (question flow, scoring)
└── Main Application (user interaction)
```

### Key Components
- **QUESTIONS**: Dictionary containing all quiz questions, options, answers, explanations
- **Color Class**: ANSI color codes for terminal styling
- **Quiz Functions**: Question presentation, answer validation, scoring
- **UI Functions**: Banner, loading bars, result display

## 🎯 Learning Objectives

இந்த quiz app-ன் மூலம் நீங்கள் கற்றுக்கொள்ளும் விஷயங்கள்:

1. **Fundamental Security Concepts**: CIA Triad, Zero-Day vulnerabilities
2. **Attack Methods**: SQL Injection, Phishing, DoS attacks
3. **Security Protocols**: HTTPS, SFTP, SSL/TLS
4. **Security Tools**: Firewalls, Wireshark, Linux commands
5. **Best Practices**: MFA, Least Privilege, Secure coding
6. **Threat Landscape**: Ransomware, Man-in-the-Middle attacks

## 🔧 Customization

### Adding New Questions
```python
{
    "question": "Your new security question?",
    "options": [
        "A) First option",
        "B) Second option", 
        "C) Third option",
        "D) Fourth option"
    ],
    "answer": "B",
    "explanation": "Detailed explanation of why B is correct."
}
```

### Modifying Colors
```python
class Color:
    RESET   = "\033[0m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    # Add your custom colors here
```

## 🤝 Contributing

इस project को improve करने के लिए contributions welcome हैं:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-questions`)
3. Add your questions or improvements
4. Commit changes (`git commit -am 'Add new security questions'`)
5. Push to branch (`git push origin feature/new-questions`)
6. Create a Pull Request

### Contribution Ideas
- Add more cybersecurity questions
- Implement difficulty levels
- Add timer functionality
- Create question categories
- Improve visual design
- Add progress tracking

## 📋 Requirements

- **Python Version**: 3.6 or higher
- **Terminal**: ANSI color support preferred
- **OS**: Windows, macOS, Linux compatible
- **Memory**: Minimal requirements (< 10MB)

## 🐛 Known Issues & Limitations

- Terminal must support ANSI colors for best experience
- Single session only (no persistent score storage)
- Questions are hardcoded (no external file loading)
- No network connectivity required

## 📞 Support & Feedback

यदि आपको कोई issues आते हैं या suggestions हैं:

- Create an issue in the GitHub repository
- Check existing documentation
- Review the code comments for understanding

## 📄 License

This project is open source. Feel free to use, modify, and distribute for educational purposes.

## 🙏 Acknowledgments

- Cybersecurity community for knowledge sharing
- Python community for excellent documentation
- Terminal color standards for visual enhancement

---

**Happy Learning! Stay Secure! 🔒**

*Made with ❤️ for the cybersecurity community*