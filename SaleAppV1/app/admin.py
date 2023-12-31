from flask_admin import Admin, BaseView, expose, AdminIndexView
from app import db, app, dao
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, UserRoleEnums
from flask_login import logout_user, current_user
from flask import redirect


class MyAdminIndex(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html', stats=dao.count_products_by_cate())


admin = Admin(app=app, name="QUẢN LÝ BÁN HÀNG", template_mode="bootstrap4", index_view=MyAdminIndex())


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnums.ADMIN


class MyProductsView(AuthenticatedAdmin):
    column_display_pk = True
    column_list = ['id', 'name', 'price', 'category']
    column_filters = ['price', 'name']
    column_searchable_list = ['name']
    can_view_details = True
    can_export = True
    can_edit = True
    can_delete = True
    column_sortable_list = ['price']


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class MyStatsView(AuthenticatedUser):
    @expose('/')
    def __index__(self, request):
        kw = request.args.get('kw')
        year = request.args.get('year')
        return self.render('admin/stats.html', stats=dao.revenue_stats(kw),
                                                month_stats=dao.revenue_stats_by_month(year))


class MyLogoutView(AuthenticatedUser):
    @expose('/')
    def __index__(self):
        logout_user()
        return redirect('/admin')


admin.add_view(MyCategoryView(Category, db.session))
admin.add_view(MyProductsView(Product, db.session))
admin.add_view(MyStatsView(name="Thống kê báo cáo"))
admin.add_view(MyLogoutView(name='Đăng xuất'))
