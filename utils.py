import sqlite3


def movie_finder(movie_name):
    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                       SELECT show_id
                       FROM netflix
                       WHERE title = '{movie_name}'
                       ORDER BY release_year DESC
                       LIMIT 5
        """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    if result:
        return result[0][0]
    else:
        return None


def info_by_id(id):
    dict_info = ['title', 'country', 'release_year', 'description']
    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                       SELECT title, country, release_year, description
                       FROM netflix
                       WHERE show_id = '{id}'
        """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    return dict(zip(dict_info, list(result[0])))


def year_to_year(year, year_2):
    output_list = []
    dict_info = ['title', 'release_year']

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                       SELECT title, release_year
                       FROM netflix
                       WHERE release_year BETWEEN {year} AND {year_2} 
                       LIMIT 100
        """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


def movie_for_children():
    output_list = []
    dict_info = ['title', 'rating', 'description']

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                           SELECT title, rating, description
                           FROM netflix
                           WHERE rating = 'G'
                           LIMIT 100
            """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


def movie_for_family():
    output_list = []
    dict_info = ['title', 'rating', 'description']

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                           SELECT title, rating, description
                           FROM netflix
                           WHERE rating IN ('G', 'PG', 'PG-13')
                           LIMIT 100
            """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


def movie_for_adult():
    output_list = []
    dict_info = ['title', 'rating', 'description']

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                           SELECT title, rating, description
                           FROM netflix
                           WHERE rating IN ('R', 'NC-17')
                           LIMIT 100
            """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


def movie_by_listed_in(genre):
    output_list = []
    dict_info = ['title', 'description']

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                           SELECT title, description
                           FROM netflix
                           WHERE listed_in LIKE '%{genre}%'
                           ORDER BY release_year DESC
                           LIMIT 10
            """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


# TODO ШАГ 5
def two_actor(actor_1, actor_2):  # Я не понял задание, реально, поэтому сделал то, что выглядит логичнее всего;(
    output_list = []  # Очень коряво сделано, потому что не это надо было искать, а если вдруг надо было искать это,
    dict_info = ['title', 'cast']  # то я быстренько все переделаю ^^
    unique_actor_list = []

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                              SELECT netflix.cast
                              FROM netflix
                              WHERE netflix.cast LIKE '%{actor_1}%' AND netflix.cast LIKE '%{actor_2}%'
                              ORDER BY release_year DESC
                              LIMIT 10
               """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    a = sum(([list(x) for x in result]),[])
    list_ = []
    for b in a:
        list_.append(b.split(", "))
    for movie_actors in list_:
        for actor in movie_actors:
            film_count = 0
            for movie_actors_for_check in list_:
                if actor in movie_actors_for_check:
                    film_count += 1
                if film_count == 3:
                    unique_actor_list.append(actor)
    return unique_actor_list


# TODO ШАГ 6
def film_by(type, release_year, genre):
    dict_info = ['title', 'description']
    output_list = []

    with sqlite3.connect("./netflix.db") as con:
        cur = con.cursor()
        sqlite_query = f"""
                              SELECT title, description
                              FROM netflix
                              WHERE type = '{type}' AND release_year = '{release_year}' AND listed_in LIKE '%{genre}%'
                              ORDER BY release_year DESC
                              LIMIT 10
               """
        result = cur.execute(sqlite_query)
        executed_query = cur.fetchall()

    result = executed_query
    for row in result:
        output_list.append(dict(zip(dict_info, row)))

    return output_list


print(film_by("Movie", 2020, 'Drama'))
# print(two_actor("Jack Black", "Dustin Hoffman"))
