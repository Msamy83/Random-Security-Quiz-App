# 🔐 Security Quiz Pro

A multi-platform cybersecurity quiz application available both as a terminal interface and modern web application. This app helps users test and improve their cybersecurity knowledge through randomized questions and an advanced scoring system.

## ✨ Features

### 🎯 Core Functionality
- **15 Comprehensive Questions**: SQL Injection, Network Security, Attack Vectors, Security Tools
- **Randomized Quizzes**: Different questions every session
- **Flexible Length**: Choose 1-15 questions per quiz
- **Multiple Choice**: A, B, C, D format questions
- **Immediate Feedback**: Correct/Wrong answers with detailed explanations

### 🖥️ Terminal Version (Python)
- **ANSI Colorful Interface**: Attractive colors in terminal
- **Text-based Animations**: Loading bars and progress indicators
- **Cross-platform**: Windows, macOS, Linux support
- **Lightweight**: Minimal resource usage

### 🌐 Web Version (HTML/CSS/JS)
- **Modern UI Design**: Glass-morphism and gradient backgrounds
- **Advanced Animations**: 
  - Smooth screen transitions
  - Floating particle effects
  - Pulse/shake answer feedback
  - Bouncing result badges
- **Interactive Elements**:
  - Range slider for question selection
  - Click-based answer selection
  - Animated progress bar with moving stripes
- **Responsive Design**: Mobile and desktop friendly

### 📚 Educational Value
- **Instant Learning**: Detailed explanation for every question
- **Score Tracking**: Real-time performance monitoring
- **Repeat Practice**: Play again option for continuous learning

## 🚀 Getting Started

### Prerequisites
**Terminal Version:**
- Python 3.x installed on your system
- Terminal/Command Prompt access

**Web Version:**
- Modern web browser (Chrome, Firefox, Safari, Edge)
- No installation required!

### Installation & Usage

#### 🖥️ Terminal Version
1. **Download the application:**
   ```bash
   git clone <repository-url>
   cd security-quiz-pro
   ```

2. **Run the Python quiz:**
   ```bash
   python security_quiz_gui.py
   ```

3. **Follow the prompts:**
   - Choose number of questions (1-15)
   - Answer each question (A/B/C/D)
   - Review your score and explanations
   - Play again or exit

#### 🌐 Web Version
1. **Simply open the file:**
   - Double-click `index.html` file
   - Or drag and drop into your browser
   - Or run: `start index.html` (Windows) / `open index.html` (macOS)

2. **Enjoy the modern interface:**
   - Use the slider to select questions (1-15)
   - Click "Start Quiz 🚀" to begin
   - Click on your answers (A/B/C/D)
   - Watch animated feedback and explanations
   - Get your final score with performance grade

## 📖 How to Use

