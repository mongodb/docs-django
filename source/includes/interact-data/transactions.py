from django.db import transaction, DatabaseError
from sample_mflix.models import Movie

# start-transaction-decorator
@transaction.atomic
def insert_movie_transaction():
    Movie.objects.create(
        title="Poor Things",
        runtime=141,
        genres=["Comedy", "Romance"]
    )
# end-transaction-decorator

# start-transaction-manager
def insert_movie_transaction():
    with transaction.atomic():
        Movie.objects.create(
            title="Poor Things",
            runtime=141,
            genres=["Comedy", "Romance"]
        )
# end-transaction-manager

# start-callback
def get_horror_comedies():
    movies = Movie.objects.filter(genres=["Horror", "Comedy"])
    for m in movies:
        print(f"Title: {m.title}, runtime: {m.runtime}")

def insert_movie_with_callback():
    with transaction.atomic():
        Movie.objects.create(
            title="The Substance",
            runtime=140,
            genres=["Horror", "Comedy"]
        )
        
        transaction.on_commit(get_horror_comedies)
# end-callback

# start-handle-errors
movie = Movie.objects.get(
    title="Jurassic Park",
    released=timezone.make_aware(datetime(1993, 6, 11))
)
try:
    with transaction.atomic():
        movie.update(title="Jurassic Park I")
except DatabaseError:
    movie.update(title="Jurassic Park")
# end-handle-errors