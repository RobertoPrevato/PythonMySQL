"""
 * Entities; this module was generated automatically from existing database using sqlacodegen tool.
 * https://github.com/RobertoPrevato/PythonMySQL
 *
 * Copyright 2017, Roberto Prevato
 * https://robertoprevato.github.io
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""
# coding: utf-8
from sqlalchemy import Column, DateTime, Float, ForeignKey, Index, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AppLanguage(Base):
    __tablename__ = 'app_language'

    id = Column(Integer, primary_key=True)
    code = Column(String(10), nullable=False, unique=True)
    english_name = Column(String(45), nullable=False)
    original_name = Column(String(45), nullable=False)


class AppUser(Base):
    __tablename__ = 'app_user'

    id = Column(Integer, primary_key=True)
    guid = Column(String(36), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    hashed_password = Column(String(56), nullable=False)
    salt = Column(String(50), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    creation_time = Column(DateTime, nullable=False)
    password_reset_token = Column(String(36))
    confirmation_token = Column(String(36))
    confirmation_time = Column(DateTime)
    newsletter = Column(Integer, nullable=False, server_default=text("'0'"))
    active = Column(Integer, nullable=False, server_default=text("'1'"))
    banned = Column(Integer, nullable=False, server_default=text("'0'"))
    confirmed = Column(Integer, nullable=False, server_default=text("'0'"))
    language = Column(String(2), nullable=False, server_default=text("'en'"))


class Picture(Base):
    __tablename__ = 'picture'

    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey('app_user.id', ondelete='CASCADE', onupdate='CASCADE'), nullable=False, index=True)
    guid = Column(String(36), nullable=False, unique=True)
    med_guid = Column(String(36), nullable=False, unique=True)
    thm_guid = Column(String(36), nullable=False, unique=True)
    file_name = Column(String(300), nullable=False)
    extension = Column(String(3), nullable=False)
    type = Column(String(45), nullable=False)
    width = Column(SmallInteger, nullable=False)
    height = Column(SmallInteger, nullable=False)
    ratio = Column(Float(asdecimal=True), nullable=False)
    creation_time = Column(DateTime, nullable=False)

    user = relationship('AppUser')


class PictureDescription(Base):
    __tablename__ = 'picture_description'
    __table_args__ = (
        Index('UK_picture_description_picture_id_language_id', 'picture_id', 'language_id', unique=True),
    )

    id = Column(Integer, primary_key=True)
    picture_id = Column(ForeignKey('picture.id', ondelete='CASCADE'), nullable=False, index=True)
    language_id = Column(ForeignKey('app_language.id', ondelete='CASCADE'), nullable=False, index=True)
    title = Column(String(100))
    caption = Column(String(255))

    language = relationship('AppLanguage')
    picture = relationship('Picture')
