from .. import pfp
from .get import get_user, get_role, get_guild, get_salon
from ..send import send
from ..token import get_token
class Message:
  def __init__(self, msginfo):
    self.author = self.auteur = Author(msginfo['author'])
    self.id: int = msginfo['id']
    self.type: int = msginfo['type']
    self.contenu = self.content = msginfo['content']
    self.guild_id = self.serveur_id = msginfo['guild_id'] if 'guild_id' in msginfo else None
    self.mention = Mention(msginfo['mentions'], msginfo['mention_roles'], self.guild_id)
    self.pinned = self.pin = msginfo['pinned']
    self.attachements = self.attachments = len(msginfo['attachments'])
    self.ping_everyone = msginfo['mention_everyone']
    self.tts = msginfo['tts']
    self.timestamp = msginfo['timestamp']
    self.edited = True if msginfo['edited_timestamp'] is not None else False
    self.flags = msginfo['flags']
    self.salon_id = self.channel_id = msginfo['channel_id']

  def salon(self):
    return get_salon(self.salon_id)

  def channel(self):
    return get_salon(self.salon_id)

  def guild(self):
    if self.guild_id is None: raise ValueError('C\'est un dm')
    return get_guild(self.guild_id)

  def serveur(self):
    if self.guild_id is None: raise ValueError('C\'est un dm')
    return get_guild(self.guild_id)

  def send(self, contenu: str = None, content: str = None, *, embeds: list = None, data: bool = True):
    return send(self.channel_id, contenu, content, embeds, get_token(), data)

  def envoyer(self, contenu: str = None, content: str = None, *, embeds: list = None, data: bool = True):
    return send(self.channel_id, contenu, content, embeds, get_token(), data)

class Mention:
  def __init__(self, person, roles, gid):
    listee: list = []
    for i in person: listee.append(MentionPerson(i))
    self.person = self.human = self.humain = listee
    self.roles_id = [role['id'] for role in roles]
    self.gid = gid

  def roles(self):
    if self.gid is None: raise ValueError('Les dms n\'ont pas de roles')
    return [get_role(id, self.gid) for id in self.roles_id]

class MentionPerson:
  def __init__(self, info):
    self.id = info['id']
    self.nom = self.name = info['username']
    self.discriminator = info['discriminator']
    self.all = f'{self.name}#{self.discriminator}'
    self.flags = info['public_flags']
    self.avatar = self.pfp = pfp.pfp(info['avatar'], self.id)
    self.avatar_decoration = info['avatar_decoration']
    self.bot = info['bot']

  def user(self):
    return get_user(self.id)

  def utilisateur(self):
    return get_user(self.id)
    
class Author:
  def __init__(self, authorinfo):
    self.id = authorinfo['id']
    self.nom = self.name = authorinfo['username']
    self.discriminator = authorinfo['discriminator']
    self.all = f'{self.name}#{self.discriminator}'
    self.flags = authorinfo['public_flags']
    self.avatar = self.pfp = pfp.pfp(authorinfo['avatar'], self.id)
    self.avatar_decoration = authorinfo['avatar_decoration']

  def user(self):
    return get_user(self.id)

  def utilisateur(self):
    return get_user(self.id)
