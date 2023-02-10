"""The initialization of the `storage` variable
`FileStorage` for the web app

The `__objects` class attribute of the `FileStorage`
class is loaded with objects on the `__file_path`
class attribute of the `FileStorage` class.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
