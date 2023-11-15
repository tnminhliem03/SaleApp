from flask import redirect
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from flask_login import logout_user, current_user
from App import app, db
from App.models import Category, Product, UserRoleEnum

admin = Admin(app = app, name = 'QUẢN TRỊ BÁN HÀNG', template_mode = 'bootstrap4')

class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated

class MyProductView(AuthenticatedModelView):
    column_list = ['id', 'name', 'price']
    can_export = True
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_editable_list = ['name', 'price']
    details_modal = True
    edit_modal = True

class MyCategoryView(AuthenticatedModelView):
    column_list = ['name', 'products']

class StatsView(AuthenticatedBaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

class LogoutView(AuthenticatedBaseView):
    @expose('/')
    def index(self):
        logout_user()

        return redirect('/admin')

admin.add_view(MyCategoryView(Category, db.session, name = 'Danh mục'))
admin.add_view(MyProductView(Product, db.session, name = 'Sản phẩm'))
admin.add_view(StatsView(name = 'Báo cáo thống kê'))
admin.add_view(LogoutView(name = 'Đăng xuất'))