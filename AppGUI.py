import tkinter as tk
import tkinter.messagebox
import customtkinter 
from PIL import Image
import os

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        # window
        self.title("Computer Hardware Information Management System")
        self.geometry(f"{1280}x{700}")
        
        # grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        # import image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "App images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(33, 33))
        self.plus_logo = customtkinter.CTkImage(Image.open(os.path.join(image_path, "black_plus.jpg")), size=(12, 12))
        
    # sidebar
        
        # logo and frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="  Group 3",image=self.logo_image, compound="left",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        # buttons
            # CPU    
        self.cpu_button = customtkinter.CTkButton(self.sidebar_frame, text="CPU",fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.cpu_button_event)
        self.cpu_button.grid(row=2, column=0, padx=20, pady=10)
            # GPU    
        self.gpu_button = customtkinter.CTkButton(self.sidebar_frame, text="GPU",fg_color="transparent", corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.gpu_button_event)
        self.gpu_button.grid(row=3, column=0, padx=20, pady=10)
            # PSU    
        self.psu_button = customtkinter.CTkButton(self.sidebar_frame, text="PSU", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.psu_button_event)
        self.psu_button.grid(row=4, column=0, padx=20, pady=10)
            # RAM    
        self.ram_button = customtkinter.CTkButton(self.sidebar_frame, text="RAM", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.ram_button_event)
        self.ram_button.grid(row=5, column=0, padx=20, pady=10)
            # Mainboard  
        self.mainboard_button = customtkinter.CTkButton(self.sidebar_frame, text="Mainboard", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.mainboard_button_event)
        self.mainboard_button.grid(row=6, column=0, padx=20, pady=10)
            # Cooling    
        self.cooling_button = customtkinter.CTkButton(self.sidebar_frame, text="Cooling", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.cooling_button_event)
        self.cooling_button.grid(row=7, column=0, padx=20, pady=10)
            # Monitors    
        self.monitor_button = customtkinter.CTkButton(self.sidebar_frame, text="Monitors", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.monitor_button_event)
        self.monitor_button.grid(row=8, column=0, padx=20, pady=10)
            # Storage  
        self.storage_button = customtkinter.CTkButton(self.sidebar_frame, text="Storage", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.storage_button_event)
        self.storage_button.grid(row=9, column=0, padx=20, pady=10)
            # Peripherals    
        self.peripheral_button = customtkinter.CTkButton(self.sidebar_frame, text="Peripherals", fg_color="transparent",corner_radius=0, height=40, border_spacing=10,
                                                  text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"), anchor="w", command=self.peripheral_button_event)
        self.peripheral_button.grid(row=10, column=0, padx=20, pady=10)
        
        # buttons frame
            # CPU
        self.cpu_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.cpu_frame.grid_columnconfigure(0, weight=1)
        
        self.cpu_frame_new_button = customtkinter.CTkButton(self.cpu_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.cpu_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.cpu_label = customtkinter.CTkLabel(self.cpu_frame, text="CPU", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.cpu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # GPU
        self.gpu_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.gpu_frame.grid_columnconfigure(0, weight=1)
        
        self.gpu_frame_new_button = customtkinter.CTkButton(self.gpu_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.gpu_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.gpu_label = customtkinter.CTkLabel(self.gpu_frame, text="GPU", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.gpu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # PSU
        self.psu_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.psu_frame.grid_columnconfigure(0, weight=1)
        
        self.psu_frame_new_button = customtkinter.CTkButton(self.psu_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.psu_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.psu_label = customtkinter.CTkLabel(self.psu_frame, text="PSU", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.psu_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # RAM
        self.ram_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ram_frame.grid_columnconfigure(0, weight=1)
        
        self.ram_frame_new_button = customtkinter.CTkButton(self.ram_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.ram_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.ram_label = customtkinter.CTkLabel(self.ram_frame, text="RAM", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.ram_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # mainboard
        self.mainboard_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.mainboard_frame.grid_columnconfigure(0, weight=1)
        
        self.mainboard_frame_new_button = customtkinter.CTkButton(self.mainboard_frame, text="+ Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.mainboard_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.mainboard_label = customtkinter.CTkLabel(self.mainboard_frame, text="Mainboard", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.mainboard_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # cooling
        self.cooling_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.cooling_frame.grid_columnconfigure(0, weight=1)
        
        self.cooling_frame_new_button = customtkinter.CTkButton(self.cooling_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.cooling_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.cooling_label = customtkinter.CTkLabel(self.cooling_frame, text="Cooling", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.cooling_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # monitor
        self.monitor_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.monitor_frame.grid_columnconfigure(0, weight=1)
        
        self.monitor_frame_new_button = customtkinter.CTkButton(self.monitor_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.monitor_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.monitor_label = customtkinter.CTkLabel(self.monitor_frame, text="Monitor", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.monitor_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # storage
        self.storage_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.storage_frame.grid_columnconfigure(0, weight=1)
        
        self.storage_frame_new_button = customtkinter.CTkButton(self.storage_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.storage_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.storage_label = customtkinter.CTkLabel(self.storage_frame, text="Storage", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.storage_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
            # peripheral
        self.peripheral_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.peripheral_frame.grid_columnconfigure(0, weight=1)
        
        self.peripheral_frame_new_button = customtkinter.CTkButton(self.peripheral_frame, text=" Add new item", font=customtkinter.CTkFont(size=15, weight="normal"), 
                                                            image=self.plus_logo, compound="left")
        self.peripheral_frame_new_button.grid(row=0, column=1, padx=20, pady=10, sticky="e")
        
        self.peripheral_label = customtkinter.CTkLabel(self.peripheral_frame, text="Peripherals", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.peripheral_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="w")
        
        # theme menu
        self.theme_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Theme", anchor="w")
        self.theme_mode_label.grid(row=11, column=0, padx=20, pady=(10, 0))
        self.theme_mode_option_menu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light"],
                                                                  command=self.change_theme_mode_event)
        self.theme_mode_option_menu.grid(row=12, column=0, padx=20, pady=(10, 10))
        
        # navigation
        self.select_frame_by_name("CPU")
        self.select_frame_by_name("GPU")
        self.select_frame_by_name("PSU")
        self.select_frame_by_name("RAM")
        self.select_frame_by_name("Mainboard")
        self.select_frame_by_name("Cooling")
        self.select_frame_by_name("Monitor")
        self.select_frame_by_name("Storage")
        self.select_frame_by_name("Peripheral")

# functions      
    # theme
    def change_theme_mode_event(self, new_theme_mode: str):
        customtkinter.set_appearance_mode(new_theme_mode)
    
    # button navigation
    def select_frame_by_name(self,name):
        # highlight the selected category
        self.cpu_button.configure(fg_color=("gray75", "gray25") if name == "CPU" else "transparent")
        self.gpu_button.configure(fg_color=("gray75", "gray25") if name == "GPU" else "transparent")
        self.psu_button.configure(fg_color=("gray75", "gray25") if name == "PSU" else "transparent")
        self.ram_button.configure(fg_color=("gray75", "gray25") if name == "RAM" else "transparent")
        self.mainboard_button.configure(fg_color=("gray75", "gray25") if name == "Mainboard" else "transparent")
        self.cooling_button.configure(fg_color=("gray75", "gray25") if name == "Cooling" else "transparent")        
        self.monitor_button.configure(fg_color=("gray75", "gray25") if name == "Monitor" else "transparent")
        self.storage_button.configure(fg_color=("gray75", "gray25") if name == "Storage" else "transparent")
        self.peripheral_button.configure(fg_color=("gray75", "gray25") if name == "Peripheral" else "transparent")
        
        if name == "CPU":
            self.cpu_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cpu_frame.grid_forget()
        if name == "GPU":
            self.gpu_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.gpu_frame.grid_forget()
        if name == "PSU":
            self.psu_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.psu_frame.grid_forget()
        if name == "RAM":
            self.ram_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.ram_frame.grid_forget()
        if name == "Mainboard":
            self.mainboard_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.mainboard_frame.grid_forget()
        if name == "Cooling":
            self.cooling_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.cooling_frame.grid_forget()
        if name == "Monitor":
            self.monitor_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.monitor_frame.grid_forget()
        if name == "Storage":
            self.storage_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.storage_frame.grid_forget()
        if name == "Peripheral":
            self.peripheral_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.peripheral_frame.grid_forget()        

        # CPU
    def cpu_button_event(self):
        self.select_frame_by_name("CPU")
        # GPU  
    def gpu_button_event(self):
         self.select_frame_by_name("GPU")
        # PSU
    def psu_button_event(self):
        self.select_frame_by_name("PSU")
        # RAM
    def ram_button_event(self):
        self.select_frame_by_name("RAM")
        # Mainboard
    def mainboard_button_event(self):
        self.select_frame_by_name("Mainboard")
        # Cooling
    def cooling_button_event(self):
        self.select_frame_by_name("Cooling")
        # Monitor
    def monitor_button_event(self):
        self.select_frame_by_name("Monitor")
        # Storage
    def storage_button_event(self):
        self.select_frame_by_name("Storage")
        # Peripherals
    def peripheral_button_event(self):
        self.select_frame_by_name("Peripheral")
            
            
# main                   
if __name__ == "__main__":
    app = App()
    app.mainloop()