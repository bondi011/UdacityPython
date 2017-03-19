import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", 
	"A story of a boy and his toys that come to life",
	"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
	"https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.storyline)

avatar = media.Movie("Avatar", 
	"A Marine on an alien planet", 
	"https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")
print(avatar.storyline)

#avatar.show_trailer()

a_few_good_men = media.Movie("A Few Good Men",
	"A story about a court room", 
	"https://upload.wikimedia.org/wikipedia/en/4/45/A_Few_Good_Men_poster.jpg",
	"https://www.youtube.com/watch?v=ePo91pMcu94")
#a_few_good_men.show_trailer()

school_of_rock = media.Movie("School of Rock",
	"Using rock music to learn",
	"https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
	"https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in paris",
	"https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
	"https://www.youtube.com/watch?v=c3sBBRxDAqk",)

hunger_games = media.Movie("Hunger Games",  "Fighting for freedom from opression",
	"https://upload.wikimedia.org/wikipedia/en/4/4b/Hunger_Games_Film_Poster.jpg",
	"https://www.youtube.com/watch?v=mfmrPu43DF8")

movies = [toy_story, avatar, a_few_good_men, school_of_rock, ratatouille, hunger_games]
fresh_tomatoes.open_movies_page(movies)