### Starting the Quiz (Terminal Version)
```
╔══════════════════════════════════════════════════════╗
║       🔐  SECURITY QUIZ PRO  🔐                      ║
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
**Dual Platform Design:**
- **Terminal Version**: Self-contained Python application
- **Web Version**: Single HTML file with embedded CSS/JS
- **No External Dependencies**: Pure vanilla implementations
- **Cross-Platform**: Works across all major platforms
- **Memory Efficient**: Lightweight with minimal resource usage

### Code Structure

#### 🖥️ Terminal Version (security_quiz_gui.py)
```
security_quiz_gui.py
├── Question Bank (15 questions with explanations)
├── Color Management (ANSI color codes)
├── UI Helpers (animations, formatting)
├── Quiz Logic (question flow, scoring)
└── Main Application (user interaction)
```

#### 🌐 Web Version (index.html)
```
index.html
├── HTML Structure (semantic markup)
├── CSS Styling (animations, responsive design)
├── JavaScript Logic (quiz functionality)
├── Question Bank (same 15 questions)
├── Animation System (particles, transitions)
└── Interactive UI (sliders, buttons, feedback)
```

### Key Components

#### Terminal Version
- **QUESTIONS**: Dictionary containing all quiz questions, options, answers, explanations
- **Color Class**: ANSI color codes for terminal styling
- **Quiz Functions**: Question presentation, answer validation, scoring
- **UI Functions**: Banner, loading bars, result display

#### Web Version
- **HTML Structure**: Semantic layout with multiple screens
- **CSS Animations**: Keyframes for smooth transitions and effects
- **JavaScript State Management**: Quiz flow and user interaction
- **Responsive Design**: Mobile-first approach with media queries
- **Visual Effects**: Particle system, gradient backgrounds, hover states

## 🎯 Learning Objectives

Through this quiz app, users will learn:

1. **Fundamental Security Concepts**: CIA Triad, Zero-Day vulnerabilities
2. **Attack Methods**: SQL Injection, Phishing, DoS attacks
3. **Security Protocols**: HTTPS, SFTP, SSL/TLS
4. **Security Tools**: Firewalls, Wireshark, Linux commands
5. **Best Practices**: MFA, Least Privilege, Secure coding
6. **Threat Landscape**: Ransomware, Man-in-the-Middle attacks

## 🔧 Customization

### Adding New Questions (Python Version)
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

### Adding New Questions (Web Version)
```javascript
{
    question: "Your new security question?",
    options: [
        "First option",
        "Second option", 
        "Third option",
        "Fourth option"
    ],
    correct: 1, // Index of correct answer (0-based)
    explanation: "Detailed explanation of why the second option is correct."
}
```

### Modifying Colors (Terminal Version)
```python
class Color:
    RESET   = "\033[0m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    # Add your custom colors here
```

## 🤝 Contributing

Contributions are welcome to improve this project:

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
- Multi-language support
- Dark/Light theme toggle

## 📋 Requirements

### Terminal Version
- **Python Version**: 3.6 or higher
- **Terminal**: ANSI color support preferred
- **OS**: Windows, macOS, Linux compatible
- **Memory**: Minimal requirements (< 10MB)

### Web Version
- **Browser**: Modern web browsers (Chrome 60+, Firefox 60+, Safari 12+, Edge 79+)
- **JavaScript**: ES6+ support required
- **Storage**: < 1MB file size
- **Network**: No internet connection required

## 🐛 Known Issues & Limitations

### Terminal Version
- Terminal must support ANSI colors for best experience
- Single session only (no persistent score storage)
- Questions are hardcoded (no external file loading)

### Web Version
- Requires JavaScript enabled
- No server-side storage (client-side only)
- Performance depends on browser capabilities

## 📞 Support & Feedback

If you encounter any issues or have suggestions:

- Create an issue in the GitHub repository
- Check existing documentation
- Review the code comments for understanding
- Submit feature requests through GitHub Issues

## 🔒 Security Considerations

This educational tool:
- Contains no sensitive data collection
- Runs entirely offline (no network requests)
- Uses no external dependencies that could pose security risks
- Follows secure coding practices for educational purposes

## 📄 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute for educational purposes.

## 🙏 Acknowledgments

- **Cybersecurity Community**: For knowledge sharing and educational resources
- **Python Community**: For excellent documentation and best practices
- **Web Standards**: For modern browser capabilities enabling rich interactive experiences
- **Educational Institutions**: For promoting cybersecurity awareness

## 🌟 Project Stats

- **Question Bank**: 15 carefully curated questions
- **Code Quality**: Well-documented, modular design
- **Accessibility**: Cross-platform compatibility
- **Learning Focus**: Practical cybersecurity knowledge
- **User Experience**: Both terminal and web interfaces

---

**Happy Learning! Stay Secure! 🔒**

*Made with ❤️ for the cybersecurity community*

## 📈 Roadmap

### Version 2.1 (Planned)
- [ ] Add more questions (target: 50+ questions)
- [ ] Implement difficulty levels (Beginner, Intermediate, Advanced)
- [ ] Add timer mode for timed challenges
- [ ] Question categories for focused learning

### Version 3.0 (Future)
- [ ] Multi-language support
- [ ] Progress tracking and analytics
- [ ] Online leaderboard
- [ ] Custom quiz creation
- [ ] Mobile app version