from flask import Blueprint, render_template, request, redirect, url_for
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido   
from app.models.mesa import Mesa
from main import db

pedidos_bp = Blueprint('pedido', __name__, url_prefix='/pedidos')

@pedidos_bp.route('/pedidos_feitos')
def ver_pedidos_feitos():
    item = Cardapio.query.get_or_404(item_id)
    
    pedido_id = request.args.get("pedido_id")
    pedido = None

    if pedido_id:
        pedido = Pedido.query.get(pedido_id)

    # Se não houver pedido, cria um novo
    if not pedido:
        pedido = Pedido(preco_total=0, observacao="", status="em preparação")
        db.session.add(pedido)
        db.session.commit()

    return render_template('item.html', item=item, pedido=pedido)

@pedidos_bp.route('/adicionar_item', methods=["POST"])
def adicionar_item():
    pedido_id = request.form.get("pedido_id")

    if pedido_id:
        pedido = Pedido.query.get(pedido_id)
    else:
        pedido = Pedido(
            preco_total=0,
            observacao="",
            status="em preparação"
        )
        db.session.add(pedido)
        db.session.commit()

    item_id = request.form.get("item_id")
    quantidade = int(request.form.get("quantidade"))
    preco_unitario = float(request.form.get("preco_unitario"))
    observacao = request.form.get("observacao")

    item = ItemPedido(
        pedido_id=pedido.id,
        cardapio_id=item_id,
        quantidade=quantidade,
        preco_unitario=preco_unitario
    )
    db.session.add(item)
    db.session.commit()

    return redirect(url_for('pedido.confirmar_pedido', pedido_id=pedido.id))

@pedidos_bp.route('/confirmar_pedido/<int:pedido_id>', methods=["GET", "POST"])
def confirmar_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    mesas = Mesa.query.all()

    if request.method == "POST":
        mesa_id = request.form.get("mesa_id")
        pedido.mesa_id = int(mesa_id)
        pedido.status = "concluído"

        total = sum(int(item.quantidade) * float(item.preco_unitario) for item in pedido.itens)
        pedido.preco_total = total

        db.session.commit()
        return redirect("/pedidos/pedidos_feitos")

    return render_template("confirmar_pedido.html", pedido=pedido, mesas=mesas)
@pedidos_bp.route('/editar_pedido')
def editar_pedido_feito():
    return render_template('editar_pedido.html')