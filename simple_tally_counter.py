import tkinter as tk
from tkinter import messagebox

class SimpleTallyCounter:
    def __init__(self, root):
        self.count = 0

        # Set up the main window
        root.title("Tally Counter")
        root.geometry("300x450")  # Increased height to accommodate new widgets

        # Add a title label at the top of the app
        self.title_label = tk.Label(root, text="Tally", font=("Arial", 24, "bold"), bg="white")
        self.title_label.pack(pady=(20, 10))  # Added top padding for better spacing

        # Display the current count
        self.count_label = tk.Label(root, text="0", font=("Arial", 48), bg="white", width=5)
        self.count_label.pack(pady=10)

        # Entry box for increment/decrement value
        self.increment_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.increment_entry.insert(0, "1")  # Default increment by 1
        self.increment_entry.pack(pady=10)

        # Frame for Set Count functionality
        self.set_frame = tk.Frame(root, bg="white")
        self.set_frame.pack(pady=10)

        # Label for Set Count
        self.set_label = tk.Label(self.set_frame, text="Set Starting Count:", font=("Arial", 12), bg="white")
        self.set_label.pack(side="left", padx=(0, 5))

        # Entry for Set Count
        self.set_entry = tk.Entry(self.set_frame, font=("Arial", 12), justify="center", width=10)
        self.set_entry.pack(side="left")

        # Set button
        self.set_button = tk.Button(
            self.set_frame, text="Set", font=("Arial", 12), bg="lightgray", command=self.set_count
        )
        self.set_button.pack(side="left", padx=(5, 0))

        # Increment button
        self.increment_button = tk.Button(
            root, text="+", font=("Arial", 24, "bold"), bg="lightgreen", command=self.increment
        )
        self.increment_button.pack(pady=10)

        # Decrement button
        self.decrement_button = tk.Button(
            root, text="-", font=("Arial", 24, "bold"), bg="lightcoral", command=self.decrement
        )
        self.decrement_button.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(
            root, text="Reset", font=("Arial", 14), bg="lightblue", command=self.reset
        )
        self.reset_button.pack(pady=10)

    def set_count(self):
        try:
            value = int(self.set_entry.get())
            self.count = value
            self.update_display()
            self.set_entry.delete(0, tk.END)  # Clear the entry after setting
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer for the starting count.")

    def increment(self):
        try:
            value = int(self.increment_entry.get())
            self.count += value
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for incrementing.")

    def decrement(self):
        try:
            value = int(self.increment_entry.get())
            self.count -= value
            self.update_display()
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for decrementing.")

    def reset(self):
        self.count = 0
        self.update_display()

    def update_display(self):
        self.count_label.config(text=str(self.count))

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleTallyCounter(root)
    root.mainloop()
