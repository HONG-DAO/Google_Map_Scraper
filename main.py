from src.gmaps import Gmaps
from src.fields import Fields
from src import write_output as write_output_module
queries = [
   "quán ăn vặt quận 3"
]

all_places = Gmaps.places(
    queries,
    max=5,
    fields=[
        Fields.NAME,
        Fields.DESCRIPTION,
        Fields.ADDRESS,
        Fields.RATING,
        Fields.WEBSITE,
        Fields.REVIEWS,
        Fields.WORKDAY_TIMING,
        Fields.CLOSED_ON,
        Fields.CATEGORIES,
        Fields.IMAGES,
    ],
    scrape_reviews=True,
    reviews_max=29,
    lang="vi",
    convert_to_english=False,
)
# Add this in your main script
for result in all_places:
    for place in result["places"]:
        print(f"Place: {place.get('name', 'Unknown')}")
        print(f"Reviews count: {place.get('reviews', 'Not found')}")
        print(f"Has reviews field: {'reviews' in place}")
        print("---")
places_only = []
for result in all_places:
    places_only.extend(result["places"])

write_output_module.write_output("quán ăn vặt quận 3", places_only, [
        Fields.NAME,
        Fields.DESCRIPTION,
        Fields.ADDRESS,
        Fields.RATING,
        Fields.WEBSITE,
        Fields.REVIEWS,
        Fields.WORKDAY_TIMING,
        Fields.CLOSED_ON,
        Fields.CATEGORIES,
        Fields.IMAGES,
])