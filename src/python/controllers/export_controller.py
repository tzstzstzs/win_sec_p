from tkinter import filedialog, messagebox
from src.python.models.export_to_doc import export_to_docx
import logging


class ExportController:
    def __init__(self, main_window, main_controller):
        self.main_window = main_window
        self.main_controller = main_controller

    def export_data(self):
        # Collect the data for export
        data_to_export = self.main_controller.data_store

        # Ask the user for a file location
        file_path = filedialog.asksaveasfilename(
            defaultextension=".docx",
            filetypes=[("Word documents", "*.docx"), ("All files", "*.*")],
            title="Choose save location"
        )

        # Export the data if a file path was selected
        if file_path:
            try:
                export_to_docx(data_to_export, file_path)
                logging.info("Successfully exported data to DOCX.")
                messagebox.showinfo("Export Successful", f"Data successfully exported to {file_path}")
            except Exception as e:
                logging.error(f"Failed to export data: {e}", exc_info=True)
                messagebox.showerror("Export Error", f"An error occurred while exporting data: {e}")
