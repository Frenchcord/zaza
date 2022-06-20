from ..send import send
from ..token import get_token
from .get import get_salon, get_guild
class Context:
  def __init__(self, msginfo):
    self.message = msginfo
    self.channel_id = self.salon_id = msginfo.channel_id
    self.guild_id = self.serveur_id = msginfo.guild_id


  def send(self, contenu: str = None, content: str = None, *, embeds: list = None, data: bool = True):
    return send(self.channel_id, contenu, content, embeds, get_token(), data)

  def envoyer(self, contenu: str = None, content: str = None, *, embeds: list = None, data: bool = True):
    return send(self.channel_id, contenu, content, embeds, get_token(), data)

  def salon(self):
    return get_salon(self.channel_id)

  def channel(self):
    return get_salon(self.channel_id)

  def guild(self):
    return get_guild(self.guild_id)

  def serveur(self):
    return get_guild(self.guild_id)
