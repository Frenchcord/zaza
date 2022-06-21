import requests; from json import loads; from ..package import errors; from ..token import get_token
from .. import pfp
url: str = 'https://discord.com/api/v10'
def get_salon(id: int = None, serveur_id: int = None, nom: str = None):
  from .channels import txt_Channel
  if id is not None:
    r = requests.get(f'{url}/channels/{id}', headers={'authorization': 'Bot ' + get_token()})
    errors.status(r.status_code)
    return txt_Channel(loads(r.content.decode('utf-8')))
  elif id is None and serveur_id is not None and nom is not None:
    r = requests.get(f'{url}/guilds/{serveur_id}/channels', headers={'authorization': 'Bot ' + get_token()})
    errors.status(r.status_code)
    for i in loads(r.content.decode('utf-8')):
      if i['name'] == nom:
        r = requests.get(f'{url}/channels/{i["id"]}', headers={'authorization': 'Bot ' + get_token()})
        errors.status(r.status_code)
        return txt_Channel(loads(r.content.decode('utf-8')))
    raise errors.InvalidChannelName(f'Le salon {nom} n\'existe pas')
  else:
    raise ValueError('Tu dois avoir au moins un id du salon ou un serveur id et un nom')

def get_channel(id: int = None, serveur_id: int = None, nom: str = None):
  from .channels import txt_Channel
  if id is not None:
    r = requests.get(f'{url}/channels/{id}', headers={'authorization': 'Bot ' + get_token()})
    errors.status(r.status_code)
    return txt_Channel(loads(r.content.decode('utf-8')))
  elif id is None and serveur_id is not None and nom is not None:
    r = requests.get(f'{url}/guilds/{serveur_id}/channels', headers={'authorization': 'Bot ' + get_token()})
    errors.status(r.status_code)
    for i in loads(r.content.decode('utf-8')):
      if i['name'] == nom:
        r = requests.get(f'{url}/channels/{i["id"]}', headers={'authorization': 'Bot ' + get_token()})
        errors.status(r.status_code)
        return txt_Channel(loads(r.content.decode('utf-8')))
    raise errors.InvalidChannelName(f'Le salon {nom} n\'existe pas')
  else:
    raise ValueError('Tu dois avoir au moins un id du salon ou un serveur id et un nom')

def get_guild(guild_id):
  from .guild import Guild
  r = requests.get(f'{url}/guilds/{guild_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return Guild(loads(r.content.decode('utf-8')))

def get_serveur(guild_id):
  from .guild import Guild
  r = requests.get(f'{url}/guilds/{guild_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return Guild(loads(r.content.decode('utf-8')))

def get_user(user_id):
  r = requests.get(f'{url}/users/{user_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return User(loads(r.content.decode('utf-8')))

def get_utilisateur(user_id):
  r = requests.get(f'{url}/users/{user_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return User(loads(r.content.decode('utf-8')))

def get_member(member_id, guild_id):
  r = requests.get(f'{url}/guilds/{guild_id}/members/{member_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  content = loads(r.content.decode('utf-8'))
  content['gid'] = guild_id
  return Member(content)

def get_membre(member_id, guild_id):
  r = requests.get(f'{url}/guilds/{guild_id}/members/{member_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  content = loads(r.content.decode('utf-8'))
  content['gid'] = guild_id
  return Member(content)


def get_message(message_id, channel_id):
  from .message import Message
  r = requests.get(f'{url}/channels/{channel_id}/messages/{message_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return Message(loads(r.content.decode('utf-8')))

def get_role(role_id, guild_id):
  from .role import Role
  r = requests.get(f'{url}/guilds/{guild_id}/roles', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  for role in loads(r.content.decode('utf-8')):
    if role['id'] == str(role_id): return Role(role)
  raise ValueError('Id Invalide')

def get_emoji(guild_id, emoji_id):
  from .emojis import Emoji
  r = requests.get(f'{url}/guilds/{guild_id}/emojis/{emoji_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  c = loads(r.content.decode('utf-8'))
  c['gid'] = guild_id
  return Emoji(c)

def get_sticker(sticker_id):
  from .stickers import Stickers
  r = requests.get(f'{url}/stickers/{sticker_id}', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  return Stickers(loads(r.content.decode('utf-8')))
def messageContext(message):
  from .context import Context
  return Context(message)
  
class Member:
  def __init__(self, memberinfo):
    self.avatar = memberinfo['avatar']
    self.nom = self.name = memberinfo['username']
    self.avatar = pfp.pfp(memberinfo['avatar'], memberinfo['id'])
    self.bot = self.robot = memberinfo['bot']
    self.timeout = memberinfo['communication_disabled_until']
    self.nick = memberinfo['nick']
    self.boost_depuis = memberinfo['premium_since']
    self.boost = True if str(memberinfo['premium_since']) != 'null' else False
    self.roles_id = memberinfo['roles']
    self.utilisateur = self.user = User(memberinfo['user'])
    self.mute = memberinfo['mute']
    self.deaf = self.sourd = memberinfo['deaf']
    self.serveur_id = self.guild_id = memberinfo['gid']

  def roles(self):
    self.roles = []
    for i in self.roles_id: self.roles.append(get_role(i, self.serveur_id))
    return self.roles

class User:
  def __init__(self, userinfo: dict):
    self.all = f'{userinfo["username"]}#{userinfo["discriminator"]}'
    self.robot = self.bot = userinfo['bot']
    self.id = userinfo['id']
    self.nom = self.name = userinfo['username']
    self.discriminator = userinfo['discriminator']
    self.avatar = pfp.pfp(userinfo['avatar'], userinfo['id'])
    self.banniere = self.banner = pfp.banner(userinfo['banner'], userinfo['id'])
    self.flags = userinfo['public_flags']

def get_all_roles(guild_id):
  from .role import Role
  r = requests.get(f'{url}/guilds/{guild_id}/roles', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  listee: list = []
  for i in loads(r.content.decode('utf-8')): listee.append(Role(i))
  return listee

def get_all_members(guild_id):
  r = requests.get(f'{url}/guilds/{guild_id}/members', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  listee: list = []
  for i in loads(r.content.decode('utf-8')): listee.append(Member(i))
  return listee

def get_all_channels(guild_id):
  from .channels import txt_Channel
  r = requests.get(f'{url}/guilds/{guild_id}/channels', headers={'authorization': 'Bot ' + get_token()})
  errors.status(r.status_code)
  listee: list = []
  for i in loads(r.content.decode('utf-8')): listee.append(txt_Channel(i))
  return listee
