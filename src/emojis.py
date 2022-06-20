class Emoji:
  def __init__(self, emojiinfo: dict):
    self.id: int = emojiinfo['id']
    self.nom = self.name = emojiinfo['name']
    self.roles_id: list = emojiinfo['roles']
    self.serveur_id = self.guild_id = emojiinfo['gid']
    self.anime = self.animated = emojiinfo['animated']
    self.colons: bool = emojiinfo['require_colons']
    self.managed: bool = emojiinfo['managed']
    self.author = self.auteur = EmojiUser(emojiinfo['user'])

  def roles(self):
    from get import get_role
    listee: list = []
    for id in self.roles_id: listee.append(get_role(id, self.guild_id))
    return listee

class EmojiUser:
  def __init__(self, authorinfo):
    self.id: int = authorinfo['id']
    self.nom = self.name = authorinfo['username']
    self.discriminator = authorinfo['discriminator']
    self.all: str = f'{self.name}#{self.discriminator}'
    self.flags: int = authorinfo['public_flags']
    from pfp import pfp
    self.avatar = self.pfp = pfp(authorinfo['avatar'], self.id)

  def user(self):
    from .get import get_user
    return get_user(self.id)
