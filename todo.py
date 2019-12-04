#!/usr/bin/python3
###
# Filename		todo.py
# Author		Kristopher Chambers
# Updated		2019-12-03
# Project		Todo App
###

import datetime

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk

# Quick object references for later:
builder = Gtk.Builder()
builder.add_from_file("gui.glade")
window = builder.get_object("main_window")
todo_store = builder.get_object("todo_store")
pri_store = builder.get_object("pri_store")
sorted_search_store = builder.get_object("sorted_search_store")
tasks_treeview = builder.get_object("tasks_treeview")

class Handler:
	def on_main_window_destroy(self, *args):
		Gtk.main_quit()

	def on_tasks_treeview_key_release (self, view, event):
		keyname = Gdk.keyval_name(event.keyval)
		# TODO: remove and replace with accelators
		#if keyname == "Delete":
		#	self.on_delete_clicked ()
				
	def on_quick_add_clicked (self, entry):
		"""Quickly add a new task to the list"""
		
		# TODO: fully parse new task text before adding
		text = entry.get_text()
		
		# TODO: make creation dates optional in preferences
		dt = datetime.date.today().isoformat()

		# TODO: add support for filtering and sorting list, by converting
		# child iterators to sorted iterators.

		# Create new task
		child_i = todo_store.append([False, "", text, "", dt, ""])

		# Select the new task after we make it.
		selection = tasks_treeview.get_selection()
		selection.select_iter(child_i)
		
		# clear the entry box when we're done
		entry.set_text ("")

		
	def on_delete_clicked (self, button):
		"""deletes currently selected task"""
		# TODO: allow deletions of multiple selected tasks
		model, i = tasks_treeview.get_selection().get_selected()
		if i is not None:
			model.remove(i)
		
	def on_save_as_clicked (self, *args):
		# TODO: implement Save As to save task list to disk
		pass
		
	def on_open_clicked (self, *args):
		# TODO: implement Open function to load todo.txt from disk
		pass

	def on_search_changed (self, *args):
		# TODO: implement Search function to let user look for specific
		# contexts and projects.
		pass

	def on_done_toggled (self, cell, path):
		"""toggles a given task's done status"""
		
		done = not todo_store[path][0]
		todo_store[path][0] = done
		
		# TODO: make completion dates optional in preferences
		# if task is complete, set completion date to the current date.
		if done:
			dt = datetime.date.today().isoformat()
			todo_store[path][5] = dt

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

