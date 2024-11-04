import customtkinter
#import utils

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Generation MG Template")
        self.geometry("1000x400")
        self.grid_columnconfigure((0, 1), weight=1)
        #Label
        self.labelName = customtkinter.CTkLabel(self, text="File")
        self.labelName.grid(row=0, column=0, padx=0, pady=0, sticky="ew")
        #Text Box
        self.displayBox = customtkinter.CTkTextbox(self, width=100, height=5)
        self.displayBox.grid(row=1, column=0, padx=10, columnspan = 3, sticky="ew")
        #Browse Button
        self.browseButton = customtkinter.CTkButton(self, text="Browse", command=self.browse_callback)
        self.browseButton.grid(row=1, column=4, padx=10, pady=10, sticky="ew")
        #Generate Button
        self.generateButton = customtkinter.CTkButton(self, text="Generate", command=self.generate_callback)
        self.generateButton.grid(row=2, column=0, padx=10, pady=10, columnspan=5, sticky="ew")
        #Text Box Status
        self.displayBoxStatus = customtkinter.CTkTextbox(self)
        self.displayBoxStatus.grid(row=3, column=0, padx=10, pady=10, columnspan = 5, sticky="ew")
        
    def browse_callback(self):
        print("button pressed")

    def generate_callback(self):
        print("button pressed")

if __name__ == "__main__":
    app = App()
    # Runs the app
    app.mainloop() 