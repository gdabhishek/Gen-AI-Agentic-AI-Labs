# Setup Guide

This guide will help you set up Cursor IDE, clone the repository, and configure a Python virtual environment.

## Table of Contents
1. [Installing Cursor IDE](#installing-cursor-ide)
2. [Cloning the Repository](#cloning-the-repository)
3. [Setting Up Python Virtual Environment](#setting-up-python-virtual-environment)

---

## Installing Cursor IDE

### For Linux

1. **Download Cursor:**
   - Visit [Cursor's official website](https://cursor.sh/)
   - Download the Linux version (`.deb` for Debian/Ubuntu or `.AppImage` for other distributions)

2. **Install Cursor:**
   
   **For Debian/Ubuntu (.deb package):**
   ```bash
   # Navigate to your Downloads folder
   cd ~/Downloads
   
   # Install the .deb package
   sudo dpkg -i cursor_*.deb
   
   # If there are dependency issues, fix them with:
   sudo apt-get install -f
   ```
   
   **For AppImage:**
   ```bash
   # Make the AppImage executable
   chmod +x cursor-*.AppImage
   
   # Run Cursor
   ./cursor-*.AppImage
   ```

3. **Launch Cursor:**
   - You can launch Cursor from your applications menu, or
   - Run `cursor` from the terminal (if installed via .deb)

### For macOS

1. **Download Cursor:**
   - Visit [Cursor's official website](https://cursor.sh/)
   - Download the macOS version (`.dmg` file)

2. **Install Cursor:**
   - Open the downloaded `.dmg` file
   - Drag Cursor to your Applications folder

3. **Launch Cursor:**
   - Open Cursor from Applications or Spotlight

### For Windows

1. **Download Cursor:**
   - Visit [Cursor's official website](https://cursor.sh/)
   - Download the Windows version (`.exe` installer)

2. **Install Cursor:**
   - Run the installer and follow the setup wizard
   - Choose installation location and options

3. **Launch Cursor:**
   - Open Cursor from Start Menu or Desktop shortcut

---

## Cloning the Repository

### Prerequisites

Make sure Git is installed:

```bash
# Check Git version
git --version

# If Git is not installed:
# Ubuntu/Debian:
sudo apt-get install git

# macOS:
brew install git

# Windows: Download from https://git-scm.com/
```

### Clone the Repo

1. **Navigate to your desired parent directory:**
   ```bash
   # Example: Navigate to your Documents or a specific location
   cd ~/Documents
   ```

2. **Clone the repository:**
   ```bash
   git clone https://github.com/gdabhishek/Gen-AI-Agentic-AI-Labs.git
   ```

3. **Navigate into the project folder:**
   ```bash
   cd Gen-AI-Agentic-AI-Labs
   ```

## Setting Up Python Virtual Environment

### Prerequisites

Make sure Python 3.11 or higher is installed:

```bash
# Check Python version
python3 --version

# If Python is not installed, install it:
# Ubuntu/Debian:
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# macOS (using Homebrew):
brew install python3

# Windows: Download from python.org
```

### Creating Virtual Environment

1. **Navigate to the project directory** (the cloned repo):
   ```bash
   cd Gen-AI-Agentic-AI-Labs
   
   # You should now be in: Gen-AI-Agentic-AI-Labs/
   ```

2. **Create the virtual environment:**
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # This creates a 'venv' folder in your current directory
   ```

3. **Activate the virtual environment:**
   
   **On Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```
   
   **On Windows:**
   ```bash
   venv\Scripts\activate
   ```
   
   **Note:** When activated, you'll see `(venv)` at the beginning of your terminal prompt.

4. **Verify the virtual environment is active:**
   ```bash
   # Check Python location (should point to venv)
   which python3  # Linux/macOS
   where python   # Windows
   
   # Check pip location
   which pip      # Linux/macOS
   where pip      # Windows
   ```

5. **Upgrade pip (recommended):**
   ```bash
   pip install --upgrade pip
   ```

### Deactivating Virtual Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```
---

## Quick Setup Checklist

- [ ] Cursor IDE installed and launched
- [ ] Repository cloned (`Gen-AI-Agentic-AI-Labs`)
- [ ] Python 3.11+ installed and verified
- [ ] Virtual environment created (`venv` folder in project directory)

---

## Troubleshooting

### Virtual Environment Not Activating

**Issue:** `source venv/bin/activate` doesn't work

**Solution:**
```bash
# Make sure you're in the correct directory (cloned repo)
pwd  # Should show: .../Gen-AI-Agentic-AI-Labs

# Check if venv exists
ls -la venv/

# Try using full path
source ./venv/bin/activate
```

### Python Interpreter Not Found in Cursor

**Issue:** Cursor can't find the Python interpreter

**Solution:**
1. Make sure the virtual environment is created
2. Use Command Palette (`Ctrl+Shift+P`) → `Python: Select Interpreter`
3. Manually browse to: `./venv/bin/python` (or `.\venv\Scripts\python.exe` on Windows)

### Terminal Doesn't Show (venv)

**Issue:** Terminal doesn't show virtual environment indicator

**Solution:**
- Manually activate: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
- Check that you're in the correct directory
- Verify the venv folder exists

---



## Additional Resources

- [Cursor Documentation](https://cursor.sh/docs)
- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [VS Code Python Extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) (Cursor is based on VS Code)

