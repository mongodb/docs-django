The |model-classes| an inner ``Meta`` class and a ``__str__()`` method.
To learn about these model features, see :ref:`django-models-define` in the
Create Models guide.

Run Code Examples
`````````````````

You can use the Python interactive shell to run the code examples.
To enter the shell, run the following command from your project's 
root directory:

.. code-block:: bash

   python manage.py shell

After entering the Python shell, ensure that you import the following models and
modules:

.. code-block:: python

   |model-imports|
   from {+framework+}.utils import timezone
   from datetime import datetime

To learn how to create a {+framework+} application that uses the ``Movie``
model and the Python interactive shell to interact with MongoDB documents,
visit the :ref:`django-get-started` tutorial.