# Wednesday Review #

# Create a class `MovieReview` which has required attributes `movie_title:str`, `reviewer_name:str`, `score:int`, `date_reviewed:datetime.date`.
	# You may need to look up how to use `datetime.date` (hint: you'll need `from datetime import date`)

# Create a `__repr__` instance method for your reviews so that you can see their necessary information.

# Create an instance method `pretty_print()` which prints the review like so: `"<movie_title> review by <reviewer_name> on <date_reviewed>: <score> / 5 stars"`.
	# Example: `land_before_time.pretty_print()` >>> `"Land Before Time review by Fred Flintstone on 2014-4-12: 5/5 stars"`

# Create an instance method `increase_score()` which increases that movie's score by 1 but not above 5.

# Create an instance method `update_review()`. This accepts an argument of a `new_score` and optionally a `new_reviewer`. This updates the `score` and sets the `date_reviewed` to today.  If `new_reviewer` was passed this will also update the `reviewer_name` and if not it will retain the previous `reviewer_name`.
	# Example: `land_before_time.update_review(4)` # score changed to `4`, date becomes today, reviewer is still `"Fred Flinstone"`
	# Example: `land_before_time.update_review(5, "Littlefoot")` # score changed to `5`, date becomes today, reviewer becomes `"Littlefoot"`

# Create a class method `review_bomb()` which accepts a `movie_title` and `num_reviews`. This generates a review `num_reviews` times for the `movie_title` each with a `score` of 1, a `reviewer_name` of `Statler & Waldorf`, and a `date_reviewed` of today. Return all instances in a list.
	# Example: `MovieReview.review_bomb("Plan 9 From Outer Space", 10)` >>> creates 10 reviews for "Plan 9 From Outer Space"


import datetime

class MovieReview:

	def __init__(self, movie_title, reviewer_name, score, date_reviewed):
		self.movie_title = movie_title
		self.reviewer_name = reviewer_name
		self.score = score
		self.date_reviewed = date_reviewed

	def formatted_date(self):
		return self.date_reviewed.strftime('%b %d %Y')

	def __repr__(self):
		return f"MovieReview(movie_title='{self.movie_title}', reviewer_name='{self.reviewer_name}', score={self.score}, date_reviewed={self.formatted_date()})"

	def pretty_print(self):
		return f"{self.movie_title} review by {self.reviewer_name} on {self.formatted_date()}: {self.score} / 5 stars"

	def increase_score(self):
		if (self.score <= 4):
			self.score += 1
		else:
			self.score = 5

	def update_review(self, new_score, new_reviewer=None):
		# set the score
		self.score = new_score
		# set new_reviewer if exists
		if (new_reviewer):
			self.reviewer_name = new_reviewer
		# set date to now
		self.date_reviewed = datetime.datetime.now()

	@classmethod # class method decorator
	def review_bomb(self, movie_title, num_reviews):
		counter = 0
		new_reviews = []
		while counter < num_reviews:
			new_rev = MovieReview(
				movie_title=movie_title, 
				score=1,
				date_reviewed=datetime.datetime.now(),
				reviewer_name="Statler & Waldorf"
			)
			new_reviews.append( new_rev )
			counter += 1
		return new_reviews


spiderman = MovieReview(
	movie_title="Spiderman: Brand New Day", 
	reviewer_name="Chett", 
	score=4, 
	date_reviewed=datetime.datetime.now()
)