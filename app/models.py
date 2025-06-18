from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Khoa(db.Model):
    __tablename__ = 'khoa'
    khoaid = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(255))
    mota = db.Column(db.String(255))

class nguoidung(db.Model):
    __tablename__ = 'nguoidung'
    userid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    hovaten = db.Column(db.String(255))
    gioitinh = db.Column(db.String(255))
    diachi = db.Column(db.String(255))
    sodienthoai = db.Column(db.String(255))
    email = db.Column(db.String(255))
    anhdaidien = db.Column(db.LargeBinary)
    vitri = db.Column(db.String(255))
    khoaid = db.Column(db.Integer, db.ForeignKey('khoa.khoaid'))

class TruongKhoa(db.Model):
    __tablename__ = 'truongkhoa'
    truongkhoaid = db.Column(db.Integer, db.ForeignKey('nguoidung.userid'), primary_key=True)

class truongbomon(db.Model):
    __tablename__ = 'truongbomon'
    truongbomonid = db.Column(db.Integer, db.ForeignKey('nguoidung.userid'), primary_key=True)

class bomon(db.Model):
    __tablename__ = 'bomon'
    bomonid = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(255))
    mota = db.Column(db.String(255))

class giangvien(db.Model):
    __tablename__ = 'giangvien'
    giangvienid = db.Column(db.Integer, db.ForeignKey('nguoidung.userid'), primary_key=True)
    tongcongviec = db.Column(db.Integer)
    congviechoanthanh = db.Column(db.Integer)
    tilehoanthanh = db.Column(db.Float)
    bomonid = db.Column(db.Integer, db.ForeignKey('bomon.bomonid'))

class phanconggiangday(db.Model):
    __tablename__ = 'phanconggiangday'
    phanconggiangdayid = db.Column(db.Integer, primary_key=True)
    monhocid = db.Column(db.Integer, db.ForeignKey('monhoc.monhocid'))
    giangvienid = db.Column(db.Integer, db.ForeignKey('giangvien.giangvienid'))
    vaitro = db.Column(db.String(255))

class kyhoc(db.Model):
    __tablename__ = 'kyhoc'
    kyhocid = db.Column(db.Integer, primary_key=True)
    thoidiem = db.Column(db.String(255))

class monhoc(db.Model):
    __tablename__ = 'monhoc'
    monhocid = db.Column(db.Integer, primary_key=True)
    ten = db.Column(db.String(255))
    mamon = db.Column(db.String(255))
    sochuong = db.Column(db.Integer)
    socauhoide = db.Column(db.Integer)
    socauhoikho = db.Column(db.Integer)
    socauhoi = db.Column(db.Integer)
    bomonid = db.Column(db.Integer, db.ForeignKey('bomon.bomonid'))

class kyhocmonhoc(db.Model):
    __tablename__ = 'kyhocmonhoc'
    kyhoc_id = db.Column(db.Integer, db.ForeignKey('kyhoc.kyhocid'), primary_key=True)
    monhocid = db.Column(db.Integer, db.ForeignKey('monhoc.monhocid'), primary_key=True)

class congviec(db.Model):
    __tablename__ = 'congviec'
    congviecid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    noidung = db.Column(db.String(255))
    soluongcauhoi = db.Column(db.Integer)
    truongbomonid = db.Column(db.Integer, db.ForeignKey('truongbomon.truongbomonid'))
    monhocid = db.Column(db.Integer, db.ForeignKey('monhoc.monhocid'))

class chitietcongviec(db.Model):
    __tablename__ = 'chitietcongviec'
    phancongid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    giangvienid = db.Column(db.Integer, db.ForeignKey('giangvien.giangvienid'))
    congviecid = db.Column(db.Integer, db.ForeignKey('congviec.congviecid'))
    ghichu = db.Column(db.String(255))
    ngayphancong = db.Column(db.Date)
    trangthai = db.Column(db.String(255))

class cautrucdethi(db.Model):
    __tablename__ = 'cautrucdethi'
    cautrucdethiid = db.Column(db.Integer, primary_key=True)
    tencautruc = db.Column(db.String(255))
    socauhoi = db.Column(db.Integer)
    tilenhanbiet = db.Column(db.Float)
    tilethonghieu = db.Column(db.Float)
    tilevandung = db.Column(db.Float)
    nguoitaoid = db.Column(db.Integer, db.ForeignKey('nguoidung.userid'))

class dethi(db.Model):
    __tablename__ = 'dethi'
    dethiid = db.Column(db.Integer, primary_key=True)
    madethi = db.Column(db.String(255))
    ngaytao = db.Column(db.Date)
    ghichu = db.Column(db.String(255))
    filedethi = db.Column(db.LargeBinary)
    nguoitaoid = db.Column(db.Integer, db.ForeignKey('nguoidung.userid'))
    monhocid = db.Column(db.Integer, db.ForeignKey('monhoc.monhocid'))
    cautrucdethiid = db.Column(db.Integer, db.ForeignKey('cautrucdethi.cautrucdethiid'))

class cauhoi(db.Model):
    __tablename__ = 'cauhoi'
    cauhoiid = db.Column(db.Integer, primary_key=True)
    mucdo = db.Column(db.String(255))
    chuong = db.Column(db.String(255))
    mota = db.Column(db.String(255))
    nguoitaoid = db.Column(db.Integer, db.ForeignKey('giangvien.giangvienid'))
    ngaytao = db.Column(db.Date)
    dethiid = db.Column(db.Integer, db.ForeignKey('dethi.dethiid'))
    noidung = db.Column(db.Text)
    loaicauhoi = db.Column(db.String(50))
    dapan = db.Column(db.Text)
    trangthai = db.Column(db.String(50), default="Chưa duyệt")
    phancongid = db.Column(db.Integer, db.ForeignKey('chitietcongviec.phancongid'))