from flask import Blueprint
from app.extensions import db
test_bp = Blueprint('test', __name__)

@test_bp.route('/test', methods=['get'])
def register():
    # Implement registration logic here using register_user service
    pass
    try:
        db.session.execute('SELECT 1')
        return '<h1>It works.</h1>'
    except Exception as e:
        return f'<p>The error:<br>{str(e)}</p>'