class Role:
  def __init__(self, info):
    self.id : int = info['id']
    self.nom = self.name = info['name']
    self.color = self.couleur = info['color']
    self.pin: bool = info['hoist']
    self.position: int = info['position']
    self.permissions: str = info['permissions']
    self.managed: bool = info['managed']
    self.mentionable: bool = info['mentionable']
