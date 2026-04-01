# ⌨️ GLOBAL KEYLOGGER v1.0 - Stealth Keystroke Logger


## 📋 Overview

**GLOBAL KEYLOGGER** is a **zero-dependency keystroke logger** designed for **authorized security assessments**. Captures **ALL keystrokes** system-wide and saves to `Desktop/my_global_notes.txt`.

**Key Features:**
- ✅ **Global hotkey capture** (all apps)
- ✅ **Stealth operation** (no windows/popups)
- ✅ **Auto-save every 2 seconds**
- ✅ **ESC safe exit**
- ✅ **Handles spaces, Enter, Backspace**
- ✅ **Pure Python + keyboard lib**

> **⚠️ CRITICAL: AUTHORIZED USE ONLY ⚠️**

## 🎓 Educational Purposes Only

```
This code is for EDUCATIONAL PURPOSES and created by Dairon
I have permission and am authorized to perform this pentest
```

## 🛠️ System Requirements

| Requirement | Version |
|-------------|---------|
| **OS** | Windows 10/11 (x64) |
| **Python** | 3.7+ |
| **Dependencies** | `keyboard` (`pip install keyboard`) |
| **Permissions** | Administrator **REQUIRED** |

## 🚀 Installation (1 Minute)

```bash
# 1. Save as keylogger.py
# 2. Install single dependency:
pip install keyboard

# 3. Run as Administrator:
python keylogger.py
```

## 🎮 Usage Guide

### Quick Start
```bash
# Terminal shows:
Running... Press ESC to stop.
# Type anywhere → keystrokes auto-save to Desktop/my_global_notes.txt
# Press ESC to safely exit
```

### Live Demo Flow
```
1. python keylogger.py (Run as Admin)
2. Open Notepad, Chrome, anywhere
3. Type: "Hello World! This is captured."
4. Check: Desktop/my_global_notes.txt
5. Press ESC → Clean shutdown ✅
```

## 📁 Output File

```
C:\Users\%USERNAME%\Desktop\my_global_notes.txt
```

**Sample captured content:**
```
Hello World!
My Gmail password: supersecret123
Bank login: user123 pass456
https://bank.com/transfer?amount=5000
```

## ⚙️ Configuration

### Easy Customization

```python
# === QUICK EDITS ===

# Change output file (line 5)
filename = os.path.join(desktop, "credentials.txt")

# Change hotkey (line 23)
if name == "delete":  # ESC → Delete key

# Change auto-save interval (line 40)
time.sleep(5)  # 2 → 5 seconds

# Silent mode (hide console)
# Add: pythonw keylogger.py
```

### Advanced Features

| Feature | Code | Effect |
|---------|------|---------|
| **Silent Mode** | `pythonw keylogger.py` | No console window |
| **Custom Path** | Edit `filename` | Any folder |
| **Custom Exit** | Change `"esc"` | Any hotkey |
| **Live Buffer** | Print `buffer` | Real-time console |

## 🛡️ Safety Controls

### Emergency Exit
```
✅ ESC key = IMMEDIATE SAFE STOP
✅ Final buffer auto-saves
✅ Clean process exit
✅ No data loss
```

### Persistence Options

```python
# Startup folder (manual)
# Copy to: shell:startup

# Registry (advanced)
# HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

## 🔍 Pentest Scenarios

| Scenario | Use Case |
|----------|----------|
| **Credential Harvesting** | Password capture demo |
| **User Profiling** | Application usage analysis |
| **Social Engineering** | Phishing credential validation |
| **Endpoint Assessment** | Keylogger detection testing |
| **Blue Team Training** | Detection/response exercise |

## 📊 Technical Details

| Component | Implementation | Detection Vectors |
|-----------|----------------|------------------|
| **Hook** | `keyboard.on_press()` | Hook monitoring |
| **Capture** | Global event handler | API monitoring |
| **Storage** | Append to file | File creation |
| **Stealth** | No UI/process hiding | Console window |
| **Persistence** | Manual startup | Registry scanning |

## 🧪 Testing Commands

```bash
# Test capture:
echo "test123" > test.txt
# Type in any app → verify in my_global_notes.txt

# Admin check:
net session >nul 2>&1
if %errorLevel% == 0 (echo Admin OK) else (echo Run as Admin!)
```

## 🔒 Legal & Authorization

```
CREATED BY: Dairon
PURPOSE: Authorized Penetration Testing
STATUS: I have explicit permission for this assessment
USAGE: Professional Security Testing ONLY
```

## 🚨 Detection Evasion

```
BASIC (Current):
├── Console window visible
├── Process: python.exe
└── File creation on Desktop

ADVANCED (Future):
├── Compile to .exe (PyInstaller)
├── Process hollowing
├── Alternate data streams
└── Encrypted storage
```

## 🧹 Cleanup

```batch
@echo off
taskkill /f /im python.exe 2>nul
del "%USERPROFILE%\Desktop\my_global_notes.txt"
echo ✅ Logger removed
```

## ⭐ Pro Tips

```
PRO TIP #1: Always test in VM first
PRO TIP #2: Run as pythonw.exe for stealth
PRO TIP #3: Monitor with Process Explorer
PRO TIP #4: Combine with screenshot grabber
PRO TIP #5: Timestamp entries for session tracking
```

---

## 📞 Support

**Author**: Dairon  
**Version**: 1.0 (Global Edition)  
**Dependencies**: `keyboard` only  

```
🚨 FOR AUTHORIZED PENTESTERS ONLY 🚨
Deploy responsibly. Document everything.
```
