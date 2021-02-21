# -*- coding:utf-8 -*-

from flask import Blueprint, request, jsonify
from sqlalchemy import func

from model.model import db, Video
from utils.word_count import word_count


api_blueprint = Blueprint("api", __name__,
                           url_prefix="/api")

@api_blueprint.route("/rose/get_list/")
def data_info():

    rows_count = Video.query.count()
    columns_count = len(Video.__table__.columns)  # 需要操作table实例
    like_max = db.session.query(func.max(Video.like_count)).scalar()
    coin_max = db.session.query(func.max(Video.coin_count)).scalar()
    collect_max = db.session.query(func.max(Video.collect_count)).scalar()
    view_max = db.session.query(func.max(Video.view_count)).scalar()/10

    print(type(view_max))
    dm_max = db.session.query(func.max(Video.dm_count)).scalar()

    return jsonify({"code": 20000,
                    "data": [
                        {"type": "记录数", "value": rows_count},
                        {"type": "字段数", "value": columns_count},
                        {"type": "最多点赞数", "value": like_max},
                        {"type": "最多投币数", "value": coin_max},
                        {"type": "最多收藏数", "value": collect_max},
                        {"type": "最多浏览人数", "value": view_max},
                        {"type": "最多弹幕数", "value": dm_max}
                    ]})


@api_blueprint.route("/funnel/retrieve/", methods=["GET"])
def funnel_retrieve():
    """TopN路由"""
    _count = request.args.get("count")
    _type = request.args.get("type")
    # _count = 100
    # _type = "view_count"
    videos = Video.query.order_by(db.desc(_type)).limit(_count).values(Video.title, _type)

    data = []
    for v in videos:
        data.append({"title": v[0], "number": v[1]})

    return jsonify({"code": 20000, "data": data})


@api_blueprint.route("/video/get_list/", methods=["GET"])
def video_getlist():
    videos = db.session.query(Video.title, Video.author, Video.like_count,
                                           Video.coin_count, Video.collect_count,
                                           Video.view_count, Video.dm_count, Video.bv)
    items = []
    for v in videos:
        item = {"title": v.title,
                "author": v.author,
                "like_count": v.like_count,
                "coin_count": v.coin_count,
                "collect_count": v.collect_count,
                "view_count": v.view_count,
                "dm_count": v.dm_count,
                "bv": v.bv }
        items.append(item)
    return jsonify({"code": 20000,
                    "data": {"items": items}})


@api_blueprint.route("/video/retrieve/", methods=["GET"])
def video_retrieve():
    author = request.args.get("author")
    v = Video.query.filter_by(author=author).first()
    item = [{"title": v.title,
            "author": v.author,
            "like_count": v.like_count,
            "coin_count": v.coin_count,
            "collect_count": v.collect_count,
            "view_count": v.view_count,
            "dm_count": v.dm_count,
            "bv": v.bv}]

    return jsonify({"code": 20000,
                    "data": {"items": item}})


@api_blueprint.route("/video/wordcloud/", methods=["GET", "POST"])
def video_wordcloud():
    # id = request.args.get("id")
    id = 1000
    v = Video.query.with_entities(Video.dm).filter_by(id=id).first()
    if not v:
        return jsonify({"code": 20000, "data": "id不存在"})

    string = v.dm
    wc_dict = word_count(string)

    wc_list = sorted(wc_dict.items(), key=lambda x: x[1], reverse=True)

    data = []
    for w in wc_list:
        d_w = {"value": w[1], "name": w[0]}
        data.append(d_w)

    return jsonify({"code": 20000, "data": data})


