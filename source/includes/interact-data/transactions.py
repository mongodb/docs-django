from django.db import transaction
from sample_mflix.models import Movie

# start-transaction-decorator
@transaction.atomic
def run_movie_transaction():
    Movie.objects.create(
        title="Poor Things",
        runtime=141,
        genres=["Comedy", "Romance"]
    )
# end-transaction-decorator

# start-transaction-manager
def run_movie_transaction():
    with transaction.atomic():
        Movie.objects.create(
            title="Poor Things",
            runtime=141,
            genres=["Comedy", "Romance"]
        )
# end-transaction-manager