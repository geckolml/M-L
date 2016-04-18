# Ejemplo de OOP en Python. 

import collections

class Vector:
  """Representa un vector en un espacio multidimensional ."""

  def __init__(self, d):
    if isinstance(d, int):
      self._coords = [0] * d
    else:                                  
      try:                                     
        self._coords = [val for val in d]
      except TypeError:
        raise TypeError('tipo de  parametro invalido ')

  def __len__(self):
    """Returna la dimension del vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Returna la  j-coordenada del vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Coloca la j-coordenada  del vector a un valor dado ."""
    self._coords[j] = val

  def __add__(self, otro):
    """Returna la suma de dos  vectores."""
    if len(self) != len(otro):          # se basa en el metodo  __len__ 
      raise ValueError('la dimension  debe ser correcta')
    resultado = Vector(len(self))           # empezamos con vectores ceros 
    for j in range(len(self)):
      resultado[j] = self[j] + otro[j]
    return resultado

  def __eq__(self, otro):
    """Returna True si el vector tiene las mismas coordenadas del otro vector ."""
    return self._coords == otro._coords

  def __ne__(self, otro):
    """Returna True si los vectores difieren uno de otro ."""
    return not self == otro             # se basa en  __eq__ 

  def __str__(self):
    """Produce una representation como cadena del vector ."""
    return '<' + str(self._coords)[1:-1] + '>'  

  def __neg__(self):
    """Returna una  copia del vector con las coordenadas  son negativas ."""
    resultado = Vector(len(self))           # empezamos con vectores ceros
    for j in range(len(self)):
      resultado[j] = -self[j]
    return resultado

  def __lt__(self, otro):
    """Compara vectores basados en el orden  lexicografico ."""
    if len(self) != len(otro):
      raise ValueError('la dimension debe ser correcta')
    return self._coords < otro._coords

  def __le__(self, otro):
    """Compara vectores basados en el orden lexicografico."""
    if len(self) != len(otro):
      raise ValueError('la dimension debe ser correcta')
    return self._coords <= otro._coords

if __name__ == '__main__':
  # uso de los metodos
  v = Vector(5)              
  v[1] = 27                 
  v[-1] = 40                 
  print(v[4])                
  u = v + v                  
  print(u)                   
  total = 0
  for entrada in v:            
    total += entrada
  print(total)
