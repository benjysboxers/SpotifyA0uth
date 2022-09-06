# SpotifyA0uth
Python code using the Spotify API and Other Libraries to get access to and display the songs within your Playlist

How It Works:
Create a Spotify/Sign into already existing Spotify Account

Go On The Spotify Developer Portal, this is how you interact with the Spotify API mostly And you Should see these two things below:

![image](https://user-images.githubusercontent.com/94329833/188719063-4fadfb68-f341-4890-8c25-e4451fa67773.png)

ClientID - is your Spotify User ID, that is how Spotify Authenticates User Access

ClientSecret - this is basically like a password for your authentication essentially the applications own password, do not share this

Once you get the clientID and ClientSecret place it in another python file I named mine "secrets.py",
then refrence it within the main script by importing clientSecret and clientID from that named file

![image](https://user-images.githubusercontent.com/94329833/188720368-8e98cc39-0d71-423b-9844-599f4c214c70.png)

You can also read up on the SpotifyAPI and play around with it if you want or are Interested in learning
about the Spotify API here:

https://developer.spotify.com/documentation/web-api/

Run the code and watch it do its magic.

Side note: You can only run your own saved playlist and not other people's playlist like you friends for example. This Code was forked from a repo with my own implementations here and there feel free to use and mess around with it as you wish.

If anything is unclear feel free to reach out to me on discord for clarification. 
