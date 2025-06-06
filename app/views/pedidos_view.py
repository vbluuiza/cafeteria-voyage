from flask import Blueprint, render_template, request, redirect, url_for, session, current_app
import threading, time
from sqlalchemy.orm import joinedload
from app.models.pedido import Pedido
from app.models.mesa import Mesa
from app.models.item_pedido import ItemPedido   
from app.models.cardapio import Cardapio
from app.models.mesa import Mesa
from main import db

pedidos_bp = Blueprint('pedido', __name__, url_prefix='/pedidos')

@pedidos_bp.route('/pedidos_feitos')
def ver_pedidos_feitos():
    
    pedidos = Pedido.query.options(
        joinedload(Pedido.mesa),
        joinedload(Pedido.itens).joinedload(ItemPedido.cardapio)
    ).order_by(Pedido.id.desc()).all()

    return render_template('pedidos_feitos.html', pedidos=pedidos)

@pedidos_bp.route('/adicionar_item', methods=["POST"])
def adicionar_item():
    pedido_id = request.form.get("pedido_id", type=int)
    item_id = request.form.get("item_id", type=int)
    quantidade = request.form.get("quantidade", type=int)
    preco_unitario = request.form.get("preco_unitario", type=float)
    observacao = request.form.get("observacao", "")
    opcional_escolhido = request.form.get("opcional_escolhido")

    if pedido_id:
        pedido = Pedido.query.get_or_404(pedido_id)
    else:
        pedido = Pedido(preco_total=0, status="em preparação")
        db.session.add(pedido)
        db.session.commit()

    item = ItemPedido(
        pedido_id=pedido.id,
        cardapio_id=item_id,
        quantidade=quantidade,
        preco_unitario=preco_unitario,
        observacao=observacao,
        opcional_escolhido=opcional_escolhido
    )
    db.session.add(item)

    pedido.preco_total += preco_unitario * quantidade
    db.session.commit()

    return redirect(
        url_for('pedido.confirmar_pedido', pedido_id=pedido.id)
    )

@pedidos_bp.route('/confirmar_pedido/<int:pedido_id>', methods=["GET", "POST"])
def confirmar_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    mesas = Mesa.query.options(joinedload(Mesa.pedidos)).all()

    if request.method == "POST":
        pedido.mesa_id = request.form.get("mesa_id", type=int)
        pedido.status = "pedido realizado"
        db.session.commit()
        
        app = current_app._get_current_object()

        def atualizar_em_background(app, pedido_id):
            with app.app_context():
                time.sleep(30)
                pedido_atualizado = Pedido.query.get(pedido_id)

                if pedido_atualizado:
                    pedido_atualizado.status = "em preparação"
                    db.session.commit()

                time.sleep(30)
                pedido_atualizado = Pedido.query.get(pedido_id)
                if pedido_atualizado:
                    pedido_atualizado.status = "concluído"
                    db.session.commit()

        threading.Thread(target=atualizar_em_background, args=(app, pedido_id)).start()

        return redirect(url_for('pedido.ver_pedidos_feitos'))

    return render_template(
        'confirmar_pedido.html',
        pedido=pedido, mesas=mesas
    )

@pedidos_bp.route('/cancelar_pedido/<int:pedido_id>')
def cancelar_pedido(pedido_id):
    pedido = Pedido.query.get_or_404(pedido_id)
    pedido_numero = pedido.id 

    for item in pedido.itens:
        db.session.delete(item)

    db.session.delete(pedido)
    db.session.commit()

    return redirect(url_for('pedido.ver_pedidos_feitos'))
 
 