#Cesar Murillo
#CIS261
#Movie Guide Part 2

def initial_file():
    with open('movies.txt', 'w') as file:
        file.write("Cat On A Hot Tin Roof\nOn The Waterfront\nMonty Python And The Holy Grail\n")

def display_menu():
    print("\nWelcome To The Movie List Guide!",
          "\n_______________________________\n",
          "\n1. Display All Movie Titles",
          "\n2. Add A Movie Title",
          "\n3. Delete A Movie Title",
          "\n4. Exit the Movie Guide")
    
def read_movies_from_file(filename):
    movies = []
    with open(filename, 'r') as file:
        for line in file:
            movies.append(line.strip())
    return movies

def display_movies_list(movies):
    if movies:
        print("\nMovie Titles: \n")
        for i, movie in enumerate(movies, start = 1):
            print(f"{i}. {movie}")
    else:
        print("No Movies To Display\n")
        
def add_movie_title(movies):
    new_movie = input("\nPlease Enter The Title Of The New Movie To Add To The List: ")
    movies.append(new_movie)
    write_movies_to_file(movies)
    print(f"\n'{new_movie}' Has Been Added Successfully.\n")
    display_movies_list(movies)

def delete_movie_title(movies):
    try:
        title_to_delete = int(input("\nPlease Enter The Number Of The Movie To Delete: "))
        if 1 <= title_to_delete <= len(movies):
            removed_movie = movies.pop(title_to_delete - 1 )
            write_movies_to_file(movies)
            print(f"\n'{removed_movie}' has been deleted.")
            display_movies_list(movies)
        else:
            print("Movie Title Not Found.")
    except ValueError:
        print("Invalid Entry! Please Try Again.")
        
def write_movies_to_file(movies):
    with open('movies.txt', 'w') as file:
        for movie in movies:
            file.write(movie + '\n')
        
def main():
    movie_file = "movies.txt"
    movies = read_movies_from_file(movie_file)
    initial_file()
    
    while True:
        display_menu()
        selection = input("\nPlease Enter A Selection (1-4): ")
        if selection == '1':
            display_movies_list(movies)
        elif selection == '2':
            add_movie_title(movies)
        elif selection == '3':
            delete_movie_title(movies)
        elif selection == '4':
            print("\nThanks For Using The Movie Guide!!!")
            break
        else:
            print("\nInvalid Selection! Please Try Again.\n")
            
if __name__ == "__main__":
    main()
