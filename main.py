from sanic import Sanic
from sanic.response import text

from atlas import init_db

app = Sanic("SanicExample")

# Sanic sunucusu başlatılmadan ÖNCE init_db'yi çalıştırıyoruz
@app.before_server_start
async def setup_database(app, loop):
    await init_db()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)

