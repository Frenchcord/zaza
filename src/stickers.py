class Stickers:
  def __init__(self, stickerinfo: dict):
    self.id: int = stickerinfo['id']
    self.nom = self.name = stickerinfo['name']
    self.type: int = stickerinfo['type']
    self.type_format: int = stickerinfo['format_type']
    self.description: str = stickerinfo['description']
    self.asset: str = stickerinfo['asset']
    self.tags = Tags(stickerinfo['tags'])

class Tags:
  def __init__(self, info):
    self.str: str = info
    self.list: list = info.split(', ')
