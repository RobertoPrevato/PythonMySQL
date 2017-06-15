import uuid
from datetime import datetime
from . import DatabaseSession
from .store import MySqlStore
from .entities import AppUser, Picture, PictureDescription, AppLanguage
from sqlalchemy import or_


class UserStore(MySqlStore):

    def create_account(self, email, username, hashed_password, salt, data):
        """
        Creates a new account

        :param email: user's email
        :param username: username
        :param hashed_password: hashed password
        :param salt: salt used to hash the account password
        """
        user_entity = AppUser

        instance = user_entity(email=email,
                               username=username,
                               guid=str(uuid.uuid4()),
                               creation_time=datetime.utcnow(),
                               hashed_password=hashed_password,
                               salt=salt,
                               **data)

        with DatabaseSession() as session:
            session.add(instance)
            session.flush()
            session.commit()

            return self.normalize(instance)

    def delete_account_by_email(self, email):
        """
        Deletes a user account by email, if it exists;

        :param email: user's email
        """
        user_entity = AppUser

        with DatabaseSession() as session:
            data = session.query(user_entity).\
                   filter(user_entity.email == email).\
                   first()
            if data is None:
                return False

            session.delete(data)
            session.commit()
            return True


class PictureStore(MySqlStore):

    """
    Provides methods to handle pictures information in database.
    """
    def insert(self,
               user_id,
               guid,
               medium_guid,
               thumbnail_guid,
               file_name,
               extension,
               content_type,
               width,
               height,
               ratio,
               timestamp):
        """
        Saves a picture for a user of the public area.
        """
        entity = Picture

        instance = entity(user_id=user_id,
                          file_name=file_name,
                          extension=extension,
                          guid=guid,
                          med_guid=medium_guid,
                          thm_guid=thumbnail_guid,
                          width=width,
                          height=height,
                          type=content_type,
                          ratio=ratio,
                          creation_time=timestamp)

        with DatabaseSession() as session:
            session.add(instance)
            session.flush()
            session.commit()
            return self.normalize(instance)

    def update_picture(self, picture_id, params):
        self.update_object(Picture, picture_id, params)

    def delete_picture(self, _id):
        entity = Picture

        with DatabaseSession() as session:
            session.query(entity).\
               filter(entity.id == _id).\
               delete()
            session.commit()
            return True


    def get_user_pictures(self, user_id):
        """
        Gets pictures by user id.

        :param user_id: user id
        """
        with DatabaseSession() as session:
            data = session.query(Picture).\
                   filter(Picture.user_id == user_id).\
                   all()
            user_pictures = self.normalize(data)

        return user_pictures

    def get_pictures_with_descriptions(self, user_id, language):
        """
        Gets pictures by user id.

        :param user_id: user id
        """

        with DatabaseSession() as session:
            q = session.query(Picture, PictureDescription.title, PictureDescription.caption).\
                   outerjoin(PictureDescription).\
                   outerjoin(AppLanguage).\
                   filter(Picture.user_id == user_id).\
                   filter(or_(AppLanguage.code == None, AppLanguage.code == language))
            data = q.all()
            return data

    def delete_picture(self, _id):
        """
        Delete the picture information with the given id.

        :param _id:
        :return:
        """
        entity = Picture

        with DatabaseSession() as session:
            session.query(entity).\
               filter(entity.id == _id).\
               delete()
            session.commit()
            return True

    def delete_picture_by_guid(self, guid):
        """
        Delete the picture information with the given id.

        :param guid: picture guid.
        :return:
        """
        entity = Picture

        with DatabaseSession() as session:
            session.query(entity).\
               filter(entity.guid == guid).\
               delete()
            session.commit()
            return True

    def delete_pictures(self, ids):
        """
        Deletes all pictures information with the given ids.

        :param ids:
        :return:
        """
        entity = Picture

        with DatabaseSession() as session:
            session.query(entity).\
               filter(entity.id.in_(ids)).\
               delete()
            session.commit()
            return True