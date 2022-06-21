from .get import get_salon, get_member, get_all_members, get_all_channels, get_all_roles
from .. import pfp
from .role import Role
from ..pfp import guild_icon, invite_blackground
class Guild:
  def __init__(self, guildinfo):
    self.id: int = guildinfo['id']
    self.nom = self.name = guildinfo['name']
    self.desc = self.description = guildinfo['description']
    self.icon = guild_icon(guildinfo['icon'], guildinfo['id'])
    self.splash = self.arriere_invitation = self.invite_background = invite_blackground(guildinfo['splash'], guildinfo['id'])
    self.splash_decouverte = pfp.splash_dec(guildinfo['discovery_splash'])
    self.region = guildinfo['region']
    self.proprio_id = self.owner_id = guildinfo['owner_id']
    self.banner = self.banniere = pfp.banner(guildinfo['banner'], guildinfo['id'])
    listee: list = []
    for i in guildinfo['emojis']: listee.append(Emoji(i))
    self.emojis: list = listee
    self.afk_channel_id = guildinfo['afk_channel_id']
    self.widget = guildinfo['widget_enabled']
    self.widget_channel_id = guildinfo['widget_channel_id']
    self.system_salon_id = self.system_channel_id = guildinfo['system_channel_id']
    self.features = [f.lower() for f in guildinfo['features']]
    listee: list = []
    for i in guildinfo['stickers']: listee.append(Stickers(i))
    self.stickers: list = listee


    self.verification_level = self.niveau_verification = guildinfo['verification_level']
    self.roles: list = []
    for i in guildinfo['roles']:
      self.roles.append(Role(i))
    self.notif = guildinfo['default_message_notifications']
    self.mfa_niveau = self.mfa_level = guildinfo['mfa_level']
    self.filtre = self.filter = guildinfo['explicit_content_filter']
    self.max_presence = guildinfo['max_presences']
    self.membres_max = self.max_members = guildinfo['max_members']
    self.max_video = guildinfo['max_video_channel_users']
    self.url = guildinfo['vanity_url_code']
    self.niveau_boost = self.premium_tier = guildinfo["premium_tier"]
    self.boosts = guildinfo['premium_subscription_count']
    self.system_salon_flags = self.system_channel_flags = guildinfo['system_channel_flags']
    self.local = self.locale = guildinfo['preferred_locale']
    self.rules_channel_id = self.salon_regles_id = guildinfo['rules_channel_id']
    self.public_updates_channel_id = self.salon_mise_a_jour_public_id = guildinfo['public_updates_channel_id']
    self.hub_type = guildinfo['hub_type']
    self.boost_bar = guildinfo['premium_progress_bar_enabled']
    self.nsfw = guildinfo['nsfw']
    self.nsfw_niveau = self.nsfw_level = guildinfo['nsfw_level']

  def salon_mise_a_jour_public(self):
    return get_salon(self.public_updates_channel_id)

  def salon_mise_a_jour(self):
    return get_salon(self.public_updates_channel_id)

  def rules_channel(self):
    return get_salon(self.rules_channel_id)

  def salon_regles(self):
    return get_salon(self.rules_channel_id)
    
  def afk_channel(self):
    return get_salon(self.afk_channel_id)

  def afk_salon(self):
    return get_salon(self.afk_channel_id)

  def owner(self):
    return get_member(self.owner_id)

  def proprio(self):
    return get_member(self.owner_id)

  def members(self):
    return get_all_members(self.id)

  def membres(self):
    return get_all_members(self.id)

  def salons(self):
    return get_all_channels(self.id)

  def channels(self):
    return get_all_channels(self.id)

  def roles(self):
    return get_all_roles(self.id)
