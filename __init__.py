# -*- coding: utf-8 -*-
"""
/***************************************************************************
 BBox
                                 A QGIS plugin
 This plugin returns the xmin, ymin, xmax, ymax of the current view window, and the GetMap request of the selected WMS. 
                             -------------------
        begin                : 2017-04-03
        copyright            : (C) 2017 by Maaka2890
        email                : kkj_15@hotmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 3 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load BBox class from file BBox.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .boundingbox import BBox
    return BBox(iface)
