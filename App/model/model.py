# -*- coding:utf-8 -*-

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import LONGTEXT

db = SQLAlchemy()


class Video(db.Model):

    __tablename__ = "video"

    id = db.Column(db.INT, primary_key=True, autoincrement=True)
    title = db.Column(db.VARCHAR(100), nullable=False)
    author = db.Column(db.VARCHAR(50), nullable=True)
    like_count = db.Column(db.Float, nullable=False)
    coin_count = db.Column(db.Float, nullable=False)
    collect_count = db.Column(db.Float, nullable=False)
    view_count = db.Column(db.Float, nullable=False)
    dm_count = db.Column(db.Float, nullable=False)
    bv = db.Column(db.VARCHAR(20), nullable=False)
    dm = db.Column(LONGTEXT, nullable=True)

