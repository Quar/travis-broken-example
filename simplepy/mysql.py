import pymysql.cursors
import yaml
import pandas as pd

default_cfg = {'cursorclass':pymysql.cursors.DictCursor}

def read_config(cfg_file):
    with open(cfg_file) as f:
        cfg = yaml.load(f)['mysql']
    return cfg

def get_conn(cfg_file):
    user_cfg = read_config(cfg_file)
    cfg = {**default_cfg, **(user_cfg or {})}
    return pymysql.connect(**cfg)

def query(conn, query):
    with conn.cursor() as cursor:
        cursor.execute(query)
        result = cursor.fetchall()
        return pd.DataFrame(result)