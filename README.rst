~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Russian VTB24 bank plugin for ofxstatement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

..`ofxstatement`_ https://github.com/kedder/ofxstatement is a tool to convert proprietary bank statement to OFX format,
suitable for importing to GnuCash. Plugin for ofxstatement parses a
particular proprietary bank statement format and produces common data
structure, that is then formatted into an OFX file.

`ofxstatement-vtb24`_ provides vtb24 bank plugin for ofxstatement.

Supported banks:

* VTB24 Bank (http://vtb24.ru) plugin 'vtb24'

В целом работает, но GnuCash не умеет импортировать ofx с unicode символами

.. _Bug in GnuCash: https://bugzilla.gnome.org/show_bug.cgi?id=703527

И нужно доделать, что бы ofx формировался в кодировке UTF-8, сейчас формирует cp1251

Authors
=======

|  Copyright (c) 2016 Partizand


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.
