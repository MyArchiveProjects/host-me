
# ⚡ HostMe - Instant Local Server Launcher

> Simple. Fast. Cross-platform. Local server launcher made for developers, by developers.

---

## 🌐 What is HostMe?

HostMe is a blazing-fast, cross-platform CLI tool to **instantly run a local server** to test or preview your website. Whether you want to **ping your HTML**, check how your frontend behaves locally, or just quickly host a static page — HostMe gets it done in seconds.

---

## 🚀 Features

- ✅ One-time setup with automatic config
- 🌍 Cross-platform support (Windows & Linux)
- 🧠 Smart error handling and port availability checks
- ⚠️ Beautiful colored CLI interface (with `[+]`, `[!]`, `[?]`, `[>]`)
- 🧪 Designed for testing, debugging, and local web previews
- 🔁 Persistent config via `config.py`
- 📁 Serves current folder content (HTML, CSS, JS, etc.)
- 🧱 Fully extendable base (custom index.html, Python modules)
- 🔗 GitHub link displayed directly in terminal

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/67105413-a794-4d36-be66-ccf0a28d2939)


---

## 📦 Installation

### 🧩 Requirements

- Python 3.6+
- OS: Windows or Linux
- No external dependencies required

---

## 🛠️ Setup

```bash
git clone https://github.com/MyArchiveProjects/host-me
cd host-me
python main.py
```

> On Linux, use `python3 main.py` instead.

---

## ⚙️ First Time?

The first time you launch `main.py`, HostMe will:

1. Ask you for a port (e.g. 8080)
2. Save it in `config.py`
3. Automatically launch the server

---

## 💻 How It Works

HostMe uses Python’s built-in `http.server` and `socketserver` to spin up a local server in your current directory.

It opens `index.html` (or directory listing) in your default browser, making it perfect for quick previews and testing.

---

## 🧪 Example Use Cases

- Test a local static website before deploying
- Share a live preview via tools like Ngrok
- Validate HTML/CSS/JS behavior
- Ping your local server from frontend code
- Develop in a self-contained local environment

---

## 🔧 Configuration

All settings are stored in a lightweight `config.py` file:

```python
first_time = False
port = 8080
```

You can manually edit this file anytime to change your preferred port.

---

## 📁 Default index.html

You can fully customize the landing page!

Default `index.html`:

```html
<!DOCTYPE html>
<html>
  <head><title>HostMe</title></head>
  <body>
    <h1>Hello world!</h1>
    <p>This is your local site.</p>
  </body>
</html>
```

Want to test a different page? Just edit `index.html` or serve any other file from the directory.

---

## 🧠 Error Handling

HostMe features **robust error handling**, including:

- Port in use? It’ll offer to change it.
- Config missing? It’ll regenerate it.
- Crash? You’ll get a full traceback with colored logs.

No more silent failures. You’ll always know what happened and why.

---

## 📌 Roadmap

- [x] Auto port conflict detection
- [x] Full Windows & Linux support
- [x] Customizable index.html
- [ ] Live-reloading (like `livereload`)
- [ ] Auto Ngrok tunnel integration
- [ ] Web dashboard for server control

---

## 🧑‍💻 Author

Made with ❤️ by [MyArchiveProjects](https://github.com/MyArchiveProjects)

---

## 🫡 License

This project is licensed under the MIT License.  
You’re free to use, modify, and share.

---

## 🤝 Contribute

Want to help improve HostMe?

- Fork the repo
- Create your feature branch (`git checkout -b feature/something`)
- Commit your changes
- Push and create a Pull Request

All contributions welcome 😎
