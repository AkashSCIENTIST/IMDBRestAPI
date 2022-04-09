import mysql.connector
conn = mysql.connector.connect(host='localhost',database='imdb',user='root',password='1234')
cur = conn.cursor(dictionary=True)

schema_quries = [
    '''
    create table actors(
        id integer primary key,
        name varchar(100) not null,
        age integer,
        country varchar(100)
    )''',
    '''
    create table movies(
        id integer primary key,
        name varchar(100) unique not null,
        year_ integer not null
    )
    ''',
    '''
    create table movie_actor(
        movie_id integer,
        actor_id integer,
        constraint fk_movie_id foreign key (movie_id) references movies(id),
        constraint fk_actor_id foreign key (actor_id) references actors(id),
        constraint pk_table primary key (movie_id, actor_id)
    )
    '''
]

def createSchemas():
    for i in schema_quries:
        try:
            cur.execute(i)
        except:
            print("Exception at table creation")

def allMovies():
    query = "select * from movies"
    cur.execute(query)
    return cur.fetchall()

def movieById(id):
    query = "select * from movies where id = {}".format(id)
    cur.execute(query)
    return cur.fetchall()

def allActors():
    query = "select * from actors"
    cur.execute(query)
    return cur.fetchall()

def actorById(id):
    query = "select * from actors where id = {}".format(id)
    cur.execute(query)
    return cur.fetchall()

def allMovieActor():
    query = "select * from movie_actor"
    cur.execute(query)
    return cur.fetchall()

def insertActor(id, name, age, country):
    query = "insert into actors values ({}, '{}', {}, '{}')".format(id, name, age, country)
    print(query)
    cur.execute(query)
    conn.commit()

def insertMovie(id, name, year):
    query = "insert into movies values ({}, '{}', {})".format(id, name, year)
    #print(query)
    cur.execute(query)
    conn.commit()

def insertMovieActor(movie_id, actor_id):
    query = "insert into movie_actor values ({}, {})".format(movie_id, actor_id)
    cur.execute(query)
    conn.commit()

def moviesByActor(actor_id):
    query = "select * from movies where id in (select movie_id from movie_actor where actor_id = {})".format(actor_id)
    cur.execute(query)
    l = cur.fetchall()
    return l

def actorsByMovie(movie_id):
    query = "select * from actors where id in (select actor_id from movie_actor where movie_id = {})".format(movie_id)
    cur.execute(query)
    l = cur.fetchall()
    return l

def getMasterTable():
    query = "select movies.id as movie_id, movies.name as movie_name, movies.year_ as released_year, actors.id as actor_id, actors.name as actor_name, actors.age as actor_age, actors.country as actor_country from movie_actor inner join movies on movies.id = movie_actor.movie_id inner join actors on actors.id = movie_actor.actor_id"
    cur.execute(query)
    return cur.fetchall()

if __name__ == '__main__':
    createSchemas()