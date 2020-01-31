from abc import ABC, abstractmethod

class InvalidOperationError(Exception):
  pass

class Stream(ABC):
  def __init__(self):
    self.opened = False

  def open(self):
    if self.opened:
      raise InvalidOperationError("already opened")
    self.opened = True
  
  def close(self):
    if not self.opened:
      raise InvalidOperationError("already closed")
    self.opened = False
  
  @abstractmethod
  def read(self):
    pass

class FileStream(Stream):
  def read(self):
    print("reading file")

f = FileStream()
f.open()
f.read()