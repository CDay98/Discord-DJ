import json
import discord

def write_json(new_data, filename):
		with open(filename) as f:
		    data = json.load(f)
		
		data.update(new_data)
		
		with open(filename, 'w') as f:
		    json.dump(data, f)

def read_json(filename):
		with open(filename) as f:
				data = json.load(f)
		return data

def set_movies(user, movies = []):
		data = {user: movies}
		write_json(data, 'Profile Data/user_movies.json')

def get_movies(username):
		data = read_json('Profile Data/user_movies.json')
		try:
				user_data = data[username]
				return user_data
		except KeyError:
				return([])

def set_songs(user, songs = []):
		data = {user: songs}
		write_json(data, 'Profile Data/user_songs.json')

def get_songs(username):
		data = read_json('Profile Data/user_songs.json')
		try:
				user_data = data[username]
				return user_data
		except KeyError:
				return([])

def profile_embed(username, songs, movies):
		movies = '\n'.join(movies)
		songs =  '\n'.join(songs)
		embed = discord.Embed(title=f'**{username}**').add_field(
			name='**Top Movies**', value = f'{movies}').add_field(
			name='**Top Songs**', value = f'{songs}')
		
		return embed