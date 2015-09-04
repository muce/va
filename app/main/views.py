from flask import request, render_template, flash, url_for, session, redirect

from flask.ext.login import login_required, current_user
from forms import EditProfileForm
from . import main
from models import MatchMaker
from ..models import *
from config import *
from discogs_client import *
from splinter import Browser
import ssl
import urllib2


mm = MatchMaker()


@main.route('/')
def index():
    app = current_app._get_current_object()
    conf = app.config

    mm.set_dict_key('user_agent', conf['DISCOGS_USER_AGENT'])
    mm.set_dict_key('consumer_key', conf['DISCOGS_CONSUMER_KEY'])
    mm.set_dict_key('consumer_secret', conf['DISCOGS_CONSUMER_SECRET'])
    mm.set_dict_key('callback_url', conf['DISCOGS_CALLBACK_URL'])
    d = Client(mm.get_dict_key('user_agent'))
    d.set_consumer_key(mm.get_dict_key('consumer_key'), mm.get_dict_key('consumer_secret'))

    while True:
        try:
            resp = d.get_authorize_url(callback_url = mm.get_dict_key('callback_url'))
            break
        except ssl.SSLError:
            print "ssl.SSLError at resp = d.get_authorize_url(callback_url = mm.get_dict_key('callback_url'))"

    mm.set_dict_key('request_token', resp[0])
    mm.set_dict_key('request_secret', resp[1])
    mm.set_dict_key('authorise_url', resp[2])
    mm.set_dict_key('client', d)

    return redirect(mm.get_dict_key('authorise_url'))


@main.route('/authorised')
def discogs_authorised():
    app = current_app._get_current_object()
    d = mm.get_dict_key('client')

    mm.set_dict_key('verifier', request.args['oauth_verifier'])
    at = d.get_access_token(mm.get_dict_key('verifier'))
    mm.set_dict_key('access_token', at[0])
    mm.set_dict_key('access_secret', at[1])

    me = d.identity()
    u = d.user(me.username)

    mm.set_dict_key('client', d)

    return render_template('verified.html',
                            user = u,
                            main_menu_url = 'http://localhost:5000/menu')


@main.route('/discogs/me')
def discogs_me():
    app = current_app._get_current_object()
    d = mm.get_dict_key('client')
    me = d.identity()

    return render_template('me.html',
                            page_name = 'me.html',
                            me = me)


@main.route('/discogs/wantlist')
def discogs_wantlist():
    app = current_app._get_current_object()
    d = mm.get_dict_key('client')
    me = d.identity()
    u = d.user(me.username)

    while True:
        try:
            wantlist = mm.get_wantlist_items(d.identity())
            wantlist_len = len(wantlist)
            break
        except ssl.SSLError:
            print "SSLError at wantlist = mm.get_wantlist_items(me)"

    return render_template('wantlist.html',
                            page_name = 'wantlist.html',
                            user_agent = mm.get_dict_key('user_agent'),
                            wantlist = wantlist,
                            wantlist_len = wantlist_len)


@main.route('/discogs/collection')
def discogs_collection():
    collection = {'item1': 'dsfdsf', 'item2': 'dsgdsgds'}
    collection_len = len(collection)
    return render_template('discogs_user.html',
                           collection = collection,
                           collection_len = collection_len)


@main.route('/discogs/users')
def discogs_users():
    discogs_users = ['sousoudaddy', 'scientistindubwise', 'blackcat_records', 'theory-x', 'xpe74', 'jillchal']
    return render_template('discogs_users.html',
                           discogs_users = discogs_users)


@main.route('/discogs/tokens')
def discogs_tokens():
    app = current_app._get_current_object()
    d = mm.get_dict_key('client')

    return render_template('tokens.html',
                            page_name = 'tokens.html',
                            mm_items = mm.get_items())


@main.route('/menu')
def discogs_menu():
    app = current_app._get_current_object()
    d = mm.get_dict_key('client')

    return render_template('main_menu.html',
                            user_agent = mm.get_dict_key('user_agent'),
                            page_name = 'main_menu.html',
                            wantlist_url = '/wantlist',
                            collectionlist_url = 'collectionlist_url',
                            salelist_url = 'salelist_url',
                            matchlist_url = 'matchlist_url',
                            other_url = 'other_url')


@main.route('/discogs/user/<username>')
def discogs_user(username):
    d = mm.get_dict_key('client')
    u = d.user(username)

    collection = mm.get_collection_folders(u)
    wantlist = mm.get_wantlist_items(u)
    listings = mm.get_listing_items(u)

    return render_template('discogs_user.html',
                            d=str(d),
                            u=u,
                            wantlist=wantlist,
                            listings=listings,
                            collection=collection,
                            num_listings=len(u.inventory),
                            num_collection=u.num_collection,
                            num_wantlist=len(u.wantlist))


# list all sellers with the release <release_id>
@main.route('/discogs/sellers/<release_id>')
def discogs_sellers(release_id):
    u = 'http://www.discogs.com/sell/release/'
    return 'discogs_sellers ' + u + str(release_id)


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('user.html', user=user)


@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)
