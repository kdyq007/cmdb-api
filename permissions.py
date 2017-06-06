# -*- coding:utf-8 -*- 


from flask_principal import RoleNeed, Permission


admin = Permission(RoleNeed('admin'))
auth = Permission(RoleNeed('authenticated'))
null = Permission(RoleNeed('null'))