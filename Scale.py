import sys, gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MyWindow(Gtk.ApplicationWindow):

	def __init__(self, app):
		Gtk.Window.__init__(self, title="Scale", application=app)
		self.set_default_size(200, 200)
		self.set_border_width(5)


		ad1 = Gtk.Adjustment(value=12, lower=0, upper=100, step_increment=5, page_increment=10, page_size=0)

		# SCALE horizontal
		self.h_scale = Gtk.Scale(
			orientation=Gtk.Orientation.HORIZONTAL, adjustment=ad1)
		# avec des entiers (no digits)
		self.h_scale.set_digits(0)
		# Dans l'espace du grid
#		self.h_scale.set_hexpand(True)
#		self.h_scale.set_valign(Gtk.Align.START)

		# SIGNAL
		self.h_scale.connect("value-changed", self.scale_moved)

		# LABEL
		self.label = Gtk.Label()
		self.label.set_text("Move Scale")

		# GRID
		grid = Gtk.Grid()
		grid.set_column_spacing(10)
		grid.set_column_homogeneous(True)
		grid.attach(self.h_scale, 0, 0, 1, 1)
		grid.attach(self.label, 0, 1, 1, 1)

		self.add(grid)

	# CALLBACK
	def scale_moved(self, event):
		self.label.set_text("Value " + str(int(self.h_scale.get_value())) + ".")


class MyApplication(Gtk.Application):

	def __init__(self):
		Gtk.Application.__init__(self)

	def do_activate(self):
		win = MyWindow(self)
		win.show_all()

	def do_startup(self):
		Gtk.Application.do_startup(self)

app = MyApplication()
exit_status = app.run(sys.argv)
sys.exit(exit_status)
