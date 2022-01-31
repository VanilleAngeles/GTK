#!/usr/bin/env python3
# coding: utf-8
'''
References:
- for RadioButton & Progressbarr --> https://python-gtk-3-tutorial.readthedocs.io/en/latest/button_widgets.html
- for reset timeout --> EXEMPLE #6 in https://python.hotexamples.com/fr/examples/gi.repository/GLib/timeout_add/python-glib-timeout_add-method-examples.html
'''
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib, Gdk

class ProgressBarWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title='Multiplication Table')
#------	acces to CSS file
		style_provider = Gtk.CssProvider()
		style_provider.load_from_path('Timeout.css')
		Gtk.StyleContext.add_provider_for_screen(
			Gdk.Screen.get_default(),
			style_provider,
			Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)
#------ Create Vertical Box		
		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.DisplayGrid()
		
	def DisplayGrid(self):
		Elements = self.vbox.get_children()
		for Element in Elements:
			self.vbox.remove(Element)
#------ GRID
		self.grid = Gtk.Grid()
		self.grid.set_hexpand(True)
		self.grid.set_column_spacing(10)
#------ Levels
		LevelsLabel = Gtk.Label()
		LevelsLabel.set_text('Niveau')
		LevelsLabel.set_name('Titre')
		self.grid.attach(LevelsLabel, 0, 0, 1, 1)
		Levels = Gtk.ListStore(int,str)
		Levels.append([100, 'Facile'])
		Levels.append([50, 'Moyen'])
		Levels.append([20, 'Difficile'])
		LevelsCombo = Gtk.ComboBox.new_with_model_and_entry(Levels)
		LevelsCombo.connect('changed', self.on_combo_changed)
		LevelsCombo.set_entry_text_column(1)
		self.grid.attach(LevelsCombo, 1, 0, 1, 1)
#------ Progress Barr
		self.progressbar = Gtk.ProgressBar()
		self.grid.attach(self.progressbar, 0, 1, 2, 1)
#------ Start
		StartButton = Gtk.Button.new_with_label('Restart')
		StartButton.set_name('Titre')
		StartButton.connect('clicked', self.on_start_clicked)
		self.grid.attach(StartButton, 0, 2, 2, 1)

		self.Timeout=50
		self.timeout_id = GLib.timeout_add(self.Timeout, self.on_timeout, None)
		self.vbox.show_all()

#------ Display
		self.vbox.pack_end(self.grid,True,True,5)
		self.add(self.vbox)
		self.vbox.show_all()

	def on_combo_changed(self,combo):
		tree_iter = combo.get_active_iter()
		if tree_iter is not None:
			model = combo.get_model()
			row_id, name = model[tree_iter][:2]
			GLib.source_remove(self.timeout_id)
			self.timeout_id = GLib.timeout_add(row_id, self.on_timeout, None)
			self.progressbar.set_fraction(0)
		else:
			entry = combo.get_child()
		
	def on_start_clicked(self,StartButton):
		self.progressbar.set_fraction(0)

	def on_timeout(self, user_data):
		new_value = self.progressbar.get_fraction() + 0.01
		if new_value > 1:
			new_value = 0
		self.progressbar.set_fraction(new_value)
		return True

win = ProgressBarWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
