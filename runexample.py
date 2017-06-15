"""
 * Demonstration.
 * https://github.com/RobertoPrevato/PythonMySQL
 *
 * Copyright 2017, Roberto Prevato
 * https://robertoprevato.github.io
 *
 * Licensed under the MIT license:
 * http://www.opensource.org/licenses/MIT
"""
import uuid
from datetime import datetime
from dal.examples import UserStore, PictureStore


if __name__ == "__main__":
    users_store = UserStore()
    pictures_store = PictureStore()

    user_email = "example@gmail.com"
    user_name = "John Doe"

    print("[*] Deleting user account, if it exists...")
    deleted = users_store.delete_account_by_email(user_email)

    print("[*] Inserting user account...")
    # insert new user;
    user_data = users_store.create_account(user_email, user_name, "HASHED_PASSWORD", "PASSWORD_SALT", {})

    print("[*] Inserting user picture...")
    pictures_store.insert(user_data.id,
                          str(uuid.uuid4()),
                          str(uuid.uuid4()),
                          str(uuid.uuid4()),
                          "file_name",
                          "jpg",
                          "image/jpeg",
                          400,
                          400,
                          1,
                          datetime.utcnow())