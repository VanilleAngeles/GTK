import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class ScaleWindow(Gtk.Window):
	def __init__(self):
		super().__init__(title="Scale Demo")
		self.set_border_width(10)

		Vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(Vbox)

		label = Gtk.Label(label='Demonstration Scale')
		label.set_valign(Gtk.Align.CENTER)
		Vbox.pack_start(label, True, True, 0)

		self.scale = Gtk.Scale().new_with_range(Gtk.Orientation.HORIZONTAL, min=30, max=240, step=30)
		Vbox.pack_start(self.scale, True, True, 0)
		
		button = Gtk.Button.new_with_label('Get value')
		button.connect('clicked', self.on_click)
		Vbox.pack_start(button, True, True, 0)
		
	def on_click(self, button):
		Value=self.scale.get_value()
		print(Value)
		return()

win = ScaleWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
