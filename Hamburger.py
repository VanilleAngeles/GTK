import gi, sys

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Password_Window(Gtk.Window):

	def __init__(self):
		self.Create_Window()

	def Create_Window(self):
		Gtk.Application.__init__(self, title='Hamburger Menu')

		self.add_selection = Gtk.ModelButton(label="Add")
		self.delete_selection = Gtk.ModelButton(label="Delete")
		self.save_selection = Gtk.ModelButton(label="Save")
		self.restore_selection = Gtk.ModelButton(label="Restore")
		self.help_selection = Gtk.ModelButton(label="Help")
		self.about_selection = Gtk.ModelButton(label="About")
		self.quit_selection = Gtk.ModelButton(label="Exit")
		
		self.hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, margin=10, spacing=10)
		self.hbox.add(self.quit_selection)
		self.quit_selection.connect('clicked', self.on_button_clicked)
		self.hbox.show_all()
		
		self.popover = Gtk.Popover()
		self.popover.set_border_width(2)
		self.popover.add(self.hbox)
	
		menu_button = Gtk.MenuButton(popover=self.popover)
		menu_icon = Gtk.Image.new_from_icon_name("open-menu-symbolic", Gtk.IconSize.MENU)
		menu_icon.show()
		menu_button.add(menu_icon)
		menu_button.show()

		hbar = Gtk.HeaderBar()
		hbar.props.show_close_button = True
		hbar.props.title = "Hamburger Menu Demo"
		hbar.add(menu_button)
		hbar.show()
		self.set_titlebar(hbar)

		self.vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, margin=10, spacing=10)
		self.add(self.vbox)
		self.vbox.set_border_width(10) 

		self.label = Gtk.Label(label='toto')
		self.vbox.pack_start(self.label, True, True, 0)
		self.button = Gtk.Button(label="----------Click Here----------")
		self.button.connect("clicked", self.Check_Password)
		self.vbox.pack_start(self.button, True, True, 0)
		self.vbox.show_all()

	def on_button_clicked(self, widget):
		Gtk.main_quit()

	def Check_Password(self, widget):
		print('Modif Menu')
		Elements = self.hbox.get_children()
		for Element in Elements:
			self.hbox.remove (Element)
		Elements = self.vbox.get_children()
		for Element in Elements:
			self.vbox.remove (Element)
		self.hbox.add(self.delete_selection)
		self.hbox.add(self.save_selection)
		self.hbox.add(self.restore_selection)
		self.hbox.add(self.help_selection)
		self.hbox.add(self.about_selection)
		self.about_selection.set_sensitive(False)
		self.hbox.add(self.add_selection)
		self.add_selection.set_sensitive(False)
		self.hbox.add(self.quit_selection)
		self.quit_selection.connect('clicked', self.on_button_clicked)
		self.hbox.show_all()
		self.label = Gtk.Label(label='Ça y est, c\'est fait. Qui c\'est le champion ?')
		self.vbox.pack_start(self.label, True, True, 0)
		self.vbox.show_all()
		
#----- Init
win = Password_Window()
win.connect("destroy", Gtk.main_quit)
win.set_default_size(width=500, height=100)
win.show_all()
Gtk.main()
