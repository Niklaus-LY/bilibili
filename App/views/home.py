# -*- coding:utf-8 -*-

from flask import Blueprint, request, jsonify, render_template


home_blueprint = Blueprint("home", __name__)


@home_blueprint.route("/")
def home():

    return render_template("index.html")


@home_blueprint.route("/api/admin/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        return jsonify({"code": 20000, "data": {"token": "admin-token"}})

@home_blueprint.route("/api/admin/getInfo", methods=["GET", "POST"])
def getInfo():

    if request.method == "GET":
        return jsonify({"code":20000,
                        "data":{"roles":["admin"], "introduction":"I am a super administrator",
                                "avatar":"https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif",
                                "name":"admin"}})


@home_blueprint.route("/logout", methods=["POST"])
def logout():
    if request.method == "POST":
        return jsonify({"code":20000,"data":"success"})