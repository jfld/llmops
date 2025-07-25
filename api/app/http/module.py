#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2024/4/5 19:03
@Author  : thezehui@gmail.com
@File    : module.py
"""
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_weaviate import FlaskWeaviate
from injector import Module, Binder, Injector
from redis import Redis

from api.internal.extension.database_extension import db
from api.internal.extension.login_extension import login_manager
from api.internal.extension.migrate_extension import migrate
from api.internal.extension.redis_extension import redis_client
from api.internal.extension.weaviate_extension import weaviate
from api.pkg.sqlalchemy import SQLAlchemy


class ExtensionModule(Module):
    """扩展模块的依赖注入"""

    def configure(self, binder: Binder) -> None:
        binder.bind(SQLAlchemy, to=db)
        binder.bind(FlaskWeaviate, to=weaviate)
        binder.bind(Migrate, to=migrate)
        binder.bind(Redis, to=redis_client)
        binder.bind(LoginManager, to=login_manager)


injector = Injector([ExtensionModule])
