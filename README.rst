###############################################################################
Python bindings for command line tools
###############################################################################

Commands can be chained together and are executed once with ``.run()``. The
subprocess results are found under the instance variables ``stdout``,
``stderr`` and ``status``. An additional variable named ``outputs`` lists a
structured version of stdout for each separate commands.

.. contents:: :local:

Xdotool
*******************************************************************************

**DESCRIPTION**

   `xdotool <https://github.com/jordansissel/xdotool>`_ lets you
   programmatically (or manually) simulate keyboard input and mouse activity,
   move and resize windows, etc.

**EXAMPLES**

.. code:: python

   from pyclutils import Xdotool as X11

   # Activate the web browser

   X11().search('Navigator', classname=True)                                  \
        .windowactivate(sync=True)                                            \
        .getactivewindow()                                                    \
        .run()

   # Get current window width

   X11().getactivewindow()                                                    \
        .getwindowgeometry()                                                  \
        .run()                                                                \
        .outputs[0]['width']

Xclip
*******************************************************************************

**DESCRIPTION**

   Reads  from standard in, or from one or more files, and makes the data
   available as an X selection for pasting into X applications. Prints current
   X selection to standard out.

**EXAMPLES**

.. code:: python

   from pyclutils import Xclip

   # Copy text to the clipboard buffer

   Xclip().selection('clipboard')                                             \
          .filter()                                                           \
          .copy('text')                                                       \
          .stdout                                                             \

   # Get the content of the primary X selection

   Xclip().selection('primary')                                               \
          .paste()                                                            \
          .stdout                                                             \
