import tkinter as tk
from tkinter import ttk, colorchooser
import platform
import psutil
import socket
import uuid

class NanoHWApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("NanoHW")
        self.geometry("1000x700")
        self.configure(bg="#f0f0f0")

        # Initialize default brush color and size
        self.brush_color = "black"
        self.brush_size = 2

        # Setup UI components
        self.setup_widgets()

    def setup_widgets(self):
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Create system info tab
        self.info_tab = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(self.info_tab, text="System Info")
        self.setup_info_tab()

        # Create NanoPaint tab
        self.paint_tab = tk.Frame(self.notebook, bg="#ffffff")
        self.notebook.add(self.paint_tab, text="NanoPaint")
        self.setup_paint_tab()

    def setup_info_tab(self):
        # OS Info
        tk.Label(self.info_tab, text="Operating System:", bg="#ffffff", font=("Arial", 12)).grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.os_label = tk.Label(self.info_tab, text=self.get_os_info(), bg="#ffffff", font=("Arial", 12))
        self.os_label.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)

        # CPU Info
        tk.Label(self.info_tab, text="CPU Info:", bg="#ffffff", font=("Arial", 12)).grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.cpu_label = tk.Label(self.info_tab, text=self.get_cpu_info(), bg="#ffffff", font=("Arial", 12))
        self.cpu_label.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)

        # Memory Info
        tk.Label(self.info_tab, text="Memory Info:", bg="#ffffff", font=("Arial", 12)).grid(row=2, column=0, sticky=tk.W, padx=5, pady=5)
        self.memory_label = tk.Label(self.info_tab, text=self.get_memory_info(), bg="#ffffff", font=("Arial", 12))
        self.memory_label.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)

        # Network Info
        tk.Label(self.info_tab, text="Network Info:", bg="#ffffff", font=("Arial", 12)).grid(row=3, column=0, sticky=tk.W, padx=5, pady=5)
        self.network_label = tk.Label(self.info_tab, text=self.get_network_info(), bg="#ffffff", font=("Arial", 12))
        self.network_label.grid(row=3, column=1, sticky=tk.W, padx=5, pady=5)

        # Process List
        tk.Label(self.info_tab, text="Running Processes:", bg="#ffffff", font=("Arial", 12)).grid(row=4, column=0, sticky=tk.W, padx=5, pady=5)

        # Treeview for process information
        self.process_tree = ttk.Treeview(self.info_tab, columns=("PID", "Name", "CPU", "Memory"), show="headings")
        self.process_tree.heading("PID", text="PID")
        self.process_tree.heading("Name", text="Name")
        self.process_tree.heading("CPU", text="CPU (%)")
        self.process_tree.heading("Memory", text="Memory (MB)")
        self.process_tree.grid(row=5, column=0, columnspan=2, pady=10, padx=5, sticky="nsew")

        # Update process list
        self.update_process_list()

        # Resize columns
        self.process_tree.column("PID", width=100, anchor="center")
        self.process_tree.column("Name", width=300, anchor="w")
        self.process_tree.column("CPU", width=100, anchor="center")
        self.process_tree.column("Memory", width=100, anchor="center")

        # Configure grid weights
        self.info_tab.grid_rowconfigure(5, weight=1)
        self.info_tab.grid_columnconfigure(1, weight=1)

    def setup_paint_tab(self):
        # Create a canvas for painting
        self.canvas = tk.Canvas(self.paint_tab, bg="#ffffff", width=800, height=500)
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Setup Paint Tools Frame
        self.tools_frame = tk.Frame(self.paint_tab, bg="#ffffff")
        self.tools_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Brush Size
        tk.Label(self.tools_frame, text="Brush Size:", bg="#ffffff").pack(pady=5)
        self.brush_size_var = tk.IntVar(value=self.brush_size)
        self.brush_size_scale = tk.Scale(self.tools_frame, from_=1, to_=20, orient=tk.HORIZONTAL, variable=self.brush_size_var)
        self.brush_size_scale.pack(pady=5)

        # Color Picker
        tk.Button(self.tools_frame, text="Pick Color", command=self.choose_color).pack(pady=5)

        # Clear Canvas
        tk.Button(self.tools_frame, text="Clear Canvas", command=self.clear_canvas).pack(pady=5)

        # Bind mouse events for drawing
        self.drawing = False
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def choose_color(self):
        color_code = colorchooser.askcolor()[1]
        if color_code:
            self.brush_color = color_code

    def clear_canvas(self):
        self.canvas.delete("all")

    def start_drawing(self, event):
        self.drawing = True
        self.last_x, self.last_y = event.x, event.y

    def draw(self, event):
        if self.drawing:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y, fill=self.brush_color, width=self.brush_size_var.get())
            self.last_x, self.last_y = event.x, event.y

    def stop_drawing(self, event):
        self.drawing = False

    def get_os_info(self):
        return f"{platform.system()} {platform.version()}"

    def get_cpu_info(self):
        return f"{platform.processor()} ({psutil.cpu_count()} cores)"

    def get_memory_info(self):
        mem = psutil.virtual_memory()
        return f"Total: {self.bytes_to_gb(mem.total)} GB, Available: {self.bytes_to_gb(mem.available)} GB"

    def bytes_to_gb(self, bytes):
        return round(bytes / (1024 ** 3), 2)

    def get_network_info(self):
        ip_address = self.get_ip_address()
        mac_address = self.get_mac_address()
        return f"IP Address: {ip_address}\nMAC Address: {mac_address}"

    def get_ip_address(self):
        try:
            hostname = socket.gethostname()
            ip_address = socket.gethostbyname(hostname)
        except socket.error:
            ip_address = "Not available"
        return ip_address

    def get_mac_address(self):
        try:
            mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
        except (ValueError, IOError):
            mac_address = "Not available"
        return mac_address

    def update_process_list(self):
        # Clear current process list
        for row in self.process_tree.get_children():
            self.process_tree.delete(row)

        # Fetch and display process information
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                mem_mb = proc.info['memory_info'].rss / (1024 ** 2)  # Convert bytes to MB
                self.process_tree.insert("", "end", values=(proc.info['pid'], proc.info['name'], proc.info['cpu_percent'], round(mem_mb, 2)))
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                continue

if __name__ == "__main__":
    app = NanoHWApp()
    app.mainloop()
