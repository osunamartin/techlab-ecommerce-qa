import requests
from datetime import datetime
from utils.config import BASE_UI_URL

def test_cliente_no_puede_cambiar_estado_pedido():

    session = requests.Session()

    # 1️⃣ login cliente
    login = session.post(
        f"{BASE_UI_URL}/api/auth/login",
        json={
            "email": "juan.perez@email.com",
            "password": "cliente123"
        }
    )

    assert login.status_code == 200

    # 2️⃣ crear pedido
    ahora = datetime.now().isoformat()

    payload_pedido = {
        "usuarioId": 1,
        "lineas": [],
        "estado": "PENDIENTE",
        "total": 500,
        "fechaCreacion": ahora,
        "fechaActualizacion": ahora,
        "items": [
            {
                "productoId": 1,
                "cantidad": 1
            }
        ]
    }

    pedido = session.post(
        f"{BASE_UI_URL}/api/pedidos",
        json=payload_pedido
    )

    assert pedido.status_code in [200, 201]

    pedido_data = pedido.json()

    # 3️⃣ tomar id del pedido recién creado
    pedido_id = pedido_data["id"]

    # 4️⃣ intentar cambiar estado (endpoint admin)
    response = session.patch(
        f"{BASE_UI_URL}/api/pedidos/admin/{pedido_id}/estado",
        params={"estado": "CONFIRMADO"}
    )

    print(response.status_code)
    print(response.text)

    # 5️⃣ validar que cliente no pueda
    assert response.status_code == 403 #Acá falla porque la api deja cambiar el estado del pedido incluso sin logear.

