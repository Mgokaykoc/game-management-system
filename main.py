from sanic import Sanic, Blueprint
from sanic.response import text
from sanic_cors import CORS
import User.UserBlueprint
from User import UserBlueprint
import game.GameBlueprint


from atlas import init_db

app = Sanic("SanicExample")

CORS(app)
app.blueprint(User.UserBlueprint.user_blueprint)


app.blueprint(User.UserBlueprint.user_blueprint)
app.blueprint(game.GameBlueprint.bp)


# Sanic sunucusu başlatılmadan ÖNCE init_db'yi çalıştırıyoruz
@app.before_server_start
async def setup_database(app, loop):
    await init_db()


if __name__ == '__main__':

    app.run(host="0.0.0.0", port=8000, debug=True, single_process=True)

