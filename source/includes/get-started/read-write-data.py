# start-query-email
from sample_mflix.models import Movie, Viewer

Viewer.objects.filter(email="jason_momoa@gameofthron.es").first()
# end-query-email

# start-query-runtime
Movie.objects.filter(runtime__lt=10)
# end-query-runtime