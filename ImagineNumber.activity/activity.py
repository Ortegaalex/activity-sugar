# Copyright 2018 Alex Ortega para la competencia de GCI
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

"""Aca va a ir comentarios de una pequenha descripcion de la actividad"""

import gi, random
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import gettext

from sugar3.activity import activity
from sugar3.graphics.toolbarbox import ToolbarBox
from sugar3.activity.widgets import ActivityButton
from sugar3.activity.widgets import TitleEntry
from sugar3.activity.widgets import StopButton
from sugar3.activity.widgets import ShareButton
from sugar3.activity.widgets import DescriptionItem

app = "activity"

gettext.textdomain(app)
gettext.bindtextdomain(app, "./po")
_ = gettext.gettext


class ImagineNumberActivity(activity.Activity):
    """ImagineNumberActivity class as specified in activity.info"""

    def __init__(self, handle):
        """Set up the ImagineNumber activity."""
        activity.Activity.__init__(self, handle)

        # No es necesario compartir
        # Esto hace que la opcion de compartir no funcione
        self.max_participants = 1

        # toolbar with the new toolbar redesign
        toolbar_box = ToolbarBox()

        activity_button = ActivityButton(self)
        toolbar_box.toolbar.insert(activity_button, 0)
        activity_button.show()

        title_entry = TitleEntry(self)
        toolbar_box.toolbar.insert(title_entry, -1)
        title_entry.show()

        description_item = DescriptionItem(self)
        toolbar_box.toolbar.insert(description_item, -1)
        description_item.show()

        share_button = ShareButton(self)
        toolbar_box.toolbar.insert(share_button, -1)
        share_button.show()

        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)
        toolbar_box.toolbar.insert(separator, -1)
        separator.show()

        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show()

	#Ahora generaremos los numeros aleatorios y le creamos la cadena correspondiente
	ran_a = random.randint(1, 100)
	ran_b = random.randint(1, 100)
	ran_c = random.randint(1, 100)
	num_imagined = ran_a + ran_b - ran_c
	cad_1 = _("Now add ")
	cad_2 = _("Now subtract ")
	cad_3 = _(" to the number you have imagined")
	cad_4 = _("The final number is ")
	cad_5 = _("I have already added")
	cad_6 = _("I have already subtracted")
	cad_7 = _("Imagine a number between 1 and 100")
	cad_8 = _("Now subtract the number that you have imagined at the beginning")
	str_1 = cad_1 + str(ran_a) + cad_3
	str_2 = cad_1 + str(ran_b) + cad_3
	str_3 = cad_2 + str(ran_c) + cad_3
	str_4 = cad_4 + str(num_imagined)
	
	#Creamos la primera caja con todo lo que contendra
	box_1 = Gtk.VBox()
	label_1 = Gtk.Label()
	label_1.set_markup("<span font=\"30\"><b>"+cad_7+"</b></span>")
	button_1 = Gtk.Button(_("Already imagined"))
	
	#Creamos la segunda caja
	box_2 = Gtk.VBox()
	label_2 = Gtk.Label()
	label_2.set_markup("<span font=\"30\"><b>"+str_1+"</b></span>")
	button_2 = Gtk.Button(cad_5)

	#Creamos la tercera caja
	box_3 = Gtk.VBox()
	label_3 = Gtk.Label()
	label_3.set_markup("<span font=\"30\"><b>"+str_2+"</b></span>")
	button_3 = Gtk.Button(cad_5)

	#Creamos la cuarta caja
	box_4 = Gtk.VBox()
	label_4 = Gtk.Label()
	label_4.set_markup("<span font=\"30\"><b>"+str_3+"</b></span>")
	button_4 = Gtk.Button(cad_6)
	
	#Creamos la quinta caja
	box_5 = Gtk.VBox()
	label_5 = Gtk.Label()
	label_5.set_markup("<span font=\"30\"><b>"+cad_8+"</b></span>")
	button_5 = Gtk.Button(cad_6)

	#Creamos la sexta caja
	box_6 = Gtk.VBox()
	label_6 = Gtk.Label()
	label_6.set_markup("<span font=\"30\"><b>"+str_4+"</b></span>")
	button_6 = Gtk.Button(_("Play again"))

	#Empaquetamos todo a las cajas correspondientes
	box_1.pack_start(label_1, True, True, 10)
	box_1.pack_start(button_1, False, False, 10)

	box_2.pack_start(label_2, True, True, 10)
	box_2.pack_start(button_2, False, False, 10)

	box_3.pack_start(label_3, True, True, 10)
	box_3.pack_start(button_3, False, False, 10)

	box_4.pack_start(label_4, True, True, 10)
	box_4.pack_start(button_4, False, False, 10)

	box_5.pack_start(label_5, True, True, 10)
	box_5.pack_start(button_5, False, False, 10)

	box_6.pack_start(label_6, True, True, 10)
	box_6.pack_start(button_6, False, False, 10)

	#Ahora le configuramos una accion al evento clicked del boton
	button_1.connect("clicked", self.action, box_1, box_2)
	button_2.connect("clicked", self.action, box_2, box_3)
	button_3.connect("clicked", self.action, box_3, box_4)
	button_4.connect("clicked", self.action, box_4, box_5)
	button_5.connect("clicked", self.action, box_5, box_6)
	button_6.connect("clicked", self.action, box_6, box_1)


	#Ahora agregamos la primera caja a la ventana principal
	self.set_canvas(box_1)
	
	box_1.show_all()

    def action(self, widget, box_a, box_s):
	self.set_canvas(box_s) #le agregamos esta caja al canvas original
	box_a.hide() #cambia el nombre 'actual' por el significado en ingles, lo mismo para siguiente, ocultamos la caja actual
	box_s.show_all() #mostramos la caja siguiente

   
