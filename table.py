"""Author=Frans Nordén, Date=2016-12-14"""

import tkinter.font as tkFont
import tkinter.ttk as ttk
import tkinter as tk

class Table(tk.Frame):
	"""Specialized class for tkinter to handle tables. Creates one row as a list of labels which enables change."""
	def __init__(self, parent, rows=12, columns=5):
		"""constructor for the tkinter table, generates rows and columns. takes
		the parent container, number of rows and number of columns as parameters"""
		tk.Frame.__init__(self, parent, background="black")
		self._widgets = []
		self.bind("<Control-q>", self.quit)

		for row in range(rows):
			current_row = []
			for column in range(columns):
				label = tk.Label(self, text="%s/%s" % (row, column), borderwidth=0, width=15)
				label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
				current_row.append(label)

			self._widgets.append(current_row)
		for column in range(columns):
			self.grid_columnconfigure(column, weight=1)

	
	def set(self, row, column, value):
		"""Makes it possible to set values in the cells
		takes in tkinter widgets identified as row and column in the table and the 
		value you want to fill the [row][column] with."""
		widget = self._widgets[row][column]
		widget.configure(text=value)