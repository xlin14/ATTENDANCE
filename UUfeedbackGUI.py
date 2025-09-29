import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class FeedbackApp:
    def __init__(self, master):
        self.master = master
        master.title("Feedback Form")
        master.geometry("450x350")
        master.resizable(False, False) # Make window not resizable

        # Style configuration to give the app a modern look
        self.style = ttk.Style(master)
        self.style.configure('TLabel', font=('Helvetica', 11))
        self.style.configure('TButton', font=('Helvetica', 10, 'bold'))
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'))

        # --- Main Frame ---
        # This frame holds all the other widgets
        main_frame = ttk.Frame(master, padding="20 20 20 20")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # --- Header Label ---
        header_label = ttk.Label(
            main_frame,
            text="Please provide feedback on your experience",
            style='Header.TLabel'
        )
        header_label.pack(pady=(0, 20))

        # --- Form Frame ---
        # A dedicated frame for the input fields
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(fill=tk.X)
        # Configure the grid to allow the entry widgets to expand horizontally
        form_frame.columnconfigure(1, weight=1)

        # --- Name Field ---
        name_label = ttk.Label(form_frame, text="Name:")
        name_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
        self.name_entry = ttk.Entry(form_frame, width=40)
        self.name_entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)

        # --- Email Field ---
        email_label = ttk.Label(form_frame, text="Email:")
        email_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
        self.email_entry = ttk.Entry(form_frame, width=40)
        self.email_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)

        # --- Feedback Field ---
        feedback_label = ttk.Label(form_frame, text="Feedback:")
        feedback_label.grid(row=2, column=0, sticky="nw", padx=5, pady=5) # sticky="nw" aligns the label to the top-left
        self.feedback_text = tk.Text(form_frame, height=8, width=40, font=('Helvetica', 10))
        self.feedback_text.grid(row=2, column=1, sticky="ew", padx=5, pady=5)

        # --- Submit Button ---
        submit_button = ttk.Button(main_frame, text="Submit Feedback", command=self.submit_feedback)
        submit_button.pack(pady=20)

    def submit_feedback(self):
        """Handle the submission of the feedback form."""
        name = self.name_entry.get()
        email = self.email_entry.get()
        # .get("1.0", tk.END) retrieves all text from the Text widget
        feedback = self.feedback_text.get("1.0", tk.END).strip()

        # Basic validation to ensure no fields are empty
        if not name or not email or not feedback:
            messagebox.showerror("Error", "All fields are required!")
            return

        # Print to console (in a real app, this data would be saved to a file or database)
        print("--- New Feedback Received ---")
        print(f"Name: {name}")
        print(f"Email: {email}")
        print(f"Feedback: {feedback}")
        print("-----------------------------\n")

        # Show a confirmation message to the user
        messagebox.showinfo("Success", "Thank you for your feedback!")

        # Clear the form fields for the next submission
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.feedback_text.delete("1.0", tk.END)


# This block runs when the script is executed directly
if __name__ == "__main__":
    root = tk.Tk()  # Create the main window
    app = FeedbackApp(root) # Create an instance of our app
    root.mainloop() # Start the application's event loop

