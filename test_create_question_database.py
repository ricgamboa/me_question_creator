# Used only to create test question database

import sqlite3
from pathlib import Path
import json


def main():
    create_new = input("Are you sure do you want to erase existing database and create a new one? [y/n]: ")
    if create_new.lower() == "yes" or create_new.lower() == "y":
        config_file_path = Path.cwd().joinpath("me_question_creator_pkg", "config_file")
        with open(config_file_path) as config_file:
            config_info = json.load(config_file)
            database_path = Path(config_info["QUESTION_DATABASE_PATH"])
        connection = sqlite3.connect(database_path)
        cursor = connection.cursor()
        cursor.executescript("DROP TABLE IF EXISTS question;"
                             "CREATE TABLE question("
                                 "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,"
                                 "global_question_id INTEGER UNIQUE,"
                                 "num_letters INTEGER,"
                                 "icons TEXT,"
                                 "positions TEXT);")
        connection.commit()
        cursor.close()
    else:
        print("Good bye")

if __name__ == "__main__":
    main()