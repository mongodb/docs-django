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