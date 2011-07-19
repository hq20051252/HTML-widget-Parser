import _mysql
querystring = """select * from t_cnsoccerway_players"""
def opendb(user = "remote",passwd = "qwer5678()_+", database = "qiud_materials_db"):
    db = _mysql.connect("119.40.35.7",user,passwd,database)
    return db
