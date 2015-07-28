# useful URLs
# http://www.discogs.com/stats/contributors?start=0
# http://www.discogs.com/sell/release/509020

class MatchMaker():

    def get_wantlist_items(self, user):
        want_list_items = []
        for i in user.wantlist:
            wantlist_obj = {}
            wantlist_obj['id'] = i.release.id
            wantlist_obj['title'] = i.release.title
            wantlist_obj['year'] = i.release.year
            wantlist_obj['status'] = i.release.status
            wantlist_obj['country'] = i.release.country
            wantlist_obj['data_quality'] = i.release.data_quality
            wantlist_obj['genres'] = i.release.genres
            wantlist_obj['labels'] = i.release.labels
            wantlist_obj['companies'] = "companies"  # i.release.companies
            wantlist_obj['artists'] = i.release.artists
            wantlist_obj['notes'] = "notes"  # i.release.notes
            wantlist_obj['format'] = i.release.formats
            wantlist_obj['credits'] = "credits"  # i.release.credits
            wantlist_obj['tracklist'] = "tracklist"  # i.release.tracklist
            want_list_items.append(wantlist_obj)
        return want_list_items

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
