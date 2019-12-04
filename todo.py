#!/usr/bin/python3
###
# Filename		todo.py
# Author		Kristopher Chambers
# Updated		2019-12-01
# Project		Todo App
###

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file("gui.glade")

# Quick object references for later:
window = builder.get_object("main_window")
todo_store = builder.get_object("todo_store")
search_store = builder.get_object("todo_store")
pri_store = builder.get_object("pri_store")
tasks_treeview = builder.get_object("tasks_treeview")

class Handler:
	def on_main_window_destroy(self, *args):
		Gtk.main_quit()
		
	def on_add_clicked (self, button):
		i = todo_store.append([False, "", "", "", "", ""])
		selection = tasks_treeview.get_selection()
		selection.select_iter(i)
		#path = Gtk.TreePath.new_from_string(i.to_string())
		#tasks_treeview.set_cursor(path=path)
		# TODO: use i to move treeview selection to the new task
		
		
	def on_save_as_clicked (self, *args):
		pass
		
	def on_open_clicked (self, *args):
		pass

	def on_search_changed (self, *args):
		pass
			
	def on_done_toggled (self, cell, path):
		"""toggles a given task's done status"""
		todo_store[path][0] = not todo_store[path][0]

	def on_pri_changed (self, cell, path, tree_iter):
		"""changes the priority of a task"""
	
		if tree_iter is not None:
			pri = pri_store[tree_iter][0]
			todo_store[path][1] = pri

	def on_text_edited (self, cell, path, text):
		"""changes a task's main text"""
		todo_store[path][2] = text
				
	def on_due_edited (self, cell, path, text):
		"""changes a task's due date"""
		todo_store[path][3] = text
	
	def on_creation_edited (self, cell, path, text):
		"""changes a task's creation date"""
		todo_store[path][4] = text
		
	def on_completion_edited (self, cell, path, text):
		"""changes a task's completion date"""
		todo_store[path][5] = text
	

builder.connect_signals(Handler())

window.show_all()
Gtk.main()

