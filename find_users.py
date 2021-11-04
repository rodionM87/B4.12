import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class Athelete(Base):
    __tablename__ = "athelete"
    id = sa.Column(sa.Integer, primary_key=True)
    age = sa.Column(sa.Integer)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)

class User(Base):
    __tablename__ = "user"
    id = sa.Column(sa.String(36), primary_key=True)
    first_name = sa.Column(sa.Text)
    last_name = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    email = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    height = sa.Column(sa.REAL)

def connect_db():
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()

def request_data():
    print("enter id to find nearest ")
    id_number = input("enter id number: ")
    return int(id_number)

def find_user_by_br(user_id, session):

    find_id = session.query(Athelete).all()
    var_with_br = [name.birthdate for name in find_id]

    # print(user_id.birthdate)

    more_trg_br = []
    less_trg_br = []
    target_usr_br = user_id.birthdate
    for br in var_with_br:
        if br < target_usr_br:
            less_trg_br.append(br)
        elif br > target_usr_br:
            more_trg_br.append(br)

    temp_var_ls = less_trg_br[0]
    for less_data in less_trg_br:
        if less_data > temp_var_ls:
            temp_var_ls = less_data

    temp_var_mr = more_trg_br[0]
    for more_data in more_trg_br:
        if more_data < temp_var_mr:
            temp_var_mr = more_data

    for i in find_id:
        if i.birthdate == temp_var_ls:
            athlete_ls_n = i.name
        elif i.birthdate == temp_var_mr:
            athlete_mr_n = i.name

    tar_name = user_id.name

    target_athlete = "Athlete's who nearest for birthdate, target athlete {tar_name} {tar_birth} older than {name_ls} {birthdate_ls} and younger than {name_mr} {birthdate_mr}"\
        .format(tar_name=tar_name, tar_birth=target_usr_br, name_ls=athlete_ls_n, birthdate_ls=temp_var_ls, name_mr=athlete_mr_n, birthdate_mr=temp_var_mr)
    return target_athlete

def find_user_by_hr(user_id, session):
    find_id = session.query(Athelete).all()
    var_with_hr = [name.height for name in find_id]

    if user_id.height == None:
        print("athlete not have data with height")
        return None
    else:
        target_usr_hr = user_id.height

    more_trg_hr = []
    less_trg_hr = []
    for br in var_with_hr:
        if br == None:
            continue
        elif br < target_usr_hr:
            less_trg_hr.append(br)
        elif br > target_usr_hr:
            more_trg_hr.append(br)

    temp_var_ls = less_trg_hr[0]
    for less_data in less_trg_hr:
        if less_data > temp_var_ls:
            temp_var_ls = less_data

    temp_var_mr = more_trg_hr[0]
    for more_data in more_trg_hr:
        if more_data < temp_var_mr:
            temp_var_mr = more_data

    for i in find_id:
        if i.height == temp_var_ls:
            athlete_ls_hr = i.name
        elif i.height == temp_var_mr:
            athlete_mr_hr = i.name

    tar_name = user_id.name

    target_athlete = "Athlete's who nearest for height, target athlete {tar_name} {tar_heigth} taller than {name_ls} {heidht_ls} and shorter than {name_mr} {heidht_mr}" \
        .format(tar_name=tar_name, tar_heigth=target_usr_hr, name_ls=athlete_ls_hr, heidht_ls=temp_var_ls, name_mr=athlete_mr_hr, heidht_mr=temp_var_mr)

    return target_athlete

def main():
    session = connect_db()
    id_number = request_data()
    athelete_id = session.query(Athelete).filter(Athelete.id == id_number).first()
    if not athelete_id:
        print("userID not found")
    else:
        user_nearest_by_br = find_user_by_br(athelete_id, session)
        user_nearest_by_hr = find_user_by_hr(athelete_id, session)
        print(user_nearest_by_br)
        print(user_nearest_by_hr)

if __name__ == "__main__":
    main()





