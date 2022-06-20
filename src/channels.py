from .get import get_guild
from .. import send
from ..token import get_token
class txt_Channel:
  def __init(self, channelinfo: dict):
    self.nsfw = channelinfo['nsfw']
    self.type = channelinfo['type']
    self.permission: list = []
    for i in channelinfo['permission_overwrites']: self.permission.append(ChannelPerm(i))
    self.flags = channelinfo['flags']
    self.nom = self.name = channelinfo['name']
    self.position = channelinfo['name']
    self.categorie_id = self.category_id = channelinfo['parent_id']
    self.guild_id = self.serveur_id = channelinfo['guild_id']

  def guild(self):
    return get_guild(self.guild_id)

  def serveur(self):
    return get_guild(self.guild_id)

  def send(self, contenu: str = None, content: str = None, *, embeds: list = None, token: str = None):
    return send.send(contenu = contenu, content = content, embeds = embeds, token=get_token() if token is None else token)

class ChannelPerm:
  def __init__(self, permlist):
    self.id = permlist['id']
    self.type = permlist['type']
    self.permis = self.allow = permlist['allow']
    self.non_permis = self.deny = permlist['deny']
