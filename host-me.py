import os
import sys
import time
import traceback
import socket

CONFIG_FILE = "config.py"

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def logo():
    print(f"""{Colors.CYAN}
  ╔════════════════════════════════════════════════════════╗
  ║             Host-Me - Local Server Manager             ║
  ║  GitHub: https://github.com/MyArchiveProjects/host-me  ║
  ╚════════════════════════════════════════════════════════╝
{Colors.RESET}""")

def banner_line(status, message):
    symbols = {
        "ok": f"{Colors.GREEN}[+]{Colors.RESET}",
        "line": f"{Colors.YELLOW}[>]{Colors.RESET}",
        "error": f"{Colors.RED}[!]{Colors.RESET}",
        "info": f"{Colors.BLUE}[?]{Colors.RESET}"
    }
    print(f"{symbols[status]} {message}")

def is_port_available(port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(("localhost", port)) != 0
    except Exception as e:
        banner_line("error", f"Port check failed: {e}")
        return False

def check_if_first_time():
    try:
        if not os.path.exists(CONFIG_FILE):
            first_time_setup()
        else:
            banner_line("ok", "Config file found.")
            time.sleep(1)
            main()
    except Exception as e:
        print_exception("check_if_first_time", e)

def first_time_setup():
    try:
        clear()
        logo()
        banner_line("info", "First-time setup initiated.")
        port = input("Enter port to use (e.g. 8080): ")

        if not port.isdigit():
            raise ValueError("Port must be numeric.")

        with open(CONFIG_FILE, "w") as f:
            f.write(f"first_time = False\nport = {port}\n")
        banner_line("ok", f"Saved config with port {port}")
        time.sleep(1)
        main()

    except Exception as e:
        print_exception("first_time_setup", e)
        input("Press enter to exit...")

def print_exception(context, error):
    banner_line("error", f"Exception in {context}:")
    print(f"{Colors.RED} ├─ Type: {type(error).__name__}")
    print(f" └─ Message: {str(error)}{Colors.RESET}")
    print(f"{Colors.YELLOW} ── Full Traceback:\n{traceback.format_exc()}{Colors.RESET}")

def main():
    try:
        clear()
        logo()

        try:
            import config
            port = config.port
        except Exception as e:
            raise ImportError("Can't import config.py or 'port' not found.")

        if not is_port_available(port):
            banner_line("error", f"Port {port} is already in use.")
            choice = input("Do you want to change it? (y/n): ").lower()
            if choice == 'y':
                new_port = input("Enter new port: ")
                if new_port.isdigit() and is_port_available(int(new_port)):
                    with open(CONFIG_FILE, "w") as f:
                        f.write(f"first_time = False\nport = {new_port}\n")
                    banner_line("ok", f"Config updated. New port: {new_port}")
                    time.sleep(1)
                    main()
                    return
                else:
                    banner_line("error", "Invalid or unavailable port.")
                    input("Press enter to exit...")
                    return
            else:
                banner_line("info", "Exiting.")
                return

        banner_line("info", f"Launching server on port {port}...")
        if os.name == "nt":
            os.system("python server.py")
        else:
            os.system("python3 server.py")

    except Exception as e:
        print_exception("main", e)
        input("Press enter to exit...")

if __name__ == "__main__":
    try:
        check_if_first_time()
    except Exception as e:
        print_exception("__main__", e)
        input("Press enter to exit...")

    sys.exit(0)
