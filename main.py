from sanic import Sanic, Blueprint
from sanic.response import text

import User.UserBlueprint
from User import UserBlueprint


from atlas import init_db

app = Sanic("SanicExample")
app.blueprint(User.UserBlueprint.user_blueprint)

# Sanic sunucusu başlatılmadan ÖNCE init_db'yi çalıştırıyoruz
@app.before_server_start
async def setup_database(app, loop):
    await init_db()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True, single_process=True)

