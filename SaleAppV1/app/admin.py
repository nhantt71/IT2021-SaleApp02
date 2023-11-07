from flask_admin import Admin, BaseView, expose
from app import db, app
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product


admin = Admin(app, name="QUẢN LÝ BÁN HÀNG", template_mode="bootstrap4")


class MyProductsView(ModelView):
    column_display_pk = True
    column_list = ['name', 'price', 'category_id']
    column_filters = ['price', 'name']
    column_searchable_list = ['name']
    can_view_details = True
    can_export = True
    can_edit = True
    can_delete = True
    column_sortable_list = ['price']


class MyStatsView(BaseView):
    @expose('/')
    def __index__(self):
        return self.render('admin/stats.html')


admin.add_view(ModelView(Category, db.session))
admin.add_view(MyProductsView(Product, db.session))
admin.add_view(MyStatsView(name="Thống kê báo cáo"))
