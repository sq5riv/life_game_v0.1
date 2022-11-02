from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import render_template, url_for


root = Blueprint('root', __name__, description='Main page operations')
user = Blueprint('user', __name__, description='user operations')
card = Blueprint('card', __name__, description='card operations')
deck = Blueprint('deck', __name__, description='deck operations')
rules = Blueprint('rules', __name__, description='rules operations')
game = Blueprint('game', __name__, description='game operations')


@root.route('/')
class Main_page(MethodView):
    def get(self):
        return render_template('index.html')

@user.route('/login')
class User_ops(MethodView):
    def get(self):
        return 'Login Page'
    def post(self):
        return 'Loged in XD'
    def delete(self):
        return 'Logout XD'

@user.route('/new_user')
class New_user(MethodView):
    def get(self):
        return 'Get user info'
    def post(self):
        return 'Add new user to database'
    def put(self):
        return 'Update user in database'
    def delete(self):
        return 'delete user from database'

@card.route('/card')
class Cards(MethodView):
    def get(self):
        return 'returns cards list'
    def post(self):
        return 'add new card to database'

@card.route('/cards/<string:card_id>')
class Card(MethodView):
    def get(self, card_id):
        return 'card number {}'.format(card_id)
    def put(self, card_id):
        return 'update card {}'.format(card_id)
    def delete(self, card_id):
        return 'delete card {}'.format(card_id)

@rules.route('/rules')
class Rules(MethodView):
    def get(self):
        return 'list of rules'
    def post(self):
        return 'add new ruleset to database'

@rules.route('/rules/<string:rules_id>')
class Rules(MethodView):
    def get(self, rules_id):
        return 'get ruleset {}'.format(rules_id)
    def put(self, rules_id):
        return 'update ruleset {} in database'.format(rules_id)
    def delete(self, rules_id):
        return 'delete ruleset {}'.format(rules_id)

@game.route('/game')
class Games(MethodView):
    def get(self):
        return 'list of games'
    def post(self):
        return 'Save game, returns game id'
@game.route('/game/<string:game_id>')
class Game(MethodView):
    def get(self, game_id):
        return 'Gets game state from game {}'.format(game_id)
    def put(self, game_id):
        return 'Overwrite game {}'.format(game_id)
    def delete(self, game_id):
        return 'Delete game {}'.format(game_id)