# useful URLs
# http://www.discogs.com/stats/contributors?start=0
# http://www.discogs.com/sell/release/509020

class MatchMaker():

    def get_wantlist_items(self, user):
        wantlist = user.wantlist
        return wantlist

    def get_collection_folders(self, user):
        folders = user.collection_folders
        return folders

    def get_listing_items(self, user):
        listing_items = user.inventory
        return listing_items

    def get_wantlist_matches(self, user1, user2):
        return {}

    def get_listing_matches(self, user1, user2):
        return {}

    def set_dict_key(self, key, value):
        self.dict[key] = value

    def get_dict_key(self, key):
        return self.dict[key]

    def get_items(self):
        return self.dict.iteritems()

    def __repr__(self):
        return '<MatchMaker %r>' % self.name

    def __init__(self):
        self.dict = {}